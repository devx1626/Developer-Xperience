#!/bin/bash
# GitHub Secrets Setup Script for Claude Code
# 
# This script helps set up the ANTHROPIC_API_KEY secret in your GitHub repository.
# 
# Prerequisites:
# 1. You have a GitHub personal access token with repo scope
# 2. You have an Anthropic API key from https://console.anthropic.com
#
# Usage:
#   ./setup-github-secrets.sh
#
# The script will prompt for:
# 1. Your GitHub personal access token
# 2. Your Anthropic API key
# 3. The repository name (owner/name)

set -e

echo "GitHub Secrets Setup for Claude Code"
echo "===================================="

# Get GitHub token
read -p "Enter your GitHub personal access token (or press Enter to skip): " GITHUB_TOKEN

if [ -z "$GITHUB_TOKEN" ]; then
    echo "Skipping GitHub token setup"
    exit 0
fi

# Get Anthropic API key
read -p "Enter your Anthropic API key (sk-ant-...): " ANTHROPIC_API_KEY

if [ -z "$ANTHROPIC_API_KEY" ]; then
    echo "Error: Anthropic API key is required"
    exit 1
fi

# Get repository name
read -p "Enter repository name (owner/name, e.g. your-org/your-repo): " REPO_NAME

if [ -z "$REPO_NAME" ]; then
    echo "Error: Repository name is required"
    exit 1
fi

# Set the secret using GitHub CLI
echo "Setting ANTHROPIC_API_KEY secret in $REPO_NAME..."
gh secret set ANTHROPIC_API_KEY --repo "$REPO_NAME" --body "$ANTHROPIC_API_KEY"

echo ""
echo "✓ ANTHROPIC_API_KEY secret has been set successfully!"
echo ""
echo "Next steps:"
echo "1. The GitHub workflow at .github/workflows/claude.yml is now active"
echo "2. Tag @claude in issue comments or PR review comments to trigger Claude Code"
echo "3. Claude Code will respond to @claude mentions with code analysis/review"