#!/usr/bin/env python3
"""Structural validation for the generated site.

Checks, per generated HTML page:
  - tag balance (every open has a matching close, in order)
  - no duplicate id attributes
  - every internal anchor (#foo) resolves to an existing id
  - no heading-level skips (e.g. h2 straight to h4)
  - every local src/href reference resolves to a file on disk

Also checks:
  - style.css brace balance
  - webmanifest parses as JSON and its icon files exist

Usage: python3 scripts/validate_html.py [page.html ...]
Defaults to index.html, html.html, css.html.
"""
import json
import os
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

VOID = {
    'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link',
    'meta', 'param', 'source', 'track', 'wbr',
}

DEFAULT_PAGES = ['index.html', 'html.html', 'css.html']


class PageChecker(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []       # (tag, line)
        self.errors = []
        self.ids = set()
        self.heads = []
        self.hrefs = []
        self.refs = []        # local src/href references

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        line = self.getpos()[0]
        if tag not in VOID:
            self.stack.append((tag, line))
        if 'id' in d:
            if d['id'] in self.ids:
                self.errors.append(f'line {line}: duplicate id "{d["id"]}"')
            self.ids.add(d['id'])
        if tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            self.heads.append(int(tag[1]))
        if tag == 'a' and 'href' in d:
            self.hrefs.append((d['href'], line))
        for k in ('src', 'href'):
            v = d.get(k)
            if v and not v.startswith(('http://', 'https://', '//', '#', 'mailto:', 'data:')):
                self.refs.append((v, line))

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if self.stack and self.stack[-1][0] == tag:
            self.stack.pop()
        else:
            self.errors.append(f'line {self.getpos()[0]}: unexpected </{tag}>')


def check_page(path):
    problems = []
    src = path.read_text(encoding='utf-8')
    c = PageChecker()
    c.feed(src)

    for tag, line in c.stack:
        problems.append(f'line {line}: <{tag}> never closed')
    problems.extend(c.errors)

    # internal anchors resolve
    targets = c.ids
    for href, line in c.hrefs:
        if href.startswith('#') and href != '#':
            if href[1:] not in targets:
                problems.append(f'line {line}: anchor "{href}" has no target')

    # heading level skips (h2 straight to h4 etc.)
    skips = [
        (c.heads[i - 1], c.heads[i])
        for i in range(1, len(c.heads))
        if c.heads[i] > c.heads[i - 1] + 1
    ]
    for prev, cur in skips:
        problems.append(f'heading level skip h{prev} -> h{cur}')

    # local references resolve to files
    for ref, line in c.refs:
        target = ROOT / ref.split('#')[0].split('?')[0]
        if not target.exists():
            problems.append(f'line {line}: missing file "{ref}"')

    return problems


def check_css(path):
    css = path.read_text(encoding='utf-8')
    opens, closes = css.count('{'), css.count('}')
    if opens != closes:
        return [f'brace mismatch: {opens} open vs {closes} close']
    return []


def check_manifest(path):
    problems = []
    try:
        manifest = json.loads(path.read_text(encoding='utf-8'))
    except json.JSONDecodeError as e:
        return [f'invalid JSON: {e}']
    for icon in manifest.get('icons', []):
        if 'src' not in icon:
            problems.append('icon without "src"')
        elif not (ROOT / icon['src']).exists():
            problems.append(f'icon file missing: {icon["src"]}')
    return problems


def main():
    page_names = sys.argv[1:] or DEFAULT_PAGES
    failures = 0

    for name in page_names:
        path = ROOT / name
        if not path.exists():
            print(f'FAIL {name}: file not found (run `npm run build` first?)')
            failures += 1
            continue
        problems = check_page(path)
        if problems:
            failures += 1
            print(f'FAIL {name}:')
            for p in problems:
                print(f'  - {p}')
        else:
            print(f'OK   {name}')

    for rel, fn in (('assets/css/style.css', check_css),
                    ('site.webmanifest', check_manifest)):
        problems = fn(ROOT / rel)
        if problems:
            failures += 1
            print(f'FAIL {rel}:')
            for p in problems:
                print(f'  - {p}')
        else:
            print(f'OK   {rel}')

    if failures:
        print(f'\n{failures} file(s) failed validation')
        sys.exit(1)
    print('\nAll checks passed')


if __name__ == '__main__':
    main()
