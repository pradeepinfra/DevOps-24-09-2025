# 🧭 AWS Network Load Balancer (NLB) — Full Overview & Guide

---

## 🔍 What is NLB (Network Load Balancer)?

**AWS Network Load Balancer (NLB)** is a **Layer 4 (Transport Layer)** load balancer that automatically distributes **TCP, UDP, or TLS traffic** across multiple backend targets such as EC2 instances, containers, or IP addresses.

It is designed for **ultra‑low latency**, **millions of requests per second**, and **high availability** with **static IPs** per Availability Zone.

---

## ⚙️ How NLB Works

When clients send network requests:

1. The **NLB receives the connection** (e.g., TCP:80, TCP:443).
2. It forwards the connection at **Layer 4** to one of the healthy backend targets (instances or IPs).
3. **Health checks** ensure traffic only goes to healthy targets.
4. NLB maintains **persistent connections** and scales automatically to handle millions of concurrent connections.

---

## 🌐 Real‑World Analogy

Imagine a toll booth on a busy highway:

* Cars = client requests
* Toll booth = NLB
* Lanes = backend servers (targets)
* The toll booth directs each car to an open lane and closes lanes under maintenance.

This ensures continuous, efficient flow without traffic jams.

---

## 🚀 Why We Use NLB (Key Benefits)

| Feature                           | Benefit                                                       |
| --------------------------------- | ------------------------------------------------------------- |
| ⚡ **High Performance**            | Handles millions of requests/sec with very low latency        |
| 🧩 **Layer 4 (Transport)**        | Works with TCP, UDP, and TLS protocols                        |
| 🏗️ **Static IPs per AZ**         | You can whitelist fixed IPs for firewall and compliance needs |
| 🩺 **Health Checks**              | Sends traffic only to healthy backend instances               |
| 🌍 **Multi‑AZ High Availability** | Spreads traffic across multiple Availability Zones            |
| 🔒 **TLS Offloading**             | Decrypts encrypted connections for backend simplicity         |
| 🔁 **Cross‑Zone Load Balancing**  | Evenly balances traffic across all targets in all AZs         |
| 📶 **AWS PrivateLink Support**    | Enables private service access between VPCs                   |

---

## 💡 Common Use Cases

| Use Case                    | Example                                       |
| --------------------------- | --------------------------------------------- |
| **TCP/UDP Applications**    | Gaming, streaming, VoIP, IoT                  |
| **Database Proxies**        | Load balance MySQL/PostgreSQL replicas        |
| **Microservices (ECS/EKS)** | Distribute traffic among pods or containers   |
| **Financial Systems**       | Real‑time, low latency workloads              |
| **Hybrid Connectivity**     | On‑premises systems connected securely to AWS |

---

## ⚖️ When to Choose NLB (vs Other Load Balancers)

| Load Balancer     | OSI Layer | Best For                        | Example                 |
| ----------------- | --------- | ------------------------------- | ----------------------- |
| **NLB**           | Layer 4   | High‑speed TCP/UDP/TLS traffic  | Gaming, IoT, streaming  |
| **ALB**           | Layer 7   | HTTP/HTTPS, routing logic, APIs | Web apps, microservices |
| **CLB (Classic)** | Layer 4/7 | Legacy systems                  | Older EC2‑based apps    |

---

## 🧩 Example Architecture

```
Internet
   ↓
AWS Network Load Balancer (TCP:80)
   ↓
Target Group (TCP:80)
   ↓
EC2 Web Servers (Ubuntu)
   ↓
Database (Optional)
```

**Process:**

1. Users access the NLB DNS name (e.g., `my-nlb-1234.elb.us-west-2.amazonaws.com`).
2. NLB receives traffic and forwards it to healthy EC2 targets.
3. Users get responses from available servers, achieving load balancing and high availability.

---

## ✅ Summary

| Point           | Description                                                               |
| --------------- | ------------------------------------------------------------------------- |
| **Definition**  | NLB is a high‑performance, Layer 4 load balancer for TCP/UDP/TLS traffic  |
| **Purpose**     | Distributes traffic evenly across healthy servers for high availability   |
| **Why Use It**  | To improve performance, scalability, fault tolerance, and availability    |
| **Key Benefit** | Handles millions of network connections per second with ultra‑low latency |


**NLB = The best choice when you need speed, scalability, and reliability for network‑level traffic.**


# AWS Network Load Balancer (NLB) — Step‑by‑Step (Manual Console Guide, Oregon Region - Ubuntu)

**Purpose:**  
This guide helps you create an **Internet‑facing AWS Network Load Balancer (NLB)** end‑to‑end using the **AWS Management Console**, in the **Oregon (us-west-2)** region, with **Ubuntu EC2 instances**.

---

## 🌐 Region
**Region:** us-west-2 (Oregon)  
**Availability Zones:** us-west-2a, us-west-2b

---

## ⚙️ Overview
You will create:
```
Internet → NLB (TCP:80) → Target Group → Ubuntu EC2 Instances → VPC (2 AZs)
```

---

## 1️⃣ Create a VPC
1. Navigate to **VPC → Your VPCs → Create VPC**
2. Choose **VPC only**
3. Name: `NLB-VPC`
4. CIDR block: `10.0.0.0/16`
5. Click **Create VPC**

---

## 2️⃣ Create Two Public Subnets
1. Go to **VPC → Subnets → Create subnet**
2. Choose your VPC
3. Subnet 1:
   - Name: `Public-Subnet-A`
   - AZ: `us-west-2a`
   - CIDR: `10.0.1.0/24`
4. Subnet 2:
   - Name: `Public-Subnet-B`
   - AZ: `us-west-2b`
   - CIDR: `10.0.2.0/24`

---

## 3️⃣ Create and Attach Internet Gateway
1. **VPC → Internet Gateways → Create internet gateway**
   - Name: `NLB-IGW`
2. **Attach to VPC → NLB-VPC**

---

## 4️⃣ Create Route Table
1. **VPC → Route Tables → Create route table**
   - Name: `Public-RT`
   - VPC: `NLB-VPC`
2. Add route: `0.0.0.0/0 → Internet Gateway`
3. Associate `Public-Subnet-A` and `Public-Subnet-B`

---

## 5️⃣ Create Security Group
1. **EC2 → Security Groups → Create security group**
   - Name: `nlb-ec2-sg`
   - VPC: `NLB-VPC`
2. Inbound Rules:
   - TCP 22 (SSH) → Your IP
   - TCP 80 (HTTP) → 0.0.0.0/0

---

## 6️⃣ Launch EC2 Instances (Ubuntu)
1. **EC2 → Launch Instance**
   - AMI: `Ubuntu 22.04 LTS (us-west-2)`
   - Type: `t3.micro`
   - Subnet: `Public-Subnet-A` (first instance), `Public-Subnet-B` (second instance)
   - Auto-assign Public IP: Enabled
   - Security Group: `nlb-ec2-sg`
2. **User Data (simple web server):**
```bash
#!/bin/bash
apt update -y
apt install -y apache2
systemctl enable apache2
systemctl start apache2
echo "Hello from $(hostname -f)" > /var/www/html/index.html
```
3. Launch 2 instances: `nlb-web-1` and `nlb-web-2`.

---

## 7️⃣ Create Target Group
1. **EC2 → Target Groups → Create target group**
   - Type: **Instances**
   - Protocol: **TCP**
   - Port: **80**
   - VPC: **NLB-VPC**
   - Health Check Protocol: **TCP**
2. Register both EC2 instances as targets.

---

## 8️⃣ Create Network Load Balancer (NLB)
1. **EC2 → Load Balancers → Create Load Balancer → Network Load Balancer**
2. Configuration:
   - Name: `My-NLB`
   - Scheme: **Internet-facing**
   - IP type: **IPv4**
3. Listener:
   - Protocol: **TCP**
   - Port: **80**
4. Availability Zones:
   - AZs: `us-west-2a`, `us-west-2b`
   - Subnets: `Public-Subnet-A`, `Public-Subnet-B`
5. Attach the **Target Group** created earlier.
6. Click **Create Load Balancer**.

---

## 9️⃣ Test the Setup
1. Copy the **NLB DNS Name** from the console (e.g., `my-nlb-123456.elb.us-west-2.amazonaws.com`)
2. Run from local terminal or CloudShell:
```bash
curl http://<NLB-DNS>
```
You should see responses like:
```
Hello from ip-10-0-1-XX.us-west-2.compute.internal
Hello from ip-10-0-2-YY.us-west-2.compute.internal
```

✅ **Load balancing verified!**

---

## 🔍 10️⃣ Monitor
- **Target Health:** EC2 → Target Groups → Targets
- **Metrics:** CloudWatch → NLB metrics → ActiveFlowCount, NewFlowCount
- **Logs:** Enable VPC Flow Logs for network analysis

---

## 🧹 11️⃣ Cleanup
1. Delete Load Balancer
2. Delete Target Group
3. Terminate EC2 instances
4. Delete Route Table, IGW, and Subnets
5. Delete VPC

---

## ✅ Summary
- Region: **Oregon (us-west-2)**
- OS: **Ubuntu 22.04**
- NLB Type: **Internet-Facing**
- Protocol: **TCP:80**
- Verified: ✅ Works across AZs with failover and health checks
