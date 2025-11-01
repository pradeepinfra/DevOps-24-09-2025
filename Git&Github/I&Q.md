# 🧩 Git Concepts and Practical Scenarios — Q&A

This document contains detailed explanations and real-world examples for common Git interview and hands-on questions.

---

## **4. Git Fork vs Git Clone**

### 🔹 Explanation
- **Git Fork**: Creates a *copy* of someone else's repository in your own GitHub account. Used to propose changes without affecting the original repo.
- **Git Clone**: Creates a *local copy* of a repository (from your own or someone else’s account).

### 💡 Example
- You want to contribute to an open-source project → **Fork** the repo.
- You want to work on your own project locally → **Clone** the repo.

```bash
# Fork: Done via GitHub UI
# Clone:
git clone https://github.com/username/project.git
```

---

## **5. Scenario where Git Fork is used instead of Git Clone**

If you want to make changes to an external project you don’t have write access to (like an open-source repo), you **fork** it to your account and then **clone your fork** locally.

> Example: You fork the `kubernetes/website` repo to suggest a documentation fix.

---

## **6. Git Fork in Action (Example)**

```bash
# Step 1: Fork the repo on GitHub
# Step 2: Clone your fork
git clone https://github.com/myusername/sample-repo.git

# Step 3: Create a new branch and make changes
git checkout -b feature/fix-readme
git commit -am "Fixed typo in README"

# Step 4: Push and create Pull Request
git push origin feature/fix-readme
```

---

## **Assignment 1**
✅ Create a fork of any project → make a small change → open a **Pull Request**.

---

## **7. Git Fetch vs Git Pull**

### 🔹 Git Fetch
Downloads the latest changes from the remote but doesn’t merge them automatically.

### 🔹 Git Pull
Does both fetch + merge automatically.

```bash
git fetch origin main
git pull origin main
```

---

## **8. Git Fetch vs Pull in Real-time**

Example:
- Teammate updates the `main` branch.
- You run `git fetch` → updates your remote tracking branch only.
- You run `git pull` → fetches and merges into your local branch.

---

## **9. Which Command Do You Use Mostly — Git Fetch or Git Pull?**

> I use **`git fetch`** more frequently to review incoming changes before merging.  
> This avoids unwanted conflicts or overwriting my local work.

---

## **Assignment 2**
✅ Practice `git fetch` and `git pull` using a sample GitHub repository.

---

## **10. Git Rebase vs Git Merge (Detailed)**

| Feature | Git Merge | Git Rebase |
|----------|------------|------------|
| History  | Creates a merge commit | Rewrites commit history |
| Use Case | Preserves branch history | Keeps linear commit history |
| Safe for public branches? | ✅ Yes | ⚠️ No (avoid rebasing public branches) |

---

## **11. Git Rebase vs Git Merge (Practical Example)**

```bash
# Merge
git checkout main
git merge feature/login

# Rebase
git checkout feature/login
git rebase main
```

- **Merge**: Adds a merge commit.
- **Rebase**: Moves commits to the top of main’s latest commit.

---

## **12. Git Merge vs Rebase (Interview Short Answer)**

> “Merge combines histories preserving branches, while Rebase rewrites history to make it linear and cleaner.”

---

## **Assignment 3**
✅ Try merging and rebasing branches in a test repository.

---

## **13. Git Branching Strategy Used in Company**

> We followed the **GitFlow** strategy:
> - `main` → Production-ready code  
> - `develop` → Integration branch  
> - `feature/*` → New features  
> - `hotfix/*` → Urgent production fixes  
> - `release/*` → Pre-production testing

This structure helped parallel feature development and stable releases.

---

## **14. 3 Challenges Faced with Git During Work**

1. **Merge Conflicts** due to overlapping work on same files.  
2. **Large File Commits** mistakenly added (e.g., `.zip` files).  
3. **Rewriting History** (via rebase) causing branch desync for teammates.

---

## **15. Recent Git Challenge and Resolution**

> A teammate accidentally force-pushed over the `develop` branch.  
> I used:
```bash
git reflog
git reset --hard HEAD@{3}
git push --force
```
to restore the correct commit safely.

---

## **16. How to Handle Merge Conflicts in Git**

1. Identify conflicting files after merge.
2. Open files → fix manually.
3. Mark resolved:
```bash
git add <file>
git commit
```
4. Verify changes before pushing.

---

## **17. Git Merge Strategies — Ours vs Theirs**

| Strategy | Meaning |
|-----------|----------|
| **Ours** | Keep your current branch’s changes, ignore theirs. |
| **Theirs** | Keep incoming branch’s changes, ignore yours. |

```bash
git merge -X ours branch-name
git merge -X theirs branch-name
```

---

## **Assignment 4**
✅ Create a merge conflict intentionally → resolve it using `ours` or `theirs` strategy.

---

## **18. Have You Ever Used Git Tags? Why?**

Yes.  
> Tags are used to **mark specific commits** as release versions (e.g., `v1.0`, `v2.1`).

```bash
git tag -a v1.0 -m "Release 1.0"
git push origin v1.0
```

---

## **19. Combine Multiple Commits into One Commit**

Use **interactive rebase**:

```bash
git rebase -i HEAD~3
# Mark older commits as 'squash'
git push -f
```

This keeps history clean and concise.

---

## **20. 10 Git Commands Used Daily**

1. `git status`  
2. `git add .`  
3. `git commit -m "message"`  
4. `git pull`  
5. `git push`  
6. `git checkout -b branch`  
7. `git merge`  
8. `git log --oneline`  
9. `git diff`  
10. `git stash`

---

## **21. Ignore Pushing Changes to a File**

Add it to `.gitignore` or use update-index:

```bash
echo "config.json" >> .gitignore
git rm --cached config.json
```

If you just want to stop tracking but keep locally:
```bash
git update-index --assume-unchanged config.json
```

---

## **22. Purpose of .git Folder**

`.git/` contains all internal data like commits, branches, refs, logs — it’s the **heart of a Git repository**.

---

## **23. Can You Restore a Deleted .git Folder?**

Not fully.  
If deleted, Git history is lost unless:
- You have a backup.
- Or can re-clone the repo from remote.

---

## **24. Teammate Accidentally Committed a Kubernetes Secret**

### ⚠️ Scenario
A teammate pushed a Kubernetes Secret (base64 encoded) file to Git.

### ✅ Steps to Fix

1. **Remove file**
   ```bash
   git rm secret.yaml
   git commit -m "Remove secret"
   git push
   ```

2. **Permanently clean Git history**
   ```bash
   git filter-repo --path secret.yaml --invert-paths
   git push --force --all
   ```

3. **Rotate secret**
   ```bash
   kubectl delete secret db-credentials
   kubectl create secret generic db-credentials \
     --from-literal=username=newadmin \
     --from-literal=password=newpassword
   ```

4. **Prevent future leaks**
   - Add `*.secret.yaml` in `.gitignore`
   - Enable secret scanning (e.g., `git-secrets`, `Gitleaks`)

### 💬 Interview Short Answer
> “Once a teammate committed a Kubernetes secret, I removed it, scrubbed it from history using `git filter-repo`, rotated the secret, and added secret scanning policies to prevent future exposure.”

---

📘 **End of Document**
