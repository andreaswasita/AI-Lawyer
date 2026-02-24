@echo off
echo ========================================
echo AI Lawyer - GitHub Repository Setup
echo ========================================
echo.

echo Step 1: Authenticate with GitHub CLI
echo Please follow the prompts to authenticate...
echo.
gh auth login --web
echo.

echo Step 2: Create Private Repository
echo.
cd /d C:\Users\anwasita\AI-Lawyer
gh repo create AI-Lawyer --private --description "Democratizing Legal Services for Indonesian Citizens - AI-powered legal platform" --source=. --remote=origin
echo.

echo Step 3: Initialize Git Repository
git init
git add .
git commit -m "Initial commit: AI Lawyer platform - MVP foundation"
echo.

echo Step 4: Push to GitHub
git branch -M main
git push -u origin main
echo.

echo ========================================
echo Repository Setup Complete!
echo ========================================
echo.
echo Repository URL: https://github.com/yourusername/AI-Lawyer
echo.
echo Next Steps:
echo 1. Configure branch protection rules in GitHub
echo 2. Add collaborators
echo 3. Set up GitHub Actions secrets
echo 4. Enable Dependabot security updates
echo.
pause
