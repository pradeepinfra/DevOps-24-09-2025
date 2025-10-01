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

### 5) Security Groups
- **Public SG (`sg-public`)**:  
  - Inbound: SSH (22) from your IP `/32`  
  - Outbound: Allow all (default)  

- **Private SG (`sg-private`)**:  
  - Inbound: SSH (22) from `sg-public` (choose by SG ID)  
  - Outbound: Allow all (default)  

### 6) Launch EC2 Instances
- **Bastion Host (Public Subnet):**  
  - AMI: Amazon Linux 2 (or Ubuntu), Type: `t3.micro`  
  - Network: `lab-vpc`, Subnet: `lab-public-subnet`, Auto-assign Public IP → Enable  
  - SG: `sg-public` → **Launch**  

- **Private App Server (Private Subnet):**  
  - Network: `lab-vpc`, Subnet: `lab-private-subnet`, Auto-assign Public IP → Disable  
  - SG: `sg-private` → **Launch**  

### 7) Connectivity Test
- From your machine →  
  ```bash
  ssh -i my-key.pem ec2-user@<BASTION_PUBLIC_IP>
