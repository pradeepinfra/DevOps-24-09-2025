# 🧭 AWS VPC – Complete Manual Setup (2025 Console Guide with Real-Time Explanation & End-to-End Testing)

This guide explains **how to manually create and configure a full AWS Virtual Private Cloud (VPC)** using the **AWS Console (2025)** — including **real-world examples**, **network flow explanations**, and **complete step-by-step setup with live testing**.

---

## 🌐 1. What is a VPC?

**Amazon VPC (Virtual Private Cloud)** is your **own private, isolated network** within AWS.
You can control how your AWS resources connect with each other and the Internet.

### 🔍 Real-Time Explanation

Think of a **VPC** as your **private data center inside AWS**.
It gives you total control over:

* IP Address ranges
* Subnets
* Routing
* Internet and private access
* Security (via SGs and NACLs)

---

## 🧩 2. VPC Components Explained (with Real-Life Analogies)

| Component                  | What it does                                             | How it works internally                                | Real-life analogy                |
| -------------------------- | -------------------------------------------------------- | ------------------------------------------------------ | -------------------------------- |
| **VPC**                    | Main network boundary                                    | Contains subnets, route tables, gateways, SGs          | 🏡 Neighborhood                  |
| **Subnet**                 | Divides VPC into zones                                   | Allocates smaller IP blocks; linked to one AZ          | 🛣 Street inside neighborhood    |
| **Internet Gateway (IGW)** | Gives VPC Internet access                                | AWS-managed router to the public Internet              | 🚪 Main entrance gate            |
| **NAT Gateway**            | Allows private subnet to access Internet (outbound only) | Translates private IP → public IP for outbound traffic | 📮 Post office sending letters   |
| **Route Table**            | Defines how traffic moves between subnets and gateways   | Matches destination IP with route rules                | 🗺 GPS map                       |
| **Security Group (SG)**    | Instance-level firewall (stateful)                       | Checks traffic at EC2 level                            | 👮 Security guard at your door   |
| **Network ACL (NACL)**     | Subnet-level firewall (stateless)                        | Checks traffic at subnet border                        | 🚧 Gatekeeper at street entrance |
| **Elastic IP (EIP)**       | Static public IP                                         | Can be attached to EC2 or NAT for stability            | 🏷 Permanent home address        |

---

## 📐 3. CIDR and IP Address Planning

| Resource       | CIDR Block  | Description                       |
| -------------- | ----------- | --------------------------------- |
| VPC            | 10.0.0.0/16 | Entire network range (65,536 IPs) |
| Public Subnet  | 10.0.1.0/24 | Internet-facing subnet            |
| Private Subnet | 10.0.2.0/24 | Backend systems, databases        |

### 🧮 How CIDR Works (in real-time)

* `/16` → 65,536 IPs → used for the full VPC.
* `/24` → 256 IPs per subnet → typically one subnet per AZ.

> AWS reserves 5 IPs per subnet (for internal use), so you get 251 usable IPs.

---

## 🛠️ 4. Real-Time Setup – Step-by-Step

### **Step 1: Create VPC**

**Console Path:** `VPC → Your VPCs → Create VPC`

* Name: `lab-vpc`
* CIDR: `10.0.0.0/16`
* Tenancy: Default
* Click **Create VPC**

📘 *This creates your digital neighborhood.*

---

### **Step 2: Create Subnets**

#### Public Subnet

* Name: `lab-public-subnet`
* CIDR: `10.0.1.0/24`
* Enable **Auto-assign IPv4**
* AZ: `ap-south-1a`

#### Private Subnet

* Name: `lab-private-subnet`
* CIDR: `10.0.2.0/24`
* Disable public IP assignment

---

### **Step 3: Internet Gateway (IGW)**

1. Go to **VPC → Internet Gateways → Create IGW**
2. Name: `lab-igw`
3. Attach to VPC: `lab-vpc`

---

### **Step 4: Route Table Setup**

1. Create Route Table → Name: `lab-public-rt`
2. Add route `0.0.0.0/0 → IGW`
3. Associate `lab-public-subnet`

---

### **Step 5: NAT Gateway (for Private Subnet)**

1. Create NAT Gateway:

   * Subnet: `lab-public-subnet`
   * Allocate Elastic IP
   * Name: `lab-nat`
2. Create Route Table: `lab-private-rt`
3. Add route `0.0.0.0/0 → NAT Gateway`
4. Associate `lab-private-subnet`

---

### **Step 6: Security Setup**

#### Public Security Group (`sg-public`)

| Direction | Protocol | Port | Source    | Purpose       |
| --------- | -------- | ---- | --------- | ------------- |
| Inbound   | SSH      | 22   | My IP     | Admin access  |
| Inbound   | HTTP     | 80   | 0.0.0.0/0 | Web access    |
| Outbound  | All      | All  | 0.0.0.0/0 | Allow updates |

#### Private Security Group (`sg-private`)

| Direction | Protocol | Port | Source     | Purpose          |
| --------- | -------- | ---- | ---------- | ---------------- |
| Inbound   | SSH      | 22   | sg-public  | SSH from bastion |
| Inbound   | MySQL    | 3306 | sg-private | DB communication |
| Outbound  | All      | All  | 0.0.0.0/0  | Allow updates    |

---

### **Step 7: Launch EC2 Instances**

1. **Public EC2:**

   * Subnet: `lab-public-subnet`
   * SG: `sg-public`
   * Assign Public IP: ✅
   * Use as Bastion or Web server

2. **Private EC2:**

   * Subnet: `lab-private-subnet`
   * SG: `sg-private`
   * No Public IP
   * Used for App/DB

---

## 🧪 8. End-to-End Testing (Connectivity Verification)

### 🔹 **Step 8.1: Connect to the Public EC2**

```bash
ssh -i my-key.pem ec2-user@<Public-EC2-Public-IP>
```

✅ SSH connection successful.

### 🔹 **Step 8.2: Test Internet Access from Public EC2**

```bash
ping -c 4 google.com
curl -I https://amazon.com
```

✅ Internet access working (IGW verified).

### 🔹 **Step 8.3: Connect Public → Private EC2**

```bash
ssh ec2-user@10.0.2.10
```

✅ Works (SG allows SSH from sg-public).

### 🔹 **Step 8.4: Test Private EC2 Internet Access**

```bash
ping -c 4 google.com
curl -I https://amazon.com
```

✅ Works via NAT Gateway.

### 🔹 **Step 8.5: Verify Private EC2 Isolation**

Direct SSH from local → private IP should fail.
✅ Confirms no public access.

### 🔹 **Step 8.6: Test SG/NACL Rules**

| Test                    | Command              | Expected | Layer                |
| ----------------------- | -------------------- | -------- | -------------------- |
| ping private→public     | `ping 10.0.1.10`     | ✅        | SG inbound on public |
| ping public→private     | `ping 10.0.2.10`     | ✅        | SG rules mutual      |
| direct Internet→private | `nmap <private-ip>`  | ❌        | NACL+SG protection   |
| outbound updates        | `sudo yum update -y` | ✅        | NAT routing          |

### 🔹 **Step 8.7: Traceroute Path**

```bash
traceroute google.com
```

Shows NAT → IGW → Internet path.

---

## 🧭 9. Architecture Verification Summary

| Component        | Verification     | Status |
| ---------------- | ---------------- | ------ |
| VPC              | 10.0.0.0/16      | ✅      |
| Public Subnet    | Internet via IGW | ✅      |
| Private Subnet   | Outbound via NAT | ✅      |
| SG/NACL          | Working          | ✅      |
| EC2 Connectivity | Verified         | ✅      |
| Isolation        | Secure           | ✅      |

✅ End-to-End testing confirms your VPC is **secure, isolated, and functional.**

---

## 🧹 10. Cleanup Resources

1. Terminate EC2 instances
2. Delete NAT Gateway → Release EIP
3. Delete Route Tables
4. Detach & Delete IGW
5. Delete Subnets
6. Delete VPC

---

## 🧠 11. Quick Architecture Recap

```
                +-------------------+
                |   Internet         |
                +---------+---------+
                          |
                     [ IGW - lab-igw ]
                          |
         +----------------+----------------+
         |                                 |
  Public Subnet (10.0.1.0/24)        Private Subnet (10.0.2.0/24)
  EC2: Bastion/Web                   EC2: App/DB
  SG: sg-public                      SG: sg-private
         |                                 |
         +-------------+-------------------+
                       |
                 [ NAT Gateway ]
                       |
                   Internet (Outbound)
```

---

## ✅ Final Validation

| Test Case                           | Expected Result | Status |
| ----------------------------------- | --------------- | ------ |
| Public EC2 → Internet               | Works           | ✅      |
| Private EC2 → Internet              | Works via NAT   | ✅      |
| Local → Public EC2 SSH              | Works           | ✅      |
| Local → Private EC2 SSH             | Blocked         | ✅      |
| Public EC2 → Private EC2 SSH        | Works           | ✅      |
| Inbound from Internet → Private EC2 | Blocked         | ✅      |

---

**✅ Setup Complete: Your AWS VPC is live, secured, and verified end-to-end.**

---

**Author:** Infravyom IT Technologies
**Last Updated:** October 2025
**Version:** 2.1 (Includes End-to-End Testing & Architecture Verification)
