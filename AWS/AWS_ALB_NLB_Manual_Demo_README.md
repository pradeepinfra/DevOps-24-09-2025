# 🌐 AWS Load Balancer Demo – ALB & NLB (Manual Setup Guide)

This project demonstrates how to **manually create and test Application Load Balancer (ALB)** and **Network Load Balancer (NLB)** in **AWS Console**, using two EC2 web servers in different Availability Zones.

---

## 🧭 Overview

| Component | Description |
|------------|--------------|
| **VPC** | Custom VPC with 2 public subnets (multi-AZ) |
| **EC2** | 2 web servers running Apache/HTTPD |
| **ALB** | Application Load Balancer (Layer 7 – HTTP) |
| **NLB** | Network Load Balancer (Layer 4 – TCP) |
| **Region** | Oregon (us-west-2) *(You can use any region)* |

---

## ⚙️ Step 1 — Create Network Components

### 1️⃣ Create VPC
- Go to **VPC Console → Create VPC**
- Name: `demo-vpc`
- IPv4 CIDR block: `10.0.0.0/16`
- Click **Create VPC**

### 2️⃣ Create Subnets
- **public-subnet-1** → AZ `us-west-2a` → CIDR `10.0.1.0/24`
- **public-subnet-2** → AZ `us-west-2b` → CIDR `10.0.2.0/24`
- Enable **Auto-assign Public IPv4**

### 3️⃣ Internet Gateway & Routing
- Create **Internet Gateway** → attach to `demo-vpc`
- Create **Route Table** → add route `0.0.0.0/0` → target IGW
- Associate both subnets with this route table

✅ Now your subnets are internet-facing.

---

## 🖥️ Step 2 — Launch EC2 Instances

1. Go to **EC2 → Launch instance**
2. Name: `web-server-1`
3. AMI: Amazon Linux 2
4. Instance type: `t2.micro`
5. Subnet: `public-subnet-1`
6. Enable **Auto-assign public IP**
7. Security group:
   - Allow SSH (22) from your IP
   - Allow HTTP (80) from `0.0.0.0/0`

Repeat same for `web-server-2` in `public-subnet-2`.

---

### 🧩 Install a Web Server
SSH into each instance and run:

```bash
sudo yum install -y httpd
echo "Hello from $(hostname)" | sudo tee /var/www/html/index.html
sudo systemctl start httpd
sudo systemctl enable httpd
```

Test:
```bash
curl http://<instance-public-ip>
```
✅ You should see “Hello from ip-10-0-x-x”.

---

## 🌍 Step 3 — Create Application Load Balancer (ALB)

1. Go to **EC2 Console → Load Balancers → Create Load Balancer → Application Load Balancer**
2. Name: `demo-alb`
3. Scheme: **Internet-facing**
4. IP type: **IPv4**
5. VPC: `demo-vpc`
6. Select both subnets
7. Create a **Security Group**: allow inbound **HTTP (80)** from `0.0.0.0/0`

### 🔗 Create Target Group
1. Target type: `Instance`
2. Name: `tg-alb-demo`
3. Protocol: HTTP
4. Port: 80
5. Health check path: `/`
6. Register both EC2 instances → Create target group

### ⚙️ Finish ALB Creation
- Listener: HTTP : 80 → Forward to `tg-alb-demo`
- Create ALB and wait until **Status: Active**

### 🧪 Test
Get ALB DNS name:
```
demo-alb-123456.us-west-2.elb.amazonaws.com
```

Open in browser or run:
```bash
curl http://demo-alb-123456.us-west-2.elb.amazonaws.com
```
✅ Should alternate between both servers’ messages.

---

## ⚡ Step 4 — Create Network Load Balancer (NLB)

1. Go to **EC2 → Load Balancers → Create Load Balancer → Network Load Balancer**
2. Name: `demo-nlb`
3. Scheme: **Internet-facing**
4. IP type: **IPv4**
5. Select both subnets (optionally attach Elastic IPs for static IPs)

### 🔗 Create Target Group
1. Target type: `Instance`
2. Name: `tg-nlb-demo`
3. Protocol: TCP
4. Port: 80
5. Register both EC2 instances → Create target group

### ⚙️ Finish NLB Creation
- Listener: TCP : 80 → Forward to `tg-nlb-demo`
- Click **Create Load Balancer**

Wait until status = **Active**

### 🧪 Test
Copy NLB DNS name:
```
demo-nlb-123456.us-west-2.elb.amazonaws.com
```

Run:
```bash
curl http://demo-nlb-123456.us-west-2.elb.amazonaws.com
```

✅ Should show same “Hello from …” output from backend instances.

---

## 📊 Step 5 — Verification

| Check | Expected Result |
|--------|------------------|
| ALB Targets | Healthy |
| NLB Targets | Healthy |
| Browser Access | Alternating EC2 responses |
| Curl Test | Successful HTTP 200 |

---

## 🏗️ Architecture Diagram

```
                 🌍 Internet
                     │
     ┌────────────────────────────────┐
     │          Load Balancers        │
     │ ┌───────────────┐  ┌──────────┐│
     │ │ ALB (HTTP 80) │  │ NLB (TCP)││
     │ └──────┬────────┘  └────┬─────┘│
     └─────────┼───────────────┼───────┘
               │               │
        ┌──────┴──────┐ ┌──────┴──────┐
        │ web-server-1│ │ web-server-2│
        │ (AZ-a)       │ │ (AZ-b)     │
        └──────────────┘ └────────────┘
```

---

## 🧠 Notes

| Feature | ALB | NLB |
|----------|-----|-----|
| Layer | 7 (HTTP/HTTPS) | 4 (TCP/UDP) |
| Health Checks | HTTP | TCP/HTTP |
| Security Group | Required | Not used |
| IP Type | Dynamic | Static (EIP supported) |
| Use Case | Web apps, path-based routing | High-performance, static IP needs |

---

## ✅ Cleanup
After testing, to avoid costs:
1. Delete both Load Balancers  
2. Delete Target Groups  
3. Terminate EC2 instances  
4. Delete VPC (if created for demo)

---

## 📚 References
- [AWS ALB Documentation](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html)
- [AWS NLB Documentation](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html)

---

**Author:** Pradeep  
**Last Updated:** October 2025  
**Purpose:** AWS ALB & NLB manual setup demonstration
