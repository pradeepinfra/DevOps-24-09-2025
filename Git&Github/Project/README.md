# 🚀 Git & GitHub Demo Project

A simple project to learn **Git** and **GitHub** basics.  

---

## 📂 Project Files  
- `index.html` → Simple web page  
- `style.css` → Basic styling  
- `script.js` → JavaScript interaction  

---

# 🔄 GitHub Process (Step by Step)

### 1. Create a GitHub Account
- Go to [https://github.com](https://github.com)  
- Sign up for a free account  
- Set username, email, and password  

---

### 2. Install Git (on PC)
- Download from [git-scm.com](https://git-scm.com/downloads)  
- Install with default settings  
- Verify installation:  
```bash
git --version
```

---

### 3. Configure Git (first time only)
```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

---

### 4. Create a Local Project
```bash
mkdir git-demo
cd git-demo
echo "# GitHub Demo Project" > README.md
```

---

### 5. Initialize Git
```bash
git init
git add .
git commit -m "First commit"
```

---

### 6. Create a Repository on GitHub
1. Log in to GitHub  
2. Click **+ → New repository**  
3. Enter repo name (example: `git-demo`)  
4. Keep it **Public** (for learning)  
5. Don’t add README (we already have one)  
6. Click **Create repository**  

---

### 7. Connect Local Repo to GitHub
Copy the URL from GitHub (HTTPS). Example:  
```bash
git remote add origin https://github.com/username/git-demo.git
git branch -M main
git push -u origin main
```

---

### 8. Clone Repository (other students can do this)
```bash
git clone https://github.com/username/git-demo.git
```

---

### 9. Create a Branch (for new features)
```bash
git checkout -b my-feature
```

---

### 10. Make Changes
Edit files (example: `index.html` or `README.md`).  

---

### 11. Stage & Commit
```bash
git add .
git commit -m "Updated index.html"
```

---

### 12. Push to GitHub
```bash
git push origin my-feature
```

---

### 13. Create Pull Request (PR)
1. Go to GitHub repository  
2. Click **Pull Requests**  
3. Click **New Pull Request**  
4. Compare branch → `main`  
5. Add description → Click **Create Pull Request**  

---

### 14. Merge Pull Request
- Owner reviews the code  
- If okay → **Merge Pull Request**  
- Branch changes now appear in `main`  

---

## ✅ End Result
- Code is stored safely on GitHub  
- Students learn how to collaborate  
- Every change is tracked  
