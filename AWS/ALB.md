# 🧭 AWS Application Load Balancer (ALB) — Project Guide

## 🧩 Architecture Overview

```
Client (Browser)
   ↓
Internet
   ↓
AWS Application Load Balancer (HTTP/HTTPS)
   ↓
Target Group (HTTP:80)
   ↓
EC2 Web Servers (Ubuntu)
```

**Goal:**  
Set up an AWS **Application Load Balancer (ALB)** to distribute HTTP/HTTPS traffic across two Ubuntu EC2 instances and verify functionality.

---

## 1️⃣ Create a VPC
- Go to **VPC → Create VPC**
- Name: `ALB-VPC`
- CIDR: `10.0.0.0/16`
- Ensure VPC status is **Available**

---

## 2️⃣ Create Public Subnets
- `Public-Subnet-A` → us-west-2a → `10.0.1.0/24`
- `Public-Subnet-B` → us-west-2b → `10.0.2.0/24`

---

## 3️⃣ Create & Attach Internet Gateway
- Create IGW → `ALB-IGW`
- Attach to `ALB-VPC`

---

## 4️⃣ Create Route Table
- Create route table → `Public-RT`
- Add route `0.0.0.0/0 → IGW`
- Associate both public subnets

---

## 5️⃣ Create Security Groups

### **ALB Security Group (`alb-sg`)**
Inbound:
- TCP **80** → `0.0.0.0/0`
- TCP **443** → `0.0.0.0/0`  
Outbound:
- Allow all

### **EC2 Security Group (`web-sg`)**
Inbound:
- TCP **80** → Source: **alb-sg** (only ALB can access servers)
- TCP **22** → Source: **Your IP** (allows secure SSH)
Outbound:
- Allow all

**Simple Flow:**
```
Internet → ALB (80/443 open to all)
ALB → EC2 (only ALB can send traffic on port 80)
You → EC2 (SSH only from your IP)
```

---

## 6️⃣ Launch EC2 Instances (Ubuntu)

AMI: `Ubuntu 22.04`  
Type: `t3.micro`  
Subnets: A & B  
Security Group: `web-sg`

### User Data:
```bash
#!/bin/bash
apt update -y
apt install -y apache2
systemctl enable apache2
systemctl start apache2
echo "Hello from $(hostname -f)" > /var/www/html/index.html
echo "OK" > /var/www/html/health
```

Test using:
```
curl http://<EC2_Public_IP>
```

---

## 7️⃣ Create Target Group
- Type: Instances  
- Protocol: HTTP  
- Port: 80  
- Health check: `/health`  
- Register both EC2 instances  
- Ensure target status = **Healthy**

---

## 8️⃣ Create Application Load Balancer
- **Create ALB → Application Load Balancer**
- Name: `My-ALB`
- Scheme: Internet-facing
- Listeners: `HTTP:80`
- Subnets: A & B
- Security Group: `alb-sg`
- Forward to Target Group

---

## 9️⃣ Test Load Balancing

```
curl http://<ALB-DNS>
```

Expected alternating responses:
```
Hello from ip-10-0-1-XX...
Hello from ip-10-0-2-YY...
```

---

## 🔍 10️⃣ Monitoring
- Target Health (EC2 → Target Groups)
- ALB Metrics (CloudWatch)
- Optional: Enable ALB Access Logs → S3

---

## 🧹 11️⃣ Cleanup
Delete in order:
1. Load Balancer  
2. Target Group  
3. EC2 Instances  
4. Subnets, Route Tables, IGW  
5. VPC  

---

## 💡 Why Use ALB?
- Layer 7 intelligent routing  
- Path/host-based routing  
- SSL/TLS with ACM  
- Supports HTTP/2, WebSockets, gRPC  
- Integrates with WAF, Cognito, OIDC  

---

## ❌ When NOT to Use ALB
- TCP/UDP workloads → Use **NLB**
- Security appliance deployments → **GWLB**

---

## 🏁 Summary

| Component | Description |
|----------|-------------|
| Region | us-west-2 |
| OS | Ubuntu 22.04 |
| Load Balancer | ALB |
| Protocol | HTTP/HTTPS |
| Result | Load balancing verified |

---

## ✅ Conclusion
Your **AWS ALB setup** is complete with high availability, intelligent routing, health checks, monitoring, and secure traffic flow using properly configured security groups.
