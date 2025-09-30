# 🐧 Linux Commands – Complete Guide

This README provides a **comprehensive collection of Linux commands** used in **day-to-day operations**, **system administration**, and **DevOps workflows**.  
It includes **basic, advanced, and organization-specific (role-based) commands** into one structured document.  

---

## 📖 Table of Contents
1. [Basic Linux Commands](#-basic-linux-commands)  
2. [Advanced Linux Commands](#-advanced-linux-commands)  
3. [Most Used Commands in Organizations](#-most-used-commands-in-organizations)  
4. [Role-Based Command Breakdown](#-role-based-command-breakdown)  
   - [Developers](#-developer-commands)  
   - [System Administrators](#-system-administrator-commands)  
   - [DevOps Engineers](#-devops-engineer-commands)  

---

## 🔑 Basic Linux Commands
```bash
pwd                  # Print current working directory
ls -lh               # List files with details
ls -a                # Show hidden files
cd /path             # Change directory
mkdir myfolder       # Create folder
rmdir emptydir       # Remove empty directory
rm -rf folder        # Remove folder and contents (dangerous!)
touch file.txt       # Create file
cat file.txt         # Show file content
less file.log        # View large files
cp file1 file2       # Copy file
mv old new           # Move/rename file
find . -name "*.log" # Search files
grep "ERROR" app.log # Search inside files
```

---

## ⚡ Advanced Linux Commands
```bash
awk '{print $1,$3}' file.txt         # Extract columns
sed 's/error/ERROR/g' file.txt       # Replace text
cut -d: -f1 /etc/passwd              # Extract fields
sort file.txt | uniq -c              # Unique line count
xargs rm -f                          # Run commands on output
jobs / fg / bg                       # Manage background jobs
nice -n 10 process.sh                # Set process priority
strace -p 1234                       # Trace system calls
lsof -i :80                          # Show process using port
tcpdump -i eth0 port 80              # Capture network packets
nmap 192.168.1.0/24                  # Scan network
rsync -avh source/ dest/             # Sync files
tar -czvf backup.tar.gz folder/      # Archive/compress
journalctl -u nginx.service          # View service logs
crontab -e                           # Schedule jobs
```

---

## 🏢 Most Used Commands in Organizations
### 📂 File & Directory
```bash
ls -lh              # List files
cd /var/log         # Change directory
cp file /backup/    # Copy
mv report.csv /opt/ # Move/rename
rm -rf old_logs     # Remove
```

### 📜 File Viewing & Editing
```bash
cat /etc/hosts      # View
less /var/log/syslog# Large files
tail -f access.log  # Follow logs
nano config.txt     # Edit
vim app.py          # Edit with vim
```

### 👤 User & Permission
```bash
whoami              # Current user
id                  # UID & GID
chmod 755 script.sh # Permissions
chown user:group f  # Change owner
```

### ⚙️ Process & Service
```bash
ps aux | grep java  # List processes
kill -9 1234        # Kill process
top / htop          # Monitor
systemctl status nginx
systemctl restart docker
```

### 🌐 Networking
```bash
ping google.com     # Connectivity
curl -I api.local   # API test
scp file user@host:/path  # Copy remote
ssh user@server     # Remote login
ss -tulnp           # Open ports
```

### 📊 System Monitoring
```bash
df -h               # Disk usage
du -sh /var/log/*   # Directory size
free -h             # Memory
uptime              # Load
```

### 📦 Package Management
**Debian/Ubuntu**
```bash
sudo apt update && sudo apt upgrade
sudo apt install nginx
```

**RHEL/CentOS**
```bash
sudo yum install httpd
sudo dnf upgrade
```

---

## 🎯 Role-Based Command Breakdown

### 👨‍💻 Developer Commands
```bash
nano config.txt             # Quick edit
vim app.py                  # Edit code
grep "ERROR" app.log        # Search logs
curl -I https://api.local   # Test API endpoint
scp app.zip server:/opt/    # Copy build
ssh user@server             # Connect to server
```

---

### 🛠️ System Administrator Commands
```bash
whoami                      # Current user
id                          # User/group info
chmod 755 script.sh         # File permissions
chown user:group file.txt   # File ownership
ps aux | grep nginx         # Find process
kill -9 1234                # Kill process
top                         # Monitor system
df -h                       # Disk usage
du -sh /var/log/*           # Folder size
free -h                     # Memory usage
uptime                      # Uptime/load
journalctl -u nginx         # Service logs
```

---

### 🚀 DevOps Engineer Commands
```bash
sudo systemctl status nginx     # Service status
sudo systemctl restart docker   # Restart service
sudo systemctl enable mysql     # Enable service on boot

rsync -avh source/ dest/        # Sync files
tar -czvf backup.tar.gz folder/ # Compress
unzip package.zip               # Extract

docker ps                       # Containers
docker logs -f container_id     # Container logs
kubectl get pods -n default     # Kubernetes pods
kubectl logs pod-name           # Pod logs
```

---

## ✅ Summary
- **Developers** → Navigation, file editing, API testing, SSH, SCP.  
- **System Administrators** → User management, permissions, monitoring, troubleshooting.  
- **DevOps Engineers** → Services, Docker/Kubernetes, deployments, automation.  

This all-in-one guide ensures you have **commands for every role and use case** inside an organization.  
