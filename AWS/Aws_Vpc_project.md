# AWS VPC —Manual Path (2025 Console)

> **Single option only.** Clean, non-duplicated, manual console steps with a short analogy + CIDR plan. No CLI/Terraform. Includes one NACL configuration.

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

**Correct Abbreviations:**
- VPC → Virtual Private Cloud
- IGW → Internet Gateway
- NAT GW → Network Address Translation Gateway
- SG → Security Group
- RT → Route Table

## CIDR Plan (use exactly these)

- VPC: `10.0.0.0/16`
- Public subnet: `10.0.1.0/24`
- Private subnet: `10.0.2.0/24`

---

## Step-by-Step (Console Only)

### 1) Create VPC

- VPC → Your VPCs → **Create VPC**
  - Name: `lab-vpc`
  - IPv4 CIDR: `10.0.0.0/16` → **Create**

### 2) Create Subnets

- VPC → Subnets → **Create subnet** → `lab-public-subnet`, VPC `lab-vpc`, AZ any, CIDR `10.0.1.0/24` → **Create**
- Select `lab-public-subnet` → **Actions → Modify auto‑assign IP** → **Enable Auto‑assign IPv4**
- VPC → Subnets → **Create subnet** → `lab-private-subnet`, VPC `lab-vpc`, same AZ, CIDR `10.0.2.0/24` → **Create**

### 3) Internet Gateway (IGW) + Public Route

- VPC → Internet Gateways → **Create** → Name `lab-igw` → **Create**
- Select `lab-igw` → **Attach to VPC** → `lab-vpc`
- VPC → Route tables → **Create** → Name `lab-public-rt`, VPC `lab-vpc`
- Open `lab-public-rt` → **Routes → Edit** → Add `0.0.0.0/0` → Target **Internet Gateway** `lab-igw` → **Save**
- **Subnet associations → Edit** → select `lab-public-subnet` → **Save**

### 4) NAT Gateway + Private Route

- VPC → NAT Gateways → **Create** → Subnet `lab-public-subnet`, Elastic IP **Allocate new**, Name lab-nat` → **Create** (wait **Available**)
- VPC → Route tables → **Create** → Name `lab-private-rt`, VPC `lab-vpc`
- Open `lab-private-rt` → **Routes → Edit** → Add `0.0.0.0/0` → Target **NAT Gateway** `lab-nat` → **Save**
- **Subnet associations → Edit** → select `lab-private-subnet` → **Save**

### 5) Security Groups

- VPC → Security Groups → **Create** → Name `sg-public`, VPC `lab-vpc`
  - Inbound: SSH (22) from your IP `/32`
  - Outbound: Allow all (default)
- **Create** `sg-private`, VPC `lab-vpc`
  - Inbound: SSH (22) from **`sg-public`** (select by SG ID)
  - Outbound: Allow all (default)

### 6) Launch EC2 Instances

- **Bastion (public)** — EC2 → Instances → **Launch**
  - AMI: Amazon Linux 2 (or Ubuntu), Type `t3.micro`
  - Network `lab-vpc`, Subnet `lab-public-subnet`, **Auto‑assign Public IP: Enable**
  - SG: `sg-public`, Key pair: your key → **Launch**
- **Private App** — **Launch**
  - Network `lab-vpc`, Subnet `lab-private-subnet`, **Auto‑assign Public IP: Disable**
  - SG: `sg-private`, Key pair: your key → **Launch**

### 7) Connectivity Check

- From your machine → `ssh -i my-key.pem ec2-user@<BASTION_PUBLIC_IP>`
- From bastion → `ssh -i my-key.pem ec2-user@10.0.2.x`
- On private EC2 → `curl -I https://example.com` (works via NAT)

---

## Cleanup (avoid charges)

1. Terminate both EC2 instances
2. Delete NAT Gateway → release Elastic IP
3. Delete `lab-public-rt` and `lab-private-rt` (or remove routes, then delete)
4. Detach & delete `lab-igw`
5. Delete subnets
6. Delete VPC



