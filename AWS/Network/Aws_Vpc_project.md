# AWS VPC — Manual Path (2025 Console)

> **Single Option Only.**  
> Step-by-step **console instructions** with analogy + CIDR plan.  
> No CLI / No Terraform.  
> Security Groups included.  
> NACL is explained separately at the bottom for comparison.  

---

## 🔑 Analogy (Real-World Story)

Think of AWS networking as a **neighborhood**. Each AWS component maps to something familiar:

### 1. VPC (Virtual Private Cloud)
- **What it is:** A logically isolated AWS network.  
- **Analogy:** The **whole neighborhood**, fenced and private.  

### 2. Subnet
- **What it is:** A slice of the VPC’s IP range.  
- **Analogy:** A **street** inside the neighborhood.  

### 3. IGW (Internet Gateway)
- **What it is:** Connects VPC to the Internet.  
- **Analogy:** The **main gate** of the neighborhood.  

### 4. NAT Gateway
- **What it is:** Lets private subnets talk to the Internet, hiding their IPs.  
- **Analogy:** The **post office** sending letters on behalf of houses.  

### 5. Security Group (SG)
- **What it is:** Firewall rules for instances (**stateful**).  
- **Analogy:** The **guard at each house door**.  

### 6. Route Table (RT)
- **What it is:** Defines subnet routing.  
- **Analogy:** The **map of the neighborhood**.  

---

## 📐 CIDR Plan

- VPC: `10.0.0.0/16`  
- Public Subnet: `10.0.1.0/24`  
- Private Subnet: `10.0.2.0/24`  

---

## 🛠️ Step-by-Step Setup (Console Only)

### 1) Create VPC
- **VPC → Your VPCs → Create VPC**  
  - Name: `lab-vpc`  
  - IPv4 CIDR: `10.0.0.0/16` → **Create**  

### 2) Create Subnets
- **Public Subnet**:  
  - Name `lab-public-subnet`, VPC `lab-vpc`, AZ (any), CIDR `10.0.1.0/24` → **Create**  
  - Select → **Actions → Modify auto-assign IP** → Enable auto-assign IPv4  

- **Private Subnet**:  
  - Name `lab-private-subnet`, VPC `lab-vpc`, same AZ, CIDR `10.0.2.0/24` → **Create**  

### 3) Internet Gateway (IGW) + Public Route
- **Create IGW**: Name `lab-igw` → **Attach to VPC** → `lab-vpc`  
- **Create Route Table**: Name `lab-public-rt`, VPC `lab-vpc`  
- In `lab-public-rt` → Routes → Add `0.0.0.0/0` → Target **IGW** → **Save**  
- Subnet associations → Select `lab-public-subnet`  

### 4) NAT Gateway + Private Route
- **NAT Gateway**: Subnet `lab-public-subnet`, Elastic IP → **Allocate new**, Name `lab-nat` → **Create** (wait until Available)  
- **Private Route Table**: Name `lab-private-rt`, VPC `lab-vpc`  
- Routes → Add `0.0.0.0/0` → Target **NAT Gateway (lab-nat)** → **Save**  
- Subnet associations → Select `lab-private-subnet`  

---

## 🔐 Security Groups Setup

### 1) Public Security Group (`sg-public`)

For EC2 instances in the **public subnet** (like bastion or test servers).

**Create**
- Go to **VPC → Security Groups → Create security group**
- Fill:
  - **Name**: `sg-public`
  - **Description**: Public SG for EC2 in Public Subnet
  - **VPC**: Select `lab-vpc`

**Inbound rules**
- **Rule 1**  
  - Type: SSH  
  - Port range: 22  
  - Source: My IP (`x.x.x.x/32`)  

*(Optional if you plan to host a web app in the public subnet)*  
- **Rule 2**  
  - Type: HTTP  
  - Port range: 80  
  - Source: `0.0.0.0/0`  

- **Rule 3**  
  - Type: HTTPS  
  - Port range: 443  
  - Source: `0.0.0.0/0`  

**Outbound rules**
- Leave default (All traffic → `0.0.0.0/0`)

---

### 2) Private Security Group (`sg-private`)

For EC2 instances in the **private subnet** (like your app or database).

**Create**
- Go to **VPC → Security Groups → Create security group**
- Fill:
  - **Name**: `sg-private`
  - **Description**: Private SG for EC2 in Private Subnet
  - **VPC**: Select `lab-vpc`

**Inbound rules**
- **Rule 1**  
  - Type: SSH  
  - Port range: 22  
  - Source: `sg-public` (choose by SG ID)  

*(Optional if running DB/app inside private subnet)*  
- **Rule 2**  
  - Type: MySQL/Aurora (3306) or Custom TCP  
  - Source: `sg-public` or `sg-private`  

**Outbound rules**
- Leave default (All traffic → `0.0.0.0/0`)

---

## ✅ Connection Testing

Since you **don’t have a bastion**:

### Option A: Public Subnet Test Server
- Launch **Ubuntu EC2** in the **public subnet** with `sg-public`.  
- SSH directly from your laptop:  
  ```bash
  ssh -i my-key.pem ubuntu@<PUBLIC_IP>
  ```
- From there, test Internet connectivity:  
  ```bash
  curl -I https://www.google.com
  ```

### Option B: Private Subnet EC2 (Using Session Manager)
- Launch **Ubuntu EC2** in the **private subnet** with `sg-private`.  
- Attach IAM role with policy: `AmazonSSMManagedInstanceCore`  
- Go to **EC2 → Connect → Session Manager** → You’ll get shell access.  
- Inside, test NAT Gateway Internet:  
  ```bash
  curl -I https://www.google.com
  ```

---
## 🧹 Cleanup (Avoid Charges)
1. Terminate EC2 instances  
2. Delete NAT Gateway → Release Elastic IP  
3. Delete `lab-public-rt` and `lab-private-rt`  
4. Detach & delete `lab-igw`  
5. Delete subnets  
6. Delete VPC  

---

## 🏗️ Architecture Diagram

### ASCII View
```
                   +------------------------+
                   |      lab-vpc (10.0.0.0/16)  
                   |  (Neighborhood Fence)   |
                   +-------------------------+
                           |
                +----------------------+
                |   Internet Gateway   |
                |   (Main Gate)        |
                +----------+-----------+
                           |
          -----------------------------------------
          |                                       |
+----------------------+               +----------------------+
| lab-public-subnet    |               | lab-private-subnet   |
| 10.0.1.0/24          |               | 10.0.2.0/24          |
| (Street: Public)     |               | (Street: Private)    |
+----------+-----------+               +----------+-----------+
           |                                       |
   [ Bastion Host ]                         [ Private App ]
   SG: sg-public                            SG: sg-private
   (Guard at door)                          (Guard at door)
           |
   NAT Gateway (Post Office)  → Outbound Internet Access
```

### PNG View
![AWS VPC Diagram](A_2D_digital_diagram_depicts_an_AWS_VPC_architectu.png)

---

## 🔒 Security Group (SG) vs Network ACL (NACL)  

| Feature                | Security Group (SG) | Network ACL (NACL) |
|-------------------------|---------------------|---------------------|
| Level of operation      | Instance level      | Subnet level        |
| Type                   | **Stateful** (return traffic auto-allowed) | **Stateless** (return traffic must be explicitly allowed) |
| Rules applied to        | Only attached resources (EC2, ENI, etc.) | All resources in the subnet |
| Default behavior        | Deny all inbound, allow all outbound | Allow all inbound & outbound |
| Common use              | Protect individual servers | Broad subnet-level filtering |

### Analogy:
- **Security Group → Guard at each house door** (controls who can enter that specific house).  
- **NACL → Security gate at the street** (controls traffic for every house on that street).  
