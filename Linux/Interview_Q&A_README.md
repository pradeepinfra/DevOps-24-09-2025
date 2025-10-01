
# Linux & DevOps Commands, Scripts, and Troubleshooting Guide

This document contains Linux commands, troubleshooting steps, and scripts for daily DevOps and system administration tasks. All original questions are kept as provided.

---

## 1. linux commands that you use on day to day

1. `ls -a -l -ltr`  
2. `cd`  
3. `cat`, `less`, `tail`  
4. `grep`  
5. `top`, `htop`, `ps`  
6. `df -h` (or `du -sh`)  
7. `systemctl`  
8. `chmod | chown`  
9. `scp | rsynk`  
10. `find`  

---

## 2. Can you restore lost pem file ? If not how can you access the instance ?

No, you cannot restore a lost PEM file — it’s not stored on AWS or recoverable.  
However, you can regain access by using a workaround: create a new key pair, attach it to the instance via a temporary EC2 rescue process, and restore SSH access.

---

## 3. /Var is almost 90 percent full, What will be your next steps ?

✅ **Step 1: Inspect Disk Usage Under /var**  
```bash
sudo du -sh /var/* | sort -hr | head -10
```

✅ **Step 2: Clean Log Files**  
```bash
sudo journalctl --vacuum-size=200M
sudo rm -rf /var/log/*.gz /var/log/*.[0-9]
sudo truncate -s 0 /var/log/syslog
```

✅ **Step 3: Clear Package Cache**  
```bash
sudo apt clean         # Debian/Ubuntu
sudo yum clean all     # RHEL/CentOS
```

✅ **Step 4: Check Docker Artifacts**  
```bash
docker system df
docker system prune -a
```

✅ **Step 5: Consider Moving or Archiving Data**  
- Archive old logs to /home or S3  
- Use logrotate to compress and limit logs:  
```bash
sudo nano /etc/logrotate.conf
```

✅ **Step 6: Set Up Alerts and Monitoring**  
- Install `ncdu`, `duf`, or setup Prometheus/Grafana alerts for disk usage thresholds.  
- Automate cleanup with cron or systemd timers if appropriate.  

🧠 **Why /var Fills Up:**  
- Verbose logging (failed cron jobs, app debug logs)  
- Docker images/layers  
- Orphaned cache files  
- Email spools or crash dumps  

---

## 4. Linux Server is slow due to High CPU utilization. How will you fix it ?

✅ **Answer:**  
Identify processes consuming high CPU using `top`, `htop`, or `pidstat`. Analyze if it’s misbehaving applications, runaway processes, or scheduled jobs, then take corrective action.

✅ **Step 1: Check Load Average**  
```bash
uptime
```
- Load average higher than CPU cores indicates overutilization.

✅ **Step 2: Identify CPU-Heavy Processes**  
```bash
top -o %CPU
htop
```

✅ **Step 3: Drill Down**  
```bash
ps -eo pid,ppid,cmd,%cpu,%mem --sort=-%cpu | head
pidstat -u 1 5
```

✅ **Step 4: Investigate the Cause**  
- Specific app? Cron job? Misconfigured service? Known bug?  

✅ **Step 5: Take Corrective Action**  
- Kill or restart runaway process: `kill -9 <pid>`  
- Restart service: `systemctl restart <service>`  
- Scale application, limit resources, tune app performance.

✅ **Step 6: Check Logs**  
```bash
journalctl -xe
tail -f /var/log/syslog
```

✅ **Step 7: Implement Preventive Measures**  
- Set CPU/memory limits in containers  
- Use Prometheus + Grafana for monitoring and alerts  
- Refactor long-running tasks

---

## 5. Application deployed on Nginx returns Connection Refused, How will you fix it ?

📝 **Short Explanation:**  
“Connection Refused” usually means NGINX or the backend service is not reachable.

✅ **Steps:**  
1. Reproduce error: `curl -I http://localhost`  
2. Check if NGINX is running: `sudo systemctl status nginx`  
3. Ensure NGINX listens on correct port: `ss -tuln | grep :80`  
4. Test NGINX config: `sudo nginx -t`  
5. Verify application backend: `curl http://localhost:5000`  
6. Check firewall/security groups  
7. Check SELinux/AppArmor restrictions

---

## 6. SSH to an instance stopped working ? How will you troubleshoot the issue ?

✅ **Answer:**  
Check if issue is networking, instance, or credentials.

✅ **Steps:**  
1. Confirm error: `ssh -i my-key.pem ec2-user@<IP>`  
2. Check instance health & reachability  
3. Verify Security Groups & NACLs  
4. Validate PEM file & username  
5. Use EC2 Instance Connect if PEM lost  
6. Rescue mode if needed: detach root volume, fix `authorized_keys`, reattach

---

## 7. Find and list the log files older than 7 days in /var/log folder.

✅ **Command:**  
```bash
find /var/log -type f -mtime +7
```

✅ **With size info:**  
```bash
find /var/log -type f -mtime +7 -exec ls -lh {} \;
```

✅ **To delete:**  
```bash
sudo find /var/log -type f -mtime +7 -delete
```

---

## 8. Find and remove the log files older than 30 days in a folder.

✅ **Command:**  
```bash
sudo find /path/to/folder -type f -name "*.log" -mtime +30 -exec rm -f {} \;
```

✅ **Dry run before delete:**  
```bash
find /path/to/folder -type f -name "*.log" -mtime +30 -exec ls -lh {} \;
```

---

## 9. Cronjob + Shell script to perform advanced log rotation (Scenario Provided)

**File:** `log_cleanup.sh`  
```bash
#!/bin/bash
LOG_DIR="/var/log/myapp"
LOG_FILE="/var/log/myapp/log_rotation.log"

[ ! -d "$LOG_DIR" ] && echo "[$(date)] ERROR: Log dir missing!" >> "$LOG_FILE" && exit 1

find "$LOG_DIR" -type f -name "*.log" -mtime +7 -mtime -30 ! -name "*.gz" -exec gzip {} \; -exec echo "[$(date)] Compressed: {}" >> "$LOG_FILE" \;

find "$LOG_DIR" -type f -name "*.gz" -mtime +30 -exec rm -f {} \; -exec echo "[$(date)] Deleted: {}" >> "$LOG_FILE" \;

find "$LOG_DIR" -type f -name "*.log" -mtime +30 -exec rm -f {} \; -exec echo "[$(date)] Deleted (uncompressed): {}" >> "$LOG_FILE" \;

echo "[$(date)] Log rotation completed." >> "$LOG_FILE"
```

**Run via cron daily:**  
```cron
0 0 * * * /path/to/log_cleanup.sh
```

---

## 10. You’ve received a CSV file with a list of usernames and passwords to create users on a Linux system.

**CSV format:**  
```csv
username,password
alice,Password@123
bob,Secure@456
carol,DevOps@789
```

**Script:** `create_users.sh`  
```bash
#!/bin/bash
INPUT="users.csv"
[[ ! -f "$INPUT" ]] && echo "CSV missing!" && exit 1

tail -n +2 "$INPUT" | while IFS=',' read -r username password; do
  id "$username" &>/dev/null && echo "User $username exists. Skipping." && continue
  useradd "$username"
  echo "${username}:${password}" | chpasswd
  chage -d 0 "$username"
  echo "User '$username' created."
done
```

**Usage:**  
```bash
chmod +x create_users.sh
sudo ./create_users.sh
```

---

## 11. Service Health monitor script in Bash

**Script:** `multi_service_monitor.sh`  
```bash
#!/bin/bash
services=("nginx" "sshd" "docker")

echo "-----------------------------------"
echo "  Service Health Check Report"
echo "-----------------------------------"

for service in "${services[@]}"; do
  if systemctl is-active --quiet "$service"; then
    echo "$service is ✅ RUNNING"
  else
    echo "$service is ❌ STOPPED"
    systemctl restart "$service" &> /dev/null
    if systemctl is-active --quiet "$service"; then
      echo "$service has been ✅ restarted."
    else
      echo "❌ Failed to restart $service."
    fi
  fi
  echo "-----------------------------------"
done
```

---

## 12. Find and delete files over 100MB

```bash
find /path/to/directory -type f -size +100M -exec rm -f {} \;
```

**Preview files before deletion:**  
```bash
find /path/to/directory -type f -size +100M -exec ls -lh {} \;
```

---

## 13. Get the list of users who logged in today (scenario - some packages deleted)

```bash
last | grep "$(date '+%a %b %e')" | awk '{print $1}' | sort | uniq
```

---

## 14. Website doesn't load, How will you investigate ??

✅ **Steps:**  
1. Check if site is down: `curl -I https://yourdomain.com`, `ping yourdomain.com`  
2. DNS resolution: `dig yourdomain.com`, `nslookup yourdomain.com`  
3. Verify routing: compare `curl -v` with server IP  
4. Network/firewall check: `telnet`, `nc -zv`  
5. Check web server: `sudo systemctl status nginx/apache2`  
6. Inspect application logs  
7. Monitor disk/memory/CPU: `df -h`, `top`, `htop`, `free -m`  
8. Check backend services (DB, cache)  
9. Check SSL certificate: `curl -Iv https://yourdomain.com`  
10. Rollback deployment if necessary  

---

## 15. Using sed command, how to remove first and last line of the file

```bash
sed '1d;$d' filename
```

- `1d` → delete first line  
- `$d` → delete last line  
