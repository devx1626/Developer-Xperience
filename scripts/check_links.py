#!/usr/bin/env python3
"""External link checker for the generated site.

Collects external http(s) URLs from src/href attributes in the generated
HTML pages and verifies each responds successfully.

Behavior:
  - HEAD request first, GET fallback (many sites reject HEAD)
  - 10s timeout per request, 2 retries on transient failures
  - bot-wary responses (403/429/999, common anti-scraping blocks) count as
    warnings, not failures - the link exists but refuses automated clients
  - honors a built-in allowlist plus optional scripts/link-allowlist.txt
    (one substring per line, e.g. a hostname); matched URLs are skipped
  - a custom User-Agent identifies the checker

Exit codes: 0 = all links ok/warned, 1 = at least one broken link.

Usage: python3 scripts/check_links.py [page.html ...]
Defaults to index.html, html.html, css.html.
"""
import re
import sys
import time
import urllib.error
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

DEFAULT_PAGES = ['index.html', 'html.html', 'css.html']
ALLOWLIST_FILE = ROOT / 'scripts' / 'link-allowlist.txt'

TIMEOUT = 10
RETRIES = 2
USER_AGENT = 'Mozilla/5.0 (compatible; DeveloperXperience-link-checker/1.0)'

# Substring matches: URLs containing these are skipped entirely.
# Keep this minimal - a link should only be allowlisted if it is valid but
# refuses automated checks (rate limits, aggressive bot protection).
ALLOWLIST = [
    'roadmap.sh',  # rate-limits automated requests from CI runners
    'developer.mozilla.org',  # aggressive bot protection on some paths
    'webaim.org',  # intermittent bot walls
]

# Anti-bot responses that mean "link is fine, we just block robots".
BOT_BLOCKED = {403, 406, 429, 999, 503}

ATTR_RE = re.compile(r'(?:src|href)=(["\'])(https?://[^"\']+)\1', re.I)


def collect_external_urls(pages):
    urls = set()
    for page in pages:
        text = (ROOT / page).read_text(encoding='utf-8')
        for _, url in ATTR_RE.findall(text):
            # fragment-only differences are the same resource
            urls.add(url.split('#')[0])
    return sorted(u for u in urls if u.startswith('http'))


def load_allowlist():
    entries = list(ALLOWLIST)
    if ALLOWLIST_FILE.exists():
        for line in ALLOWLIST_FILE.read_text(encoding='utf-8').splitlines():
            line = line.strip()
            if line and not line.startswith('#'):
                entries.append(line)
    return entries


def is_allowed(url, allowlist):
    return any(entry in url for entry in allowlist)


def request_once(url, method):
    req = urllib.request.Request(url, method=method, headers={'User-Agent': USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            return resp.status, None
    except urllib.error.HTTPError as e:
        return e.code, None
    except (urllib.error.URLError, TimeoutError, OSError) as e:
        reason = getattr(e, 'reason', e)
        return None, str(reason)


def check_url(url):
    """Return (status, detail) where status is 'ok', 'warn', or 'fail'."""
    last_detail = None
    for attempt in range(RETRIES + 1):
        for method in ('HEAD', 'GET'):
            code, detail = request_once(url, method)
            if code is None:
                last_detail = detail
                continue  # network-level error: try GET, then retry
            if 200 <= code < 400:
                return 'ok', str(code)
            if code in BOT_BLOCKED:
                return 'warn', f'HTTP {code} (bot-blocked, link likely valid)'
            if code in (404, 410):
                # deterministic failure - no point retrying
                return 'fail', f'HTTP {code}'
            last_detail = f'HTTP {code}'
        if attempt < RETRIES:
            time.sleep(1.5 * (attempt + 1))
    return 'fail', last_detail or 'no response'


def main():
    pages = sys.argv[1:] or DEFAULT_PAGES
    missing = [p for p in pages if not (ROOT / p).exists()]
    if missing:
        print(f'pages not found: {", ".join(missing)} (run `npm run build` first?)')
        sys.exit(1)

    allowlist = load_allowlist()
    urls = collect_external_urls(pages)
    skipped = [u for u in urls if is_allowed(u, allowlist)]
    to_check = [u for u in urls if not is_allowed(u, allowlist)]

    print(f'{len(urls)} external URLs ({len(skipped)} allowlisted, '
          f'{len(to_check)} to check)\n')

    failures = []
    warnings = []
    for i, url in enumerate(to_check, 1):
        status, detail = check_url(url)
        marker = {'ok': 'OK  ', 'warn': 'WARN', 'fail': 'FAIL'}[status]
        print(f'[{i}/{len(to_check)}] {marker} {url}' +
              ('' if status == 'ok' else f'  -> {detail}'))
        if status == 'fail':
            failures.append((url, detail))
        elif status == 'warn':
            warnings.append((url, detail))

    print(f'\nchecked: {len(to_check)}, ok: {len(to_check) - len(failures) - len(warnings)}, '
          f'warnings: {len(warnings)}, failures: {len(failures)}')
    if warnings:
        print('\nWarnings (bot-blocked, treated as valid):')
        for url, detail in warnings:
            print(f'  - {url} ({detail})')
    if failures:
        print('\nBroken links:')
        for url, detail in failures:
            print(f'  - {url} ({detail})')
        print('\nIf a link is genuinely valid but blocks checkers, add its '
              'hostname to scripts/link-allowlist.txt.')
        sys.exit(1)
    print('\nAll links OK')


if __name__ == '__main__':
    main()
