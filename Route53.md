# 🧭 Infravyom EC2 Web Server Setup Guide

This guide documents the **complete end-to-end setup** for hosting the website  
**`www.infravyom.com`** on an **AWS EC2 Ubuntu instance** using **Apache**,  
with **Let’s Encrypt HTTPS**, **firewall hardening**, and **auto-renewing SSL certificates**.

---

## ⚙️ 1. Infrastructure Overview

| Component | Description |
|------------|-------------|
| **Cloud Provider** | AWS EC2 (Ubuntu 22.04 LTS) |
| **Web Server** | Apache 2.4 |
| **Domain** | infravyom.com |
| **DNS** | A-record → Elastic IP (`44.230.110.148`) |
| **SSL/TLS** | Let’s Encrypt via Certbot |
| **Security** | AWS Security Group, Fail2Ban, ModSecurity |
| **Automation Script** | `setup_infravyom.sh` |

---

## 🌐 2. DNS Configuration

At your DNS provider (Route53 / GoDaddy / Cloudflare):

| Record | Type | Value |
|--------|------|-------|
| `infravyom.com` | A | `44.230.110.148` |
| `www.infravyom.com` | A | `44.230.110.148` |

Verify DNS:
```bash
dig +short infravyom.com
dig +short www.infravyom.com
```
Expected → both return `44.230.110.148`

---

## 🧩 3. Apache Installation & Configuration

### Install Apache
```bash
sudo apt update
sudo apt install -y apache2
sudo systemctl enable --now apache2
```

### Verify Service
```bash
sudo systemctl status apache2
sudo ss -tlnp | grep ':80'
```
Expected → Apache listening on `*:80`

---

## 🏠 4. Set Up Document Root

Your site’s content lives in `/var/www/html`.

```bash
sudo bash -c 'cat > /var/www/html/index.html <<EOF
<!doctype html>
<html>
<head><meta charset="utf-8"><title>Infravyom</title></head>
<body><h1>Welcome to Infravyom IT Technologies</h1></body>
</html>
EOF'
sudo chown -R www-data:www-data /var/www/html
sudo chmod -R 755 /var/www/html
```

---

## 🧱 5. Virtual Host Configuration

Create the primary vhost file:

```bash
sudo tee /etc/apache2/sites-available/infravyom.conf > /dev/null <<'EOF'
<VirtualHost *:80>
    ServerName infravyom.com
    ServerAlias www.infravyom.com
    DocumentRoot /var/www/html
    <Directory /var/www/html>
        AllowOverride All
        Require all granted
    </Directory>
    ErrorLog ${APACHE_LOG_DIR}/infravyom-error.log
    CustomLog ${APACHE_LOG_DIR}/infravyom-access.log combined
</VirtualHost>
EOF
```

Enable and reload Apache:
```bash
sudo a2ensite infravyom.conf
sudo a2dissite 000-default.conf
sudo systemctl reload apache2
sudo apachectl configtest
```

---

## 🔒 6. Enable HTTPS with Let’s Encrypt (Certbot)

Install Certbot:
```bash
sudo apt install -y snapd
sudo snap install core && sudo snap refresh core
sudo snap install --classic certbot
sudo ln -sf /snap/bin/certbot /usr/bin/certbot
```

Generate and configure SSL:
```bash
sudo certbot --apache -d infravyom.com -d www.infravyom.com
```

Certbot automatically:
- Obtains valid certificates  
- Creates `/etc/apache2/sites-enabled/infravyom-le-ssl.conf`  
- Configures redirection HTTP → HTTPS  

Check certificate:
```bash
sudo certbot certificates
```

Verify HTTPS listener:
```bash
sudo ss -tlnp | grep ':443'
sudo apachectl -S
```

---

## 🔁 7. Redirect HTTP → HTTPS and Non-WWW → WWW

Add redirect config:
```bash
sudo tee /etc/apache2/sites-available/infravyom-redirect.conf > /dev/null <<'EOF'
<VirtualHost *:80>
    ServerName infravyom.com
    ServerAlias www.infravyom.com
    Redirect permanent / https://www.infravyom.com/
</VirtualHost>
EOF

sudo a2ensite infravyom-redirect.conf
sudo systemctl reload apache2
```

Check redirection:
```bash
curl -I -L http://infravyom.com
```

Expected:
```
HTTP/1.1 301 Moved Permanently
Location: https://www.infravyom.com/
```

---

## 🧰 8. Security Hardening

### A. Disable Apache banners and directory listing
```bash
sudo tee /etc/apache2/conf-available/security-hardening.conf > /dev/null <<'EOF'
ServerSignature Off
ServerTokens Prod
<Directory /var/www/html>
    Options -Indexes
</Directory>
EOF

sudo a2enconf security-hardening
sudo systemctl reload apache2
```

### B. Enable ModSecurity
```bash
sudo apt install -y libapache2-mod-security2
sudo cp /etc/modsecurity/modsecurity.conf-recommended /etc/modsecurity/modsecurity.conf
sudo sed -i 's/SecRuleEngine DetectionOnly/SecRuleEngine On/' /etc/modsecurity/modsecurity.conf
sudo a2enmod security2
sudo systemctl restart apache2
```

### C. Enable Fail2Ban
```bash
sudo apt install -y fail2ban
sudo tee /etc/fail2ban/jail.d/apache-local.conf > /dev/null <<'EOF'
[apache-noscript]
enabled = true
port = http,https
filter = apache-noscript
logpath = /var/log/apache2/*error.log
maxretry = 2
bantime = 86400
EOF

sudo systemctl enable --now fail2ban
sudo fail2ban-client status apache-noscript
```

---

## 🌍 9. Optional: Enable HSTS (Strict Transport Security)
```bash
sudo a2enmod headers
sudo tee /etc/apache2/conf-available/hsts.conf > /dev/null <<'EOF'
Header always set Strict-Transport-Security "max-age=15768000; includeSubDomains; preload"
EOF
sudo a2enconf hsts
sudo systemctl reload apache2
```

---

## 🔁 10. Auto-Renewal Test
Certbot auto-renews via systemd. Test it:

```bash
sudo certbot renew --dry-run
```

Expected → `Congratulations, all simulated renewals succeeded!`

---

## 🧪 11. Verification Checklist

| Test | Command | Expected |
|------|----------|----------|
| HTTP | `curl -I http://infravyom.com` | 301 redirect → HTTPS |
| HTTPS | `curl -I https://infravyom.com` | `200 OK` |
| Port 80/443 | `sudo ss -tlnp | egrep ':80|:443'` | Apache listening |
| Cert valid | `sudo certbot certificates` | VALID until expiry |
| Logs | `sudo tail -f /var/log/apache2/access.log` | Requests visible |

---

## 🛡️ 12. AWS Security Group Recommendations

| Port | Protocol | Source | Purpose |
|------|-----------|---------|----------|
| 22 | TCP | **Your IP only (x.x.x.x/32)** | SSH |
| 80 | TCP | 0.0.0.0/0 | HTTP |
| 443 | TCP | 0.0.0.0/0 | HTTPS |

**Always remove SSH access from `0.0.0.0/0` after setup.**

---

## 🧾 13. Maintenance

| Task | Command |
|------|----------|
| View Apache errors | `sudo tail -n 50 /var/log/apache2/error.log` |
| Reload Apache | `sudo systemctl reload apache2` |
| Restart Apache | `sudo systemctl restart apache2` |
| View Fail2Ban status | `sudo fail2ban-client status` |
| Renew certs manually | `sudo certbot renew` |

---

## ✅ 14. Final Verification

Visit:
- **https://infravyom.com**
- **https://www.infravyom.com**

Both should show:
> “Welcome to Infravyom IT Technologies”

and load securely with a **valid SSL padlock**.

---

## 🧠 Notes

- Auto-renewal runs twice daily via `systemd` timer:  
  ```bash
  systemctl list-timers | grep certbot
  ```
- You can safely modify `/var/www/html/index.html` for your real site.
- ModSecurity logs attacks in `/var/log/apache2/modsec_audit.log`.
- Fail2Ban bans repeat offenders automatically.

---

### 🏁 Summary

✅ DNS records → Elastic IP (`44.230.110.148`)  
✅ Apache vhosts → `/etc/apache2/sites-available/infravyom.conf`  
✅ HTTPS → Let’s Encrypt (valid until 2026-02-04)  
✅ Security → Fail2Ban + ModSecurity + hardened Apache  
✅ Auto-renewal tested (`certbot renew --dry-run`)  
✅ Fully working over HTTPS 🌐
