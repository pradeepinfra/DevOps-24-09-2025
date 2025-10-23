# 🧭 AWS VPC – Simple Step-by-Step Setup (2025 Guide for Beginners)

This guide helps you **create and test a complete AWS Virtual Private Cloud (VPC)** using the **AWS Console** — with **easy examples, clear steps, and simple testing**.

---

## 🌐 1. What is a VPC?

A **VPC (Virtual Private Cloud)** is your **own private network** inside AWS.  
You decide which resources can talk to the internet and which stay private.

### 🧠 Simple Analogy
Think of a **VPC** like your **own gated community** —  
You decide who can enter, where the houses (servers) are, and how they connect.

---

## 🧩 2. VPC Components (Made Simple)

| Component | Purpose | Analogy |
|------------|----------|----------|
| **VPC** | Main network | 🏡 Neighborhood |
| **Subnet** | Smaller section inside the VPC | 🛣 Street |
| **Internet Gateway (IGW)** | Gives internet access | 🚪 Main gate |
| **NAT Gateway** | Lets private servers reach the internet (outbound only) | 📮 Post office |
| **Route Table** | Controls traffic flow | 🗺 GPS map |
| **Security Group (SG)** | Firewall for EC2 instances | 👮 Security guard |
| **Network ACL (NACL)** | Firewall for subnet | 🚧 Street gate |
| **Elastic IP (EIP)** | Permanent public IP | 🏷 House number |

---

## 📐 3. Network Plan (IP Ranges)

| Resource | CIDR | Description |
|-----------|-------|-------------|
| VPC | 10.0.0.0/16 | Full network |
| Public Subnet | 10.0.1.0/24 | Internet-facing |
| Private Subnet | 10.0.2.0/24 | Internal systems |

🧮 `/16` = 65,536 IPs → for full VPC  
🧮 `/24` = 256 IPs → for each subnet  

> AWS keeps 5 IPs per subnet (for internal use), so you get 251 usable IPs per subnet.

---

## ⚙️ 4. Step-by-Step Setup

### **Step 1: Create VPC**
- Go to **VPC → Your VPCs → Create VPC**
- Name: `lab-vpc`
- CIDR: `10.0.0.0/16`
- Click **Create**

✅ You now have your private AWS network.

---

### **Step 2: Create Subnets**

#### Public Subnet
- Name: `lab-public-subnet`
- CIDR: `10.0.1.0/24`
- AZ: `ap-south-1a`
- Turn **Auto-assign Public IP** ON

#### Private Subnet
- Name: `lab-private-subnet`
- CIDR: `10.0.2.0/24`
- Turn **Auto-assign Public IP** OFF

✅ Subnets divide your network into public and private zones.

---

### **Step 3: Internet Gateway**
- Go to **Internet Gateways → Create**
- Name: `lab-igw`
- Attach to VPC: `lab-vpc`

✅ This is your VPC’s “door” to the internet.

---

### **Step 4: Route Tables**
- Create **lab-public-rt**
- Add route: `0.0.0.0/0 → IGW`
- Associate it with **public subnet**

✅ Now public subnet can reach the internet.

---

### **Step 5: NAT Gateway (for Private Subnet)**
- Create **NAT Gateway**
  - Subnet: `lab-public-subnet`
  - Allocate Elastic IP
- Create **lab-private-rt**
  - Add route: `0.0.0.0/0 → NAT Gateway`
  - Associate with **private subnet**

✅ Private subnet now has **outbound internet** through NAT (for updates, downloads, etc.).

---

### **Step 6: Security Groups**

#### `sg-public`
| Type | Port | Source | Description |
|------|------|---------|-------------|
| SSH | 22 | My IP | Login access |
| HTTP | 80 | 0.0.0.0/0 | Web access |
| Outbound | All | 0.0.0.0/0 | Allow all outgoing |

#### `sg-private`
| Type | Port | Source | Description |
|------|------|---------|-------------|
| SSH | 22 | sg-public | SSH from Bastion |
| MySQL | 3306 | sg-private | DB traffic |
| Outbound | All | 0.0.0.0/0 | Allow all outgoing |

---

### **Step 7: Launch EC2 Instances**

#### Public EC2
- Subnet: `lab-public-subnet`
- SG: `sg-public`
- Public IP: ✅
- Purpose: Bastion / Web server

#### Private EC2
- Subnet: `lab-private-subnet`
- SG: `sg-private`
- No Public IP
- Purpose: App / Database server

---

## 🧪 8. Test Everything (End-to-End)

### 1️⃣ Connect to Public EC2
```bash
ssh -i my-key.pem ec2-user@<Public-IP>
```
✅ Should connect successfully.

---

### 2️⃣ Check Internet from Public EC2
```bash
ping -c 4 google.com
```
✅ Works (Internet Gateway OK)

---

### 3️⃣ Connect to Private EC2 (from Public EC2)
```bash
ssh ec2-user@10.0.2.10
```
✅ Works (SG allows access)

---

### 4️⃣ Test Internet from Private EC2
```bash
ping -c 4 google.com
```
✅ Works via NAT Gateway

---

### 5️⃣ Try to SSH directly from your laptop → private EC2  
❌ Should **fail** — proves isolation is working.

---

## 🧭 9. Quick Verification Table

| Check | Expected | Status |
|--------|-----------|--------|
| Public EC2 → Internet | Works | ✅ |
| Private EC2 → Internet | Works via NAT | ✅ |
| SSH Local → Public EC2 | Works | ✅ |
| SSH Local → Private EC2 | Blocked | ✅ |
| SSH Public → Private | Works | ✅ |
| Internet → Private | Blocked | ✅ |

---

## 🧹 10. Cleanup (Optional)

1. Terminate EC2 instances  
2. Delete NAT Gateway → Release EIP  
3. Delete Route Tables  
4. Detach & Delete IGW  
5. Delete Subnets  
6. Delete VPC  

---

## 🧠 11. Quick Architecture Recap

```
Internet
   |
[ IGW ]
   |
Public Subnet (10.0.1.0/24)
   |--> EC2: Bastion/Web (Public IP)
   |
[ NAT Gateway ]
   |
Private Subnet (10.0.2.0/24)
   |--> EC2: App/DB (No Public IP)
```

✅ **Public EC2** can reach the internet  
✅ **Private EC2** can go out via NAT  
✅ **Private EC2** is not directly reachable from the internet

---

## 🎯 Final Result

You’ve built and tested a **complete AWS VPC** that is:
- Secure 🔒  
- Functional 🌐  
- Beginner-friendly ✅  

---

**Author:** Infravyom IT Technologies  
**Version:** 2.2 (Simplified Beginner Edition)  
**Updated:** October 2025  
