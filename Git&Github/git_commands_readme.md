# 📘 Git Commands Tutorial – Step by Step Guide

This README will help you and your students **learn Git commands step by step** with examples. Each section contains explanations and terminal commands that can be practiced directly.

---

## 🔹 1. Setup & Configuration
```bash
git --version                         # Check Git version
git config --global user.name "Your Name"       # Set username
git config --global user.email "your@email.com" # Set email
git config --list                      # Show all configs
```

✅ *Tip: Configure your identity before making commits.*

---

## 🔹 2. Starting a Repository
```bash
git init                               # Initialize a new local repo
git clone <repo_url>                   # Clone remote repo
```

✅ Example:
```bash
git clone https://github.com/username/project.git
```

---

## 🔹 3. Basic Snapshotting
```bash
git status                             # Check status of working directory
git add <file>                         # Stage a file
git add .                              # Stage all files
git reset <file>                       # Unstage a file

git commit -m "Message"                # Commit with message
git commit -am "Message"               # Stage + commit tracked files

git diff                               # Show unstaged changes
git diff --staged                      # Show staged changes
```

---

## 🔹 4. Branching & Merging
```bash
git branch                             # List branches
git branch <name>                      # Create branch
git checkout <name>                    # Switch branch
git checkout -b <name>                 # Create + switch to branch
git merge <branch>                     # Merge branch into current
git branch -d <name>                   # Delete branch
git branch -D <name>                   # Force delete branch
```

✅ Example:
```bash
git checkout -b feature-login          # Create new branch
```

---

## 🔹 5. Remote Repositories
```bash
git remote -v                          # Show remotes
git remote add origin <url>            # Add remote
git push -u origin main                # Push first time
git push                               # Push changes
git pull                               # Fetch + merge changes
git fetch                              # Fetch latest changes
```

---

## 🔹 6. Undoing Changes
```bash
git restore <file>                     # Discard unstaged changes
git reset --soft HEAD~1                # Undo last commit (keep staged)
git reset --mixed HEAD~1               # Undo last commit (keep unstaged)
git reset --hard HEAD~1                # Undo last commit (remove changes)
git revert <commit_id>                 # Revert a specific commit
```

---

## 🔹 7. Stashing (Temporary Save)
```bash
git stash                              # Save changes temporarily
git stash list                         # Show stashes
git stash apply                        # Reapply last stash
git stash pop                          # Reapply + delete last stash
git stash drop                         # Delete stash
```

---

## 🔹 8. Logs & History
```bash
git log                                # Show commit history
git log --oneline                      # Compact view
git log --graph --oneline --all        # Graph view
git show <commit_id>                   # Show commit details
git blame <file>                       # Show who changed each line
```

---

## 🔹 9. Tagging
```bash
git tag                                # List tags
git tag v1.0                           # Create tag
git tag -a v1.0 -m "Release 1.0"       # Annotated tag
git push origin v1.0                   # Push tag
git push --tags                        # Push all tags
```

---

## 🔹 10. Collaboration
```bash
git fetch origin                       # Fetch latest
git pull origin main                   # Pull from main
git push origin main                   # Push to main
```

---

## 🔹 11. Advanced Commands
```bash
git cherry-pick <commit_id>            # Apply commit from another branch
git rebase main                        # Replay commits on top of main
git reflog                             # Show history of HEAD changes
git clean -f                           # Remove untracked files
git clean -fd                          # Remove untracked files & folders
```

---

# ✅ Quick Git Workflow Example
```bash
git init                               # Start repo
git add .                              # Stage changes
git commit -m "First commit"           # Commit
git branch dev                         # Create branch
git checkout dev                       # Switch to dev branch
git push -u origin dev                 # Push branch to remote
```

---

⚡ **Shortcut Summary**  
- `init` → start repo  
- `clone` → copy repo  
- `add` → stage files  
- `commit` → save changes  
- `push` → upload to remote  
- `pull` → download + merge  
- `branch` → manage branches  
- `merge` → combine branches  
- `stash` → temporary save  
- `rebase` → rewrite history  

---

🚀 This covers almost **all Git commands** your students will need. They can practice step by step following this guide.

