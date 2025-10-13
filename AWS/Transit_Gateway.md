# 🛜 AWS Transit Gateway – Simple Analogy Explanation

## 🧠 What is AWS Transit Gateway?

**AWS Transit Gateway (TGW)** is a **central hub** that connects multiple **Amazon VPCs**, **on-premises networks**, and **VPN connections**, allowing them to communicate efficiently and securely.

---

## 🚏 Analogy: The Central Bus Station

Imagine each **VPC** in AWS is like a **city** 🏙️  

- To connect **Hyderabad** and **Vijayawada**, you build a **direct road** — this is like **VPC Peering**.  
- But when you have **10 or more cities (VPCs)**, connecting every city directly to every other city means creating too many roads.  
  - This becomes **complex, costly, and difficult to manage**.

So instead of building many roads, you create **one Central Bus Station** 🚌  

Now:
- Every city connects **only once** — to the Bus Station.  
- Any city can reach any other city **through that Bus Station**.

That **Bus Station** is your **Transit Gateway** in AWS.

---

## 🔧 AWS Concept Mapping

| Analogy Term         | AWS Term                  | Description |
|----------------------|---------------------------|--------------|
| City                 | VPC                       | Individual network or environment |
| Direct Road          | VPC Peering               | One-to-one connection between two VPCs |
| Central Bus Station  | Transit Gateway (TGW)     | Central hub for communication |
| Road from City to Station | TGW Attachment        | Connection between a VPC and the TGW |
| Travel Routes        | TGW Routes / Route Tables | Controls how traffic moves between VPCs |

---

## ✅ Benefits of Transit Gateway

1. **Simplified connectivity** — One-to-many instead of many-to-many connections.  
2. **Centralized routing control** — Easy management from a single point.  
3. **Better scalability** — Supports thousands of VPCs and connections.  
4. **Cost and performance efficiency** — Reduces redundant peering links and routing complexity.  

---

## 💬 Quick Summary

> **Transit Gateway = Central Bus Station of AWS Networking.**  
>  
> Instead of building direct roads between every VPC (which gets messy),  
> all VPCs connect to one hub — the **Transit Gateway** —  
> and communicate through it efficiently and securely.

---

## 📘 Example Architecture

```
   [VPC-A]──┐
             │
   [VPC-B]───┼──▶ [Transit Gateway] ◀───[On-Prem VPN]
             │
   [VPC-C]───┘
```

All VPCs connect through the **Transit Gateway**, which routes traffic between them without requiring individual VPC peering connections.

---

## 🧩 Real-World Use Case

- A company with multiple environments:
  - `Prod-VPC`
  - `Dev-VPC`
  - `Test-VPC`
  - `Shared-Services-VPC`
  - `On-Premises VPN`

All connect to one **Transit Gateway**, allowing smooth communication between environments without complex peering setups.

---

### 🔍 Summary Table

| Without TGW | With TGW |
|--------------|-----------|
| Many VPC Peering connections | Single centralized hub |
| Hard to scale | Easy to scale |
| Complex routing | Simple and controlled routing |
| Hard to manage | Centralized management |

---

🧭 **In short:**  
> Transit Gateway keeps your AWS network **organized, scalable, and easy to manage**, just like a central bus station keeps city traffic well-connected.



# AWS Transit Gateway 3-VPC Setup (Manual Project)

## 🧭 Overview

This project demonstrates how to connect **three VPCs** using an **AWS Transit Gateway**. Each VPC will host an EC2 instance, and we’ll verify network connectivity between them.

### Architecture

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

## ⚙️ Step-by-Step Manual Setup

### Step 1: Create 3 VPCs

Go to **VPC Console → Your VPCs → Create VPC**

| VPC Name | CIDR Block  |
| -------- | ----------- |
| VPC-1    | 10.0.0.0/16 |
| VPC-2    | 11.0.0.0/16 |
| VPC-3    | 12.0.0.0/16 |

---

### Step 2: Create Subnets

Create one public subnet in each VPC (same Availability Zone).

| VPC   | Subnet Name        | CIDR Block  | AZ         |
| ----- | ------------------ | ----------- | ---------- |
| VPC-1 | VPC1-Public-Subnet | 10.0.1.0/24 | us-west-2a |
| VPC-2 | VPC2-Public-Subnet | 11.0.1.0/24 | us-west-2a |
| VPC-3 | VPC3-Public-Subnet | 12.0.1.0/24 | us-west-2a |

✅ Enable **Auto-assign Public IPv4** for all.

---

### Step 3: Create and Attach Internet Gateways

Go to **VPC → Internet Gateways → Create Internet Gateway**

| IGW Name | Attach to VPC |
| -------- | ------------- |
| IGW-VPC1 | VPC-1         |
| IGW-VPC2 | VPC-2         |
| IGW-VPC3 | VPC-3         |

---

### Step 4: Update Route Tables

Each VPC’s main route table → **Edit Routes** → Add:

* Destination: `0.0.0.0/0`
* Target: Internet Gateway (e.g. IGW-VPC1)

Associate the subnet with that route table.

---

### Step 5: Launch EC2 Instances

Launch **3 EC2 instances**, one per VPC.

| Instance | VPC   | Subnet             | Security Group   |
| -------- | ----- | ------------------ | ---------------- |
| EC2-1    | VPC-1 | VPC1-Public-Subnet | Allow SSH + ICMP |
| EC2-2    | VPC-2 | VPC2-Public-Subnet | Allow SSH + ICMP |
| EC2-3    | VPC-3 | VPC3-Public-Subnet | Allow SSH + ICMP |

**Security Group Rules:**

* Inbound: SSH (22) from My IP, ICMP (All)
* Outbound: All traffic allowed

---

### Step 6: Create Transit Gateway

Go to **VPC → Transit Gateways → Create Transit Gateway**

| Setting                         | Value    |
| ------------------------------- | -------- |
| Name                            | TGW-Main |
| Amazon ASN                      | 64512    |
| DNS Support                     | Enabled  |
| Default Route Table Association | Enabled  |
| Default Route Table Propagation | Enabled  |

---

### Step 7: Create Transit Gateway Attachments

Create **3 attachments** linking the TGW with each VPC.

| Attachment Name | VPC   | Subnet             |
| --------------- | ----- | ------------------ |
| TGW-VPC1-Attach | VPC-1 | VPC1-Public-Subnet |
| TGW-VPC2-Attach | VPC-2 | VPC2-Public-Subnet |
| TGW-VPC3-Attach | VPC-3 | VPC3-Public-Subnet |

---

### Step 8: Update Route Tables (for TGW Routing)

**VPC-1 Route Table:**

```
11.0.0.0/16 → TGW-Main
12.0.0.0/16 → TGW-Main
```

**VPC-2 Route Table:**

```
10.0.0.0/16 → TGW-Main
12.0.0.0/16 → TGW-Main
```

**VPC-3 Route Table:**

```
10.0.0.0/16 → TGW-Main
11.0.0.0/16 → TGW-Main
```

---

### Step 9: Test Connectivity

1. SSH into **EC2-1**
2. Ping EC2-2 and EC2-3 private IPs

✅ If ping works → Transit Gateway connectivity is successful.

---

### Step 10: Clean Up

To avoid charges:

* Terminate EC2 instances
* Delete TGW attachments
* Delete Transit Gateway
* Delete IGWs and VPCs

---

## 🧰 Summary

| Component       | Count | Description           |
| --------------- | ----- | --------------------- |
| VPCs            | 3     | Each with unique CIDR |
| Subnets         | 3     | Public subnets        |
| IGWs            | 3     | Internet Gateways     |
| EC2 Instances   | 3     | Test servers          |
| Transit Gateway | 1     | Connects all 3 VPCs   |
| TGW Attachments | 3     | One per VPC           |

---

## ✅ Verification Checklist

* [x] VPCs created and routed correctly
* [x] EC2 instances launched and reachable
* [x] Transit Gateway created and attached
* [x] Routes updated
* [x] Ping between VPCs successful

---

**Author:** Infravyom IT Technologies 
**Purpose:** Transit Gateway Connectivity Lab

