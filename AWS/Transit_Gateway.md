# 🛜 AWS Transit Gateway (TGW) — 2025 Project Guide

## 🚀 Overview

**AWS Transit Gateway (TGW)** acts as a **central hub** that connects multiple **VPCs**, **VPNs**, and **on-premises networks** — enabling efficient, secure communication through a single connection.

Instead of building complex **VPC peering meshes**, TGW makes your network **simpler, more scalable, and easier to manage**.

---

## 🧠 Simple Analogy — *The Central Bus Station 🚌*

Think of each **VPC** as a **city** 🏙️.

- To connect two cities, you build a **road** → that’s **VPC Peering**.  
- But when you have 10+ cities, creating roads between all of them becomes **complex** and **expensive**.  

So, you build **one Central Bus Station** 🚌 — every city connects to it once, and all cities can communicate via the station.

That **bus station** = **AWS Transit Gateway**.

---

## 🧩 AWS Concept Mapping

| Real World | AWS Concept | Description |
|-------------|--------------|--------------|
| City | VPC | Individual AWS network |
| Road between cities | VPC Peering | One-to-one link between VPCs |
| Central Bus Station | Transit Gateway (TGW) | Central communication hub |
| Road to station | TGW Attachment | Connection from VPC to TGW |
| Bus Routes | TGW Route Tables | Controls how traffic moves between VPCs |

---

## ✅ Why Use Transit Gateway (2025 Benefits)

| Benefit | Description |
|----------|--------------|
| 🌐 **Centralized Connectivity** | Connect and manage all VPCs via one hub |
| ⚙️ **Simplified Routing** | One-to-many routing, no peering chaos |
| 📈 **Highly Scalable** | Supports thousands of VPCs |
| 💰 **Cost Efficient** | Reduces redundant connections |
| 🔒 **Secure & Controlled** | Centralized network flow management |

---

## 🧭 Project Objective

Create **3 VPCs** and connect them through **one Transit Gateway (TGW)**.  
Then test **inter-VPC communication** using **EC2 instances**.

---

## 🏗️ Architecture Diagram

```
                +-----------------------------+
                |        Transit Gateway      |
                +-------------+---------------+
                              |
     +-----------+------------+-----------+
     |            |            |           |
+----+----+  +----+----+  +----+----+  
|  VPC-1  |  |  VPC-2  |  |  VPC-3  |  
|10.0.0.0 |  |11.0.0.0 |  |12.0.0.0 |
+----+----+  +----+----+  +----+----+
|EC2-1   |  |EC2-2   |  |EC2-3   |
|10.0.1.10| |11.0.1.10| |12.0.1.10|
+---------+  +---------+  +---------+
```

---

## ⚙️ Step-by-Step Setup (AWS Console)

### Step 1️⃣ — Create 3 VPCs

| VPC | CIDR |
|------|------|
| VPC-1 | 10.0.0.0/16 |
| VPC-2 | 11.0.0.0/16 |
| VPC-3 | 12.0.0.0/16 |

---

### Step 2️⃣ — Create 1 Public Subnet per VPC

| VPC | Subnet Name | CIDR | AZ |
|------|--------------|--------|------|
| VPC-1 | VPC1-Public | 10.0.1.0/24 | us-west-2a |
| VPC-2 | VPC2-Public | 11.0.1.0/24 | us-west-2a |
| VPC-3 | VPC3-Public | 12.0.1.0/24 | us-west-2a |

✅ Enable **Auto-assign Public IP** for each subnet.

---

### Step 3️⃣ — Create Internet Gateways

| IGW | Attach To |
|------|------------|
| IGW-VPC1 | VPC-1 |
| IGW-VPC2 | VPC-2 |
| IGW-VPC3 | VPC-3 |

---

### Step 4️⃣ — Update Route Tables

For each VPC route table, add:

```
Destination: 0.0.0.0/0
Target: Internet Gateway (of respective VPC)
```

Associate each **public subnet** with this route table.  
✅ Allows EC2 instances to access the internet.

---

### Step 5️⃣ — Launch EC2 Instances

| Instance | VPC | Subnet | Security Group |
|-----------|------|----------|----------------|
| EC2-1 | VPC-1 | VPC1-Public | SSH (22), ICMP (All) |
| EC2-2 | VPC-2 | VPC2-Public | SSH (22), ICMP (All) |
| EC2-3 | VPC-3 | VPC3-Public | SSH (22), ICMP (All) |

---

### Step 6️⃣ — Create Transit Gateway (TGW)

| Setting | Value |
|----------|--------|
| Name | TGW-Main |
| Amazon ASN | 64512 |
| DNS Support | Enabled |
| Default Route Table Association | Enabled |
| Default Route Table Propagation | Enabled |

---

### Step 7️⃣ — Create TGW Attachments

| Attachment | VPC | Subnet |
|--------------|------|----------|
| TGW-VPC1 | VPC-1 | VPC1-Public |
| TGW-VPC2 | VPC-2 | VPC2-Public |
| TGW-VPC3 | VPC-3 | VPC3-Public |

---

### Step 8️⃣ — Update TGW Routing Tables

**VPC-1 Routes**
```
11.0.0.0/16 → TGW-Main
12.0.0.0/16 → TGW-Main
```

**VPC-2 Routes**
```
10.0.0.0/16 → TGW-Main
12.0.0.0/16 → TGW-Main
```

**VPC-3 Routes**
```
10.0.0.0/16 → TGW-Main
11.0.0.0/16 → TGW-Main
```

---

### Step 9️⃣ — Test Connectivity

1. SSH into **EC2-1**  
2. Run:
   ```bash
   ping 11.0.1.10
   ping 12.0.1.10
   ```
✅ If ping works — Transit Gateway setup is successful!

---

### Step 🔟 — Clean Up

To avoid charges:
- Terminate EC2 instances  
- Delete TGW attachments and TGW  
- Delete IGWs and VPCs  

---

## 📋 Project Summary

| Resource | Count | Description |
|-----------|--------|--------------|
| VPCs | 3 | 10.0.0.0/16, 11.0.0.0/16, 12.0.0.0/16 |
| Subnets | 3 | Public subnets |
| IGWs | 3 | Internet gateways |
| EC2 Instances | 3 | Test servers |
| TGW | 1 | Central hub |
| TGW Attachments | 3 | One per VPC |

---

## ✅ Verification Checklist

- [x] VPCs created  
- [x] Subnets and IGWs configured  
- [x] EC2s deployed  
- [x] TGW created and attached  
- [x] Routing configured  
- [x] Ping success between VPCs  

---

## 🧩 Real-World Use Case (2025)

| Environment | Description |
|--------------|--------------|
| **Prod VPC** | Core application servers |
| **Dev VPC** | Developer environment |
| **Shared Services VPC** | Monitoring, logging, and utilities |
| **On-Prem VPN** | Corporate datacenter network |

All connected via **AWS Transit Gateway** — ensuring a **centralized, secure, and scalable** architecture.

---

## 📘 Summary

> 🚌 **Transit Gateway = The Bus Station of AWS Networking.**  
> Instead of managing multiple VPC peerings, connect all your networks once to TGW —  
> and let AWS handle the routing automatically.

---

### 🧾 Author

**Infravyom IT Technologies**  
👨‍💻 *By:* Pradeep  
📅 *Edition:* 2025  
🎯 *Purpose:* AWS Transit Gateway Connectivity Lab  
