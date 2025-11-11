# 🐧 Linux File Permissions — Complete Guide

This guide explains **everything about Linux file permissions** — what they mean, how to change them, and how to read their numeric and symbolic forms.

---

## 📘 1. What Are File Permissions?

In Linux, **permissions** determine **who can read, write, or execute** a file or directory.

Each file and directory has **three types of access levels**:

| User Type | Description |
|------------|-------------|
| **Owner (u)** | The person who created the file. |
| **Group (g)** | Users who belong to the same group as the owner. |
| **Others (o)** | Everyone else. |

---

## 🧩 2. Types of Permissions

| Permission | Symbol | Description | Example on File | Example on Directory |
|-------------|---------|--------------|------------------|----------------------|
| **Read** | `r` | View or read the contents. | Open or view file. | List contents of directory (`ls`). |
| **Write** | `w` | Modify contents. | Edit or delete the file. | Create or delete files inside the directory. |
| **Execute** | `x` | Run file as a program/script. | Run the script. | Enter (`cd`) into the directory. |

---

## 🔢 3. Numeric (Octal) Representation

Each permission has a **number value**:

| Permission | Numeric Value |
|-------------|----------------|
| Read (r) | 4 |
| Write (w) | 2 |
| Execute (x) | 1 |
| No permission (-) | 0 |

You **add them up** to get a total for each user type:

Example:
```
rwx = 4 + 2 + 1 = 7  
rw- = 4 + 2 + 0 = 6  
r-- = 4 + 0 + 0 = 4
```

So permission `rw-r--r--` = `644`

---

## 🧮 4. Understanding Permission Structure

Example:
```
-rwxr-xr--
```

Breakdown:

| Position | User Type | Permissions | Meaning |
|-----------|------------|--------------|----------|
| 1 | File Type | `-` means file, `d` means directory | File |
| 2–4 | Owner | `rwx` | Read, write, execute |
| 5–7 | Group | `r-x` | Read, execute |
| 8–10 | Others | `r--` | Read only |

**In numeric form:**  
`rwxr-xr--` → `755`

---

## 💻 5. Changing Permissions with `chmod`

`chmod` = **change mode**

### ✴️ Syntax:
```
chmod [permissions] [filename]
```

### 🔸 Numeric Example:
```
chmod 755 script.sh
```
➡ Owner: `rwx`, Group: `r-x`, Others: `r-x`

### 🔹 Symbolic Example:
```
chmod u+x myfile.sh     # Add execute permission for user
chmod g-w myfile.sh     # Remove write permission for group
chmod o=r myfile.sh     # Set others to read-only
chmod a+x myfile.sh     # Give execute permission to all (user, group, others)
```

---

## 🧍 6. Changing Ownership

Each file has:
- **Owner**
- **Group**

### Commands:
```
chown user file.txt          # Change owner
chown user:group file.txt    # Change both owner and group
chgrp group file.txt         # Change group only
```

Example:
```
chown ubuntu:developers app.py
```

---

## 🧱 7. File vs Directory Permissions

| Type | Read (r) | Write (w) | Execute (x) |
|------|-----------|------------|-------------|
| **File** | View contents | Modify contents | Run the file |
| **Directory** | List files | Create/Delete files | Enter directory |

Example:
```
drwxr-x---  myfolder/
```
- `d` → Directory  
- Owner: full access  
- Group: read & execute  
- Others: no access  

---

## 🧰 8. Common Permission Settings

| Mode | Meaning | Typical Use |
|------|----------|--------------|
| `600` | Owner can read/write | Private config files |
| `644` | Owner can read/write, others read | Common for text files |
| `700` | Only owner can read/write/execute | Private scripts |
| `755` | Everyone can read/execute, only owner can write | Common for programs/scripts |
| `777` | Everyone can read/write/execute | ⚠️ **Not secure**, avoid using unless necessary |

---

## 🔍 9. View File Permissions

To check file permissions:
```
ls -l
```

Example output:
```
-rw-r--r--  1 ubuntu ubuntu  1200 Nov 11 10:00  notes.txt
```

Breakdown:
| Field | Description |
|--------|--------------|
| `-rw-r--r--` | Permissions |
| `ubuntu` | Owner |
| `ubuntu` | Group |
| `1200` | File size |
| `notes.txt` | File name |

---

## 🧠 10. Shortcut Reference Table

| Symbol | Numeric | Meaning |
|---------|----------|----------|
| `rwx` | 7 | Read + Write + Execute |
| `rw-` | 6 | Read + Write |
| `r-x` | 5 | Read + Execute |
| `r--` | 4 | Read only |
| `-wx` | 3 | Write + Execute |
| `-w-` | 2 | Write only |
| `--x` | 1 | Execute only |
| `---` | 0 | No permissions |

---

## 🧩 11. Example Scenarios

### Example 1:
You have a script `deploy.sh` and want everyone to run it but not edit it:
```
chmod 755 deploy.sh
```

### Example 2:
You have a config file `secrets.env` that only you should access:
```
chmod 600 secrets.env
```

### Example 3:
Give group write permission:
```
chmod g+w project.txt
```

---

## ✅ 12. Quick Summary

| Command | Purpose |
|----------|----------|
| `chmod` | Change permissions |
| `chown` | Change file owner |
| `chgrp` | Change file group |
| `ls -l` | List files with permissions |
| `umask` | Default permission mask |

---

### 🧭 Example Practice

Create a sample directory and test:
```bash
mkdir test-perms
cd test-perms
touch file1 file2
chmod 644 file1
chmod 700 file2
ls -l
```

Expected output:
```
-rw-r--r--  file1
-rwx------  file2
```

---

## 🎯 Conclusion

Linux file permissions are **core to system security and management**.  
Understanding them helps you:
- Control who can access files.
- Protect sensitive data.
- Manage user access safely.

> 🛡️ Tip: Never use `777` unless absolutely required — it gives full control to everyone.

---

**Author:** Pradeep  
**Topic:** Linux Permissions Simplified  
**Updated:** November 2025

