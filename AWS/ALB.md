# 🧭 AWS Application Load Balancer (ALB) — Project Guide

---

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
Set up an AWS **Application Load Balancer (ALB)** to distribute web (HTTP/HTTPS) traffic across two Ubuntu EC2 instances and verify that it works.

---

## 1️⃣ Create a VPC

**Purpose:** Your private AWS network for resources.

**Steps:**
- Go to **VPC → Your VPCs → Create VPC**
- Name: `ALB-VPC`
- CIDR: `10.0.0.0/16`

✅ **Verify:** VPC shows as *Available*.

---

## 2️⃣ Create Public Subnets

**Purpose:** Public access for EC2 and ALB.

**Steps:**
- **Subnet 1:** `Public-Subnet-A` — AZ: `us-west-2a`, CIDR: `10.0.1.0/24`
- **Subnet 2:** `Public-Subnet-B` — AZ: `us-west-2b`, CIDR: `10.0.2.0/24`

✅ **Verify:** Both subnets appear under `ALB-VPC`.

---

## 3️⃣ Create & Attach Internet Gateway

**Purpose:** Connect your VPC to the Internet.

**Steps:**
- Create IGW → Name: `ALB-IGW`
- Attach to `ALB-VPC`

✅ **Verify:** IGW status shows *Attached*.

---

## 4️⃣ Create Route Table

**Purpose:** Allow outbound internet traffic.

**Steps:**
- Create route table → Name: `Public-RT`
- Add route: `0.0.0.0/0 → Internet Gateway`
- Associate both public subnets.

✅ **Verify:** Subnets show route to `igw-xxxx`.

---

## 5️⃣ Create Security Groups

**ALB Security Group (`alb-sg`):**
- Inbound:
  - TCP 80 (HTTP) → 0.0.0.0/0
  - TCP 443 (HTTPS) → 0.0.0.0/0
- Outbound: Allow all

**EC2 Security Group (`web-sg`):**
- Inbound:
  - TCP 80 (HTTP) → `alb-sg`
  - TCP 22 (SSH) → Your IP
- Outbound: Allow all

✅ **Verify:** SGs created and applied correctly.

---

## 6️⃣ Launch EC2 Instances (Ubuntu)

**Purpose:** Backend servers for ALB.

**Steps:**
- AMI: `Ubuntu 22.04 LTS`
- Type: `t3.micro`
- Subnets:
  - Instance 1 → `Public-Subnet-A`
  - Instance 2 → `Public-Subnet-B`
- Security Group: `web-sg`
- User Data:
```bash
#!/bin/bash
apt update -y
apt install -y apache2
systemctl enable apache2
systemctl start apache2
echo "Hello from $(hostname -f)" > /var/www/html/index.html
echo "OK" > /var/www/html/health
```

✅ **Test:**
```bash
curl http://<EC2_Public_IP>
```
Expected output:
```
Hello from ip-10-0-1-XX.us-west-2.compute.internal
```

---

## 7️⃣ Create Target Group

**Purpose:** ALB forwards traffic to instances via Target Group.

**Steps:**
- Go to **EC2 → Target Groups → Create target group**
  - Target type: `Instances`
  - Protocol: `HTTP`
  - Port: `80`
  - Health Check: `HTTP /health`
  - VPC: `ALB-VPC`
- Register both EC2 instances.

✅ **Verify:** Target health = *Healthy*.

---

## 8️⃣ Create Application Load Balancer

**Steps:**
- **EC2 → Load Balancers → Create → Application Load Balancer**
- Name: `My-ALB`
- Scheme: `Internet-facing`
- Listeners: `HTTP:80`, (optional `HTTPS:443`)
- Subnets: `Public-Subnet-A`, `Public-Subnet-B`
- Security Group: `alb-sg`
- Attach the previously created Target Group.

✅ **Verify:** Status = *Active*.

---

## 9️⃣ Test Load Balancing

Copy the ALB DNS name:
```
my-alb-123456.elb.us-west-2.amazonaws.com
```

Run:
```bash
curl http://<ALB-DNS>
```
You should see alternating responses:
```
Hello from ip-10-0-1-XX.us-west-2.compute.internal
Hello from ip-10-0-2-YY.us-west-2.compute.internal
```

✅ **Load balancing confirmed!**

---

## 🔍 10️⃣ Monitoring

- **Target Health:** EC2 → Target Groups → Targets  
- **Metrics:** CloudWatch → ALB Metrics (`RequestCount`, `TargetResponseTime`)  
- **Logs:** Enable ALB Access Logs to S3 (optional)

---

## 🧹 11️⃣ Cleanup

Delete resources to avoid charges:
1. Load Balancer  
2. Target Group  
3. EC2 Instances  
4. Route Table, IGW, Subnets  
5. VPC

---

## 💡 Why and When to Use an ALB

**Why use ALB:**
- Handles **HTTP/HTTPS traffic (Layer 7)** intelligently.
- Supports **path-based** and **host-based routing**.
- Integrates with **ACM for TLS/SSL** certificates.
- Works with **AWS WAF**, **Cognito**, and **OIDC** for authentication.
- Supports **WebSockets**, **HTTP/2**, and **gRPC**.
- Provides detailed **access logs and metrics** for monitoring.

**When to use ALB:**
- You have multiple web applications or microservices.
- You need routing based on path (e.g., `/api`, `/app`) or host.
- You want TLS termination with managed certificates.
- You need Layer 7 features like redirects, rewrites, or header inspection.

**When NOT to use ALB:**
- For TCP/UDP workloads or raw network traffic → Use **NLB**.
- For deploying inline security appliances → Use **Gateway Load Balancer (GLB)**.

---

## 🏁 Summary

| Component | Description |
|------------|-------------|
| **Region** | Oregon (us-west-2) |
| **OS** | Ubuntu 22.04 |
| **Load Balancer Type** | Application Load Balancer |
| **Protocol** | HTTP / HTTPS |
| **Test** | Successful alternate responses |
| **Result** | Verified load balancing across AZs |

---

✅ **Conclusion:**  
Your **AWS Application Load Balancer (ALB)** efficiently distributes web traffic, supports HTTPS, and provides intelligent routing with built-in high availability, observability, and integration options for modern applications.
