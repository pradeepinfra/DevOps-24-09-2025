# 🧭 AWS VPC – Complete Manual Setup (2025 Console Guide with Real-Time Explanation)

This guide explains **how to manually create and configure a full AWS Virtual Private Cloud (VPC)** using the **AWS Console (2025)** — including **real-world examples**, **network flow explanations**, and **complete step-by-step setup**.

---

## 🌐 1. What is a VPC?

**Amazon VPC (Virtual Private Cloud)** is your **own private, isolated network** within AWS.  
You can control how your AWS resources connect with each other and the Internet.

### 🔍 Real-Time Explanation
Think of a **VPC** as your **private data center inside AWS**.  
It gives you total control over:
- IP Address ranges
- Subnets (network segments)
- Routing
- Internet and private access
- Security (via SGs and NACLs)

# 🧩 AWS Subnets – Explained Simply

A **subnet (sub-network)** in AWS is a **logical subdivision of a VPC (Virtual Private Cloud)**.  
It helps organize and control how your resources communicate — internally or externally.

### 🏗 Example
If AWS were a big city, **your VPC is your personal gated neighborhood**.  
You decide who enters, who leaves, and how data moves inside.

---

## 🧩 2. VPC Components Explained (with Real-Life Analogies)

| Component | What it does | How it works internally | Real-life analogy |
|------------|--------------|--------------------------|-------------------|
| **VPC** | Main network boundary | Contains subnets, route tables, gateways, SGs | 🏡 Neighborhood |
| **Subnet** | Divides VPC into zones | Allocates smaller IP blocks; linked to one AZ | 🛣 Street inside neighborhood |
| **Internet Gateway (IGW)** | Gives VPC Internet access | AWS-managed router to the public Internet | 🚪 Main entrance gate |
| **NAT Gateway** | Allows private subnet to access Internet (outbound only) | Translates private IP → public IP for outbound traffic | 📮 Post office sending letters |
| **Route Table** | Defines how traffic moves between subnets and gateways | Matches destination IP with route rules | 🗺 GPS map |
| **Security Group (SG)** | Instance-level firewall (stateful) | Checks traffic at EC2 level | 👮 Security guard at your door |
| **Network ACL (NACL)** | Subnet-level firewall (stateless) | Checks traffic at subnet border | 🚧 Gatekeeper at street entrance |
| **Elastic IP (EIP)** | Static public IP | Can be attached to EC2 or NAT for stability | 🏷 Permanent home address |

---

## 📐 3. CIDR and IP Address Planning

| Resource | CIDR Block | Description |
|-----------|------------|-------------|
| VPC | 10.0.0.0/16 | Entire network range (65,536 IPs) |
| Public Subnet | 10.0.1.0/24 | Internet-facing subnet |
| Private Subnet | 10.0.2.0/24 | Backend systems, databases |

### 🧮 How CIDR Works (in real-time)
- `/16` → 65,536 IPs → used for the full VPC.
- `/24` → 256 IPs per subnet → typically one subnet per AZ.

> AWS reserves 5 IPs per subnet (for internal use), so you get 251 usable IPs.

---

## 🛠️ 4. Real-Time Setup – Step-by-Step

### **Step 1: Create VPC**
**Console Path:** `VPC → Your VPCs → Create VPC`

- Name: `lab-vpc`
- CIDR: `10.0.0.0/16`
- Tenancy: Default
- Click **Create VPC**

📘 *This creates your digital neighborhood.*

---

### **Step 2: Create Subnets**

#### Public Subnet
- Name: `lab-public-subnet`
- CIDR: `10.0.1.0/24`
- Enable **Auto-assign IPv4**
- AZ: `ap-south-1a`

📘 *This is the "street" open to visitors.*

#### Private Subnet
- Name: `lab-private-subnet`
- CIDR: `10.0.2.0/24`
- Disable public IP assignment

📘 *This is your secure backend street — no direct Internet.*

---

### **Step 3: Internet Gateway (IGW)**

1. Go to **VPC → Internet Gateways → Create IGW**
2. Name: `lab-igw`
3. Attach to VPC: `lab-vpc`

💡 **Behind the scenes:**  
When an EC2 instance in a public subnet sends traffic to `0.0.0.0/0`, the IGW handles it and sends it to the Internet.

📘 *Think of this as the main gate where visitors enter/exit.*

---

### **Step 4: Route Table Setup**

1. Create Route Table → Name: `lab-public-rt`
2. Add route `0.0.0.0/0 → IGW`
3. Associate `lab-public-subnet`

📘 *Public subnet now knows how to go to the Internet.*

---

### **Step 5: NAT Gateway (for Private Subnet)**

1. Create NAT Gateway:
   - Subnet: `lab-public-subnet`
   - Allocate Elastic IP
   - Name: `lab-nat`
2. Create Route Table: `lab-private-rt`
3. Add route `0.0.0.0/0 → NAT Gateway`
4. Associate `lab-private-subnet`

💡 **Behind the scenes:**  
When private instances download OS updates, the NAT Gateway converts their **private IP** → **public IP**, sends traffic to Internet, and maps replies back.

📘 *Like sending mail through the post office – outsiders never see your address.*

---

### **Step 6: Security Setup**

#### Public Security Group (`sg-public`)
| Direction | Protocol | Port | Source | Purpose |
|------------|-----------|------|---------|----------|
| Inbound | SSH | 22 | My IP | Admin access |
| Inbound | HTTP | 80 | 0.0.0.0/0 | Web access |
| Outbound | All | All | 0.0.0.0/0 | Allow updates |

#### Private Security Group (`sg-private`)
| Direction | Protocol | Port | Source | Purpose |
|------------|-----------|------|---------|----------|
| Inbound | SSH | 22 | sg-public | SSH from bastion |
| Inbound | MySQL | 3306 | sg-private | DB communication |
| Outbound | All | All | 0.0.0.0/0 | Allow updates |

🧠 **How SG Works Internally**
- Stateful → if you allow inbound SSH, return traffic is auto-allowed.
- Applied per EC2, not subnet.

📘 *Like a guard who remembers who came in and lets them back out.*

---

### **Step 7: Launch EC2 Instances**

1. **Public EC2:**  
   - Subnet: `lab-public-subnet`  
   - SG: `sg-public`  
   - Assign Public IP: ✅  
   - Use as Bastion or Web server  

2. **Private EC2:**  
   - Subnet: `lab-private-subnet`  
   - SG: `sg-private`  
   - No Public IP  
   - Used for App/DB  

📘 *Private EC2 cannot be accessed directly from the Internet.*

---

### **Step 8: Test Connectivity**

| Scenario | Expected Result |
|-----------|----------------|
| SSH from local → Public EC2 | ✅ Works |
| Public EC2 → Private EC2 | ✅ Works |
| Private EC2 → Internet | ✅ Works (via NAT) |
| Internet → Private EC2 | ❌ Blocked |

📘 *Confirms isolation and controlled access.*

---

### **Step 9: Cleanup Resources**

1. Terminate EC2 instances  
2. Delete NAT Gateway → Release EIP  
3. Delete Route Tables  
4. Detach & Delete IGW  
5. Delete Subnets  
6. Delete VPC  

📘 *Always clean up to avoid billing.*

---

## 🧠 10. Deep Dive: Security Group vs NACL

| Feature | SG | NACL |
|----------|----|------|
| Level | Instance | Subnet |
| Stateful | ✅ Yes | ❌ No |
| Default | Deny inbound, allow outbound | Allow all |
| Logging | Flow Logs | Flow Logs |
| Use Case | Instance firewall | Subnet-wide control |

🧩 **When to use what**
- **SG:** For application-level rules (web, DB, SSH).
- **NACL:** For network boundary protection (block malicious IPs, etc.).

---

## 🧭 11. Real-Time Traffic Flow Example

```
Private EC2 (10.0.2.10)
  ↓
Route Table → NAT Gateway (10.0.1.5)
  ↓
Internet Gateway (Public)
  ↓
Internet (Software update, Git, etc.)
```

Return traffic reverses the same path, with NAT mapping responses automatically.

---

## 💬 12. Quick Interview Notes

| Question | Answer |
|-----------|---------|
| What’s the difference between IGW and NAT? | IGW = inbound/outbound for public subnet; NAT = outbound only for private subnet |
| Can a private EC2 have public IP? | No |
| Why attach IGW to VPC? | Routes won’t work without an attached IGW |
| Why use multiple AZs? | For high availability and fault tolerance |
| Can SG reference another SG? | Yes, e.g., allow SSH from `sg-public` |

---

## 🧾 Summary

✅ Created **VPC**, **subnets**, **route tables**, **IGW**, and **NAT**  
✅ Configured **security** using **SG** and **NACL**  
✅ Launched **public** and **private EC2**  
✅ Verified **network connectivity**  
✅ Cleaned up resources  

---

**Author:** Infravyom IT Technologies  
**Last Updated:** October 2025  
**Version:** 2.0 (Includes Real-Time Component Explanation)
