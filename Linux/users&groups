# Linux Users, Groups & Permissions – Super Simple Guide (AWS Ubuntu)

This guide explains **each concept and command step by step in very simple words**.
If you are new to Linux or AWS EC2, this is for you.

---

## 🟢 Why AWS creates `ubuntu` user by default

AWS **does NOT allow direct login as `root`**.

### Why?
- `root` has full power
- One wrong command can destroy the server

### What AWS does instead
- Creates a normal user called **ubuntu**
- Gives admin power using **sudo**
- This is safer and recommended

Login example:
```bash
ssh -i key.pem ubuntu@<EC2-IP>
```

---

## 👤 What is a USER

A **user** is a person account in Linux.

A user can:
- Login to the server
- Run commands
- Own files

Examples:
- `ubuntu`
- `devops`

Check current user:
```bash
whoami
```

---

## 👑 What is root & sudo

- **root** → super admin (dangerous)
- **sudo** → temporary admin permission

Wrong:
```bash
apt update
```

Correct:
```bash
sudo apt update
```

---

## 👥 What is a GROUP

A **group** is a team of users.

Why groups?
- Permissions are given to groups
- Easy management

Examples:
- `sudo`
- `docker`

---

## 👤 Create a User

```bash
sudo adduser devops
```

Creates:
- User `devops`
- Home directory
- Password
- Private group

---

## 👥 Create a Group

```bash
sudo groupadd projectteam
```

---

## ➕ Add User to Group

```bash
sudo usermod -aG projectteam devops
```

Check:
```bash
groups devops
```

---

## 🔑 Give sudo Access

```bash
sudo usermod -aG sudo devops
```

Remove sudo:
```bash
sudo gpasswd -d devops sudo
```

---

## 📁 File Permissions

```
OWNER | GROUP | OTHERS
```

Permissions:
- r → read
- w → write
- x → execute

---

## 🔢 Permission Numbers

| Permission | Number |
|----------|--------|
| read | 4 |
| write | 2 |
| execute | 1 |

Examples:
- 7 → rwx
- 6 → rw-
- 5 → r-x
- 4 → r--
- 0 → ---

---

## 🔐 chmod Examples

```bash
chmod 770 /project
chmod 700 secret.txt
chmod 444 readme.txt
```

---

## 🔄 chown Examples

```bash
sudo chown devops file.txt
sudo chown :projectteam /project
```

---

## ❌ Permission Denied – Why?

- Not owner
- Not in group
- Permission missing
- Forgot sudo

Fix:
```bash
sudo <command>
```

---

## 🧪 Practice Example

```bash
sudo adduser devops
sudo groupadd team
sudo usermod -aG team devops
sudo mkdir /project
sudo chown :team /project
sudo chmod 770 /project
```

---

## 🧠 Golden Rule

```
Users → Groups → Permissions
sudo → admin power
```

---

## ✅ Summary

- AWS creates `ubuntu` for security
- Users are people
- Groups are teams
- Permissions are locks
- sudo is the master key
