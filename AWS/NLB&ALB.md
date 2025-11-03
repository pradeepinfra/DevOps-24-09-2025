# 🧭 AWS Network Load Balancer (NLB) — Test & Verification Guide

---

## 🧩 Architecture Overview

```
Client (Your PC)
   ↓
Internet
   ↓
AWS Network Load Balancer (TCP:80)
   ↓
Target Group (TCP:80)
   ↓
EC2 Web Servers (Ubuntu)
```

**Goal:**  
Set up an AWS Network Load Balancer (NLB) to distribute TCP traffic across two Ubuntu EC2 instances and verify it works.

---

## 1️⃣ Create a VPC

**Purpose:** Your private AWS network for resources.

**Steps:**
- Go to **VPC → Your VPCs → Create VPC**
- Name: `NLB-VPC`
- CIDR: `10.0.0.0/16`

✅ **Verify:** VPC shows as "available."

---

## 2️⃣ Create Public Subnets

**Purpose:** Public access for EC2 and NLB.

**Steps:**
- **Subnet 1:** `Public-Subnet-A` — AZ: `us-west-2a`, CIDR: `10.0.1.0/24`
- **Subnet 2:** `Public-Subnet-B` — AZ: `us-west-2b`, CIDR: `10.0.2.0/24`

✅ **Verify:** Both subnets appear under `NLB-VPC`.

---

## 3️⃣ Create & Attach Internet Gateway

**Purpose:** Connect your VPC to the Internet.

**Steps:**
- Create IGW → Name: `NLB-IGW`
- Attach to `NLB-VPC`

✅ **Verify:** IGW status shows **attached**.

---

## 4️⃣ Create Route Table

**Purpose:** Allow outbound internet traffic.

**Steps:**
- Create route table → Name: `Public-RT`
- Add route: `0.0.0.0/0 → Internet Gateway`
- Associate both public subnets.

✅ **Verify:** Subnets show default route to `igw-xxxx`.

---

## 5️⃣ Create Security Group

**Purpose:** Control inbound/outbound traffic.

**Steps:**
- Name: `nlb-ec2-sg`
- VPC: `NLB-VPC`
- Inbound Rules:
  - TCP 22 (SSH) → Your IP
  - TCP 80 (HTTP) → 0.0.0.0/0

✅ **Verify:** Security group attached properly.

---

## 6️⃣ Launch EC2 Instances (Ubuntu)

**Purpose:** Backend servers for NLB.

**Steps:**
- AMI: `Ubuntu 22.04 LTS`
- Type: `t3.micro`
- Subnets:
  - Instance 1 → `Public-Subnet-A`
  - Instance 2 → `Public-Subnet-B`
- Security Group: `nlb-ec2-sg`
- User Data:
```bash
#!/bin/bash
apt update -y
apt install -y apache2
systemctl enable apache2
systemctl start apache2
echo "Hello from $(hostname -f)" > /var/www/html/index.html
```

✅ **Test:**  
Use curl from local terminal:
```bash
curl http://<EC2_Public_IP>
```
You should see:  
`Hello from ip-10-0-1-XX.us-west-2.compute.internal`

---

## 7️⃣ Create Target Group

**Purpose:** NLB uses this to forward traffic to instances.

**Steps:**
- **EC2 → Target Groups → Create**
  - Target type: `Instances`
  - Protocol: `TCP`
  - Port: `80`
  - VPC: `NLB-VPC`
  - Health Check: `TCP`
- Register both EC2 instances.

✅ **Verify:** Target health = **Healthy**

---

## 8️⃣ Create Network Load Balancer

**Steps:**
- **EC2 → Load Balancers → Create → Network Load Balancer**
- Name: `My-NLB`
- Scheme: `Internet-facing`
- Protocol: `TCP`
- Port: `80`
- Subnets: `Public-Subnet-A`, `Public-Subnet-B`
- Attach Target Group

✅ **Verify:** Status = **Active**

---

## 9️⃣ Test Load Balancing

Copy NLB DNS:
```
my-nlb-123456.elb.us-west-2.amazonaws.com
```

Run:
```bash
curl http://<NLB-DNS>
```

You should see alternating results:
```
Hello from ip-10-0-1-XX.us-west-2.compute.internal
Hello from ip-10-0-2-YY.us-west-2.compute.internal
```

✅ **Load balancing confirmed!**

---

## 🔍 10️⃣ Monitor

- **Target Health:** EC2 → Target Groups → Targets  
- **Metrics:** CloudWatch → NLB Metrics (`ActiveFlowCount`, `NewFlowCount`)  
- **Logs:** Enable VPC Flow Logs (optional)

---

## 🧹 11️⃣ Cleanup

Delete resources to avoid costs:
1. Load Balancer  
2. Target Group  
3. EC2 Instances  
4. Route Table, IGW, Subnets  
5. VPC

---

## 🏁 Summary

| Component | Description |
|------------|-------------|
| **Region** | Oregon (us-west-2) |
| **OS** | Ubuntu 22.04 |
| **NLB Type** | Internet-Facing |
| **Protocol** | TCP:80 |
| **Test** | Successful alternate responses |
| **Result** | Verified load balancing across AZs |

---

✅ **Conclusion:**  
Your **AWS Network Load Balancer** efficiently distributes TCP traffic across multiple EC2 instances with automatic health checks, high availability, and minimal latency.
