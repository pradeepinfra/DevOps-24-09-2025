# AWS VPC — Manual Path (2025 Console)

> **Single option only.** Clean, non-duplicated, manual console steps with a short analogy + CIDR plan. No CLI/Terraform. Includes one NACL configuration.  
> **Important:** When creating the VPC, select **“VPC only”** (not “VPC and more”).

---

## Analogy (with real-world story + real-time sentences)

Think of AWS networking like a **neighborhood**. Each part of AWS networking maps to something students already know, plus a real-time sentence to say during class:

### 1. VPC (Virtual Private Cloud)
- **What it is:** A logically isolated part of AWS where you create your own network.  
- **Analogy:** The entire **neighborhood**, fenced and private.  
- **Real-time sentence:** “We’re creating our own neighborhood in AWS. It’s fenced off, and only the gates we build will connect it to the outside world.”  

### 2. Subnet
- **What it is:** A section of the VPC IP range.  
- **Analogy:** A **street** inside the neighborhood.  
- **Real-time sentence:** “This subnet is like a street. One street is public and connected to the city road, the other is private and has no direct road out.”  

### 3. IGW (Internet Gateway)
- **What it is:** Gateway to connect the VPC to the Internet.  
- **Analogy:** The **main gate** of the neighborhood.  
- **Real-time sentence:** “This is the gate — without it, no one from our neighborhood can reach the Internet.”  

### 4. NAT GW (Network Address Translation Gateway)
- **What it is:** Lets private subnet instances access the Internet, hiding their IPs.  
- **Analogy:** The **post office** that sends letters on behalf of houses.  
- **Real-time sentence:** “Private houses can’t go out directly; they send their letters through the post office, which hides their home address.”  

### 5. SG (Security Group)
- **What it is:** Firewall rules attached to instances. **Stateful**.  
- **Analogy:** The **guard at each house’s door**.  
- **Real-time sentence:** “The guard checks the guest list. If I allow only my laptop IP for SSH, that’s who the guard lets in.”  

### 6. RT (Route Table)
- **What it is:** Routing rules for subnets.  
- **Analogy:** The **map of the neighborhood**.  
- **Real-time sentence:** “The map says: if you want to go to the Internet, take the gate. If you’re in the private street, send it to the post office (NAT).”  

### 7. NACL (Network Access Control List)
- **What it is:** Firewall rules at the subnet level. **Stateless**.  
- **Analogy:** The **security gate at the street entrance**.  
- **Real-time sentence:** “Even before you reach a house guard (SG), there’s a street gate (NACL) deciding who can walk down the street at all.”  

---

## CIDR Plan

- VPC: `10.0.0.0/16`  
- Public subnet: `10.0.1.0/24`  
- Private subnet: `10.0.2.0/24`  

---

## Step-by-Step (Console Only)

### 1) Create VPC
- VPC → Your VPCs → **Create VPC**  
- Select **VPC only**  
- Name: `lab-vpc`  
- IPv4 CIDR: `10.0.0.0/16` → **Create**  

---

### 2) Create Subnets
- VPC → Subnets → **Create subnet** → `lab-public-subnet`, VPC `lab-vpc`, AZ any, CIDR `10.0.1.0/24` → **Create**  
- Select `lab-public-subnet` → **Actions → Modify auto-assign IP** → **Enable Auto-assign IPv4**  
- VPC → Subnets → **Create subnet** → `lab-private-subnet`, VPC `lab-vpc`, same AZ, CIDR `10.0.2.0/24` → **Create**  

---

### 3) Internet Gateway (IGW) + Public Route
- VPC → Internet Gateways → **Create** → Name `lab-igw` → **Create**  
- Select `lab-igw` → **Attach to VPC** → `lab-vpc`  
- VPC → Route tables → **Create** → Name `lab-public-rt`, VPC `lab-vpc`  
- Open `lab-public-rt` → **Routes → Edit** → Add `0.0.0.0/0` → Target **Internet Gateway** `lab-igw` → **Save**  
- **Subnet associations → Edit → select only `lab-public-subnet` → Save**  

---

### 4) NAT Gateway + Private Route
- VPC → NAT Gateways → **Create** → Subnet `lab-public-subnet`, Elastic IP **Allocate new**, Name `lab-nat` → **Create** (wait until **Available**)  
- VPC → Route tables → **Create** → Name `lab-private-rt`, VPC `lab-vpc`  
- Open `lab-private-rt` → **Routes → Edit** → Add `0.0.0.0/0` → Target **NAT Gateway** `lab-nat` → **Save**  
- **Subnet associations → Edit → select only `lab-private-subnet` → Save**  

👉 **Rule:** Do not associate both subnets to the same route table.  
- Public RT → public subnet only  
- Private RT → private subnet only  

---

### 5) Security Groups
- VPC → Security Groups → **Create** → Name `sg-public`, VPC `lab-vpc`  
  - Inbound: SSH (22) from your IP `/32`  
  - Outbound: Allow all (default)  

- **Create** `sg-private`, VPC `lab-vpc`  
  - Inbound: SSH (22) from **`sg-public`** (select by SG ID)  
  - Outbound: Allow all (default)  

---

### 6) NACL (Network ACL)
- VPC → Network ACLs → **Create** → Name `lab-nacl`, VPC `lab-vpc`  
- Open `lab-nacl` → **Inbound rules → Edit** →  
  - Allow `100` → `0.0.0.0/0` → **SSH (22)** → ALLOW  
  - Allow `101` → `0.0.0.0/0` → **HTTP (80)** → ALLOW  

- **Outbound rules → Edit** →  
  - Rule `100` → `0.0.0.0/0` → ALL traffic → ALLOW  

- **Subnet associations → Edit → Associate `lab-public-subnet`**  

👉 (Private subnet can stay with default NACL unless you want stricter rules.)  

---

### 7) Launch EC2 Instances
- **Bastion (public)** — EC2 → Instances → **Launch**  
  - AMI: Amazon Linux 2 (or Ubuntu), Type `t3.micro`  
  - Network `lab-vpc`, Subnet `lab-public-subnet`, **Auto-assign Public IP: Enable**  
  - SG: `sg-public`, Key pair: your key → **Launch**  

- **Private App** — **Launch**  
  - Network `lab-vpc`, Subnet `lab-private-subnet`, **Auto-assign Public IP: Disable**  
  - SG: `sg-private`, Key pair: your key → **Launch**  

---

### 8) Connectivity Check
From your machine:  
```bash
ssh -i my-key.pem ec2-user@<BASTION_PUBLIC_IP>
