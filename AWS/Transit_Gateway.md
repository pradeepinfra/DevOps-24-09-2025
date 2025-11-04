# 🛜 AWS Transit Gateway (TGW) — 2025 Project Guide

---

## 🚀 Overview

**AWS Transit Gateway (TGW)** acts as a **central hub** that connects multiple **VPCs**, **VPNs**, or **on-premises networks** — allowing all of them to communicate efficiently and securely through a single connection.

It eliminates complex **VPC peering meshes** and makes network design **simpler, scalable, and easy to manage**.

---

## 🧠 Simple Analogy — *The Central Bus Station 🚌*

Imagine each **VPC** is like a **city** 🏙️.

- To connect two cities (VPCs), you build a **road** → that’s **VPC Peering**.  
- But when you have 10+ cities, building roads between every city becomes **complex and costly**.  

So, instead, you create **one Central Bus Station** — every city connects to it once, and all cities communicate through that hub.  

That **bus station** = **AWS Transit Gateway**.

---

## 🧩 AWS Concept Mapping

| Real World Term | AWS Concept | Description |
|------------------|--------------|--------------|
| City | VPC | Individual AWS network |
| Road between cities | VPC Peering | One-to-one VPC link |
| Central Bus Station | Transit Gateway (TGW) | Central connection hub |
| Road from city to station | TGW Attachment | VPC connection to TGW |
| Bus routes | TGW Route Tables | Defines traffic flow between VPCs |

---

## ✅ Why Use Transit Gateway (2025 Benefits)

| Benefit | Description |
|----------|--------------|
| 🌐 **Centralized Connectivity** | Manage all VPCs from one hub |
| ⚙️ **Simplified Routing** | One-to-many routing instead of many-to-many |
| 📈 **Scalability** | Supports thousands of VPCs |
| 💰 **Cost Efficiency** | Reduces redundant peering and complexity |
| 🔒 **Security** | Central control of network flow |

---

## 🧭 Project Objective

We’ll create **3 VPCs** and connect them through **one Transit Gateway** to verify **inter-VPC communication** using **EC2 instances**.

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

### 🧩 Step 1: Create 3 VPCs

| VPC Name | CIDR Block |
|-----------|-------------|
| VPC-1 | 10.0.0.0/16 |
| VPC-2 | 11.0.0.0/16 |
| VPC-3 | 12.0.0.0/16 |

---

### 🌐 Step 2: Create 1 Subnet per VPC (Public)

| VPC | Subnet Name | CIDR | AZ |
|------|--------------|--------|------|
| VPC-1 | VPC1-Public | 10.0.1.0/24 | us-west-2a |
| VPC-2 | VPC2-Public | 11.0.1.0/24 | us-west-2a |
| VPC-3 | VPC3-Public | 12.0.1.0/24 | us-west-2a |

✅ Enable **Auto-assign Public IPv4**.

---

### 🌍 Step 3: Create and Attach Internet Gateways

| IGW | Attach To |
|------|------------|
| IGW-VPC1 | VPC-1 |
| IGW-VPC2 | VPC-2 |
| IGW-VPC3 | VPC-3 |

---

### 🧭 Step 4: Update Route Tables

For each VPC → Route Table → **Edit Routes**

```
Destination: 0.0.0.0/0
Target: Internet Gateway (IGW of respective VPC)
```

Then associate your **Public Subnet** with this route table.

✅ This ensures instances can connect to the Internet for SSH and ping tests.

---

### 💻 Step 5: Launch EC2 Instances

| Instance | VPC | Subnet | SG Rules |
|-----------|------|----------|-----------|
| EC2-1 | VPC-1 | VPC1-Public | SSH (22), ICMP (All) |
| EC2-2 | VPC-2 | VPC2-Public | SSH (22), ICMP (All) |
| EC2-3 | VPC-3 | VPC3-Public | SSH (22), ICMP (All) |

---

### 🔗 Step 6: Create Transit Gateway

| Setting | Value |
|----------|--------|
| Name | TGW-Main |
| Amazon ASN | 64512 |
| DNS Support | Enabled |
| Default Route Table Association | Enabled |
| Default Route Table Propagation | Enabled |

---

### 🧷 Step 7: Create TGW Attachments

| Attachment | VPC | Subnet |
|--------------|------|----------|
| TGW-VPC1 | VPC-1 | VPC1-Public |
| TGW-VPC2 | VPC-2 | VPC2-Public |
| TGW-VPC3 | VPC-3 | VPC3-Public |

---

### 🗺️ Step 8: Update Route Tables for TGW Routing

**VPC-1**
```
11.0.0.0/16 → TGW-Main
12.0.0.0/16 → TGW-Main
```

**VPC-2**
```
10.0.0.0/16 → TGW-Main
12.0.0.0/16 → TGW-Main
```

**VPC-3**
```
10.0.0.0/16 → TGW-Main
11.0.0.0/16 → TGW-Main
```

---

### 🧪 Step 9: Test Connectivity

1. SSH into **EC2-1**
2. Run:
   ```bash
   ping 11.0.1.10
   ping 12.0.1.10
   ```
✅ If ping works — TGW connectivity is successful!

---

### 🧹 Step 10: Clean Up (to avoid charges)

- Terminate EC2s  
- Delete TGW attachments and TGW  
- Delete IGWs and VPCs  

---

## 📋 Project Summary

| Component | Count | Description |
|-------------|--------|----------------|
| VPCs | 3 | Unique CIDRs |
| Subnets | 3 | Public |
| IGWs | 3 | Internet Gateways |
| EC2 | 3 | Test Instances |
| TGW | 1 | Central Hub |
| TGW Attachments | 3 | One per VPC |

---

## ✅ Verification Checklist

- [x] VPCs created  
- [x] EC2s deployed  
- [x] TGW created and attached  
- [x] Routing updated  
- [x] Ping success between VPCs  

---

## 🧩 Real-World Example (2025 Use Case)

- **Prod VPC** → Core application servers  
- **Dev VPC** → Developer environment  
- **Shared Services VPC** → Monitoring & Logging  
- **On-Prem VPN** → Corporate network  

All connected via **AWS Transit Gateway** → centralized, secure, and scalable.

---

## 📘 Summary

> **Transit Gateway = The Bus Station of AWS Networking.**  
>  
> Instead of creating dozens of VPC peerings, connect everything once to TGW —  
> and let AWS handle all the routing automatically.

---

### 🧾 Author
**Infravyom IT Technologies**  
**By:** Pradeep  
**Purpose:** AWS Transit Gateway Connectivity Lab (2025 Edition)
