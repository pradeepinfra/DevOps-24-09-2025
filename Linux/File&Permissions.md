# 🐧 Linux File Permissions — Complete Beginner to Advanced Guide

This guide explains **everything about Linux file permissions** — what they mean, how to change them, and how to use numeric or symbolic modes.

---

## 🧩 1. What Are File Permissions?

In Linux, **permissions** decide **who can read, write, or execute** a file or directory.

| User Type | Description |
|------------|-------------|
| **Owner (u)** | The user who created the file |
| **Group (g)** | Users in the same group as the owner |
| **Others (o)** | Everyone else |

---

## 🧠 2. Types of Permissions

| Permission | Symbol | Meaning | File Example | Directory Example |
|-------------|---------|----------|----------------|------------------|
| Read | `r` | View contents | Open a file | List files |
| Write | `w` | Modify contents | Edit or delete | Create/Delete inside |
| Execute | `x` | Run the file | Run program | Enter (`cd`) |

---

## 🔢 3. Numeric (Octal) Representation

| Permission | Number |
|-------------|---------|
| Read (r) | 4 |
| Write (w) | 2 |
| Execute (x) | 1 |

You add them up for each user type.

Examples:
```
rwx = 7
rw- = 6
r-- = 4
```

`rw-r--r--` = 644  
`rwxr-xr-x` = 755

---

## 🧱 4. Reading Permissions

Example output from `ls -l`:
```
-rwxr-xr-- 1 ubuntu ubuntu 1200 Nov 12 notes.txt
```

| Part | Meaning |
|------|----------|
| `-` | File type (`-` = file, `d` = directory) |
| `rwx` | Owner permissions |
| `r-x` | Group permissions |
| `r--` | Others permissions |

So: `rwxr-xr--` = **755**

---

## 💻 5. Changing Permissions — `chmod`

### 🔸 Numeric Example:
```
chmod 755 script.sh
```
➡ Owner: `rwx`, Group: `r-x`, Others: `r-x`

### 🔹 Symbolic Example:
```
chmod u+x file.sh     # Add execute for owner
chmod g-w file.sh     # Remove write for group
chmod o=r file.sh     # Others read only
chmod a+x file.sh     # Everyone execute
```

---

## 👑 6. Changing Ownership — `chown` / `chgrp`

```
chown user file.txt          # Change owner
chown user:group file.txt    # Change both owner & group
chgrp group file.txt         # Change only group
```

Example:
```
chown ubuntu:developers app.py
```

---

## 📂 7. File vs Directory Permissions

| Type | Read | Write | Execute |
|------|------|--------|----------|
| File | Open/View | Modify | Run |
| Directory | List files | Add/Delete files | Enter (`cd`) |

Example:
```
drwxr-x--- myfolder/
```

---

## 🧮 8. Common Permission Modes

| Mode | Symbol | Meaning | Example Use |
|------|---------|----------|--------------|
| 600 | `rw-------` | Only owner read/write | Config files |
| 644 | `rw-r--r--` | Owner write, others read | Text files |
| 700 | `rwx------` | Only owner access | Private scripts |
| 755 | `rwxr-xr-x` | Everyone execute, owner write | Common scripts |
| 777 | `rwxrwxrwx` | Everyone full access | ⚠️ Not secure |

---

## 🧪 9. Practical Example

```bash
mkdir test-perms
cd test-perms
touch file1 file2
chmod 644 file1
chmod 700 file2
ls -l
```

Output:
```
-rw-r--r-- file1
-rwx------ file2
```

---

## 🧭 10. Commands Reference

| Command | Purpose |
|----------|----------|
| `ls -l` | Show permissions |
| `chmod` | Change permissions |
| `chown` | Change file owner |
| `chgrp` | Change group |
| `umask` | Default permission mask |

---

## ⚠️ 11. Avoid Using `777`

`chmod 777 file.txt` means **everyone** can read, write, execute — unsafe.  
Use only for temporary testing.

---

## ✅ 12. Summary

| Symbol | Number | Meaning |
|---------|----------|----------|
| `rwx` | 7 | Read, Write, Execute |
| `rw-` | 6 | Read, Write |
| `r-x` | 5 | Read, Execute |
| `r--` | 4 | Read only |
| `---` | 0 | No permissions |

---

### 🎯 Final Tip

> Always keep scripts as **755** and text/config files as **644**.  
> Avoid **777** unless absolutely required.

**Author:** Pradeep  
**Updated:** November 2025  
