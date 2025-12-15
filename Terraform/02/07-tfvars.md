# 🌱 Terraform `.tfvars` (With Full AWS EC2 Example)

This README explains **Terraform `.tfvars`** in a **very simple and beginner‑friendly way**, including a **complete AWS EC2 example**.

---

## What is a `.tfvars` file?

A **`.tfvars` file** is used to **store values** for Terraform variables.

- Terraform reads values from `.tfvars`
- Terraform creates resources using those values

---

## Easy Understanding (Analogy)

- `variables.tf` → Questions  
- `.tfvars` → Answers  
- `main.tf` → Actual work  

Terraform flow:
1. Read questions from `variables.tf`
2. Take answers from `.tfvars`
3. Create resources from `main.tf`

---

## Example 1: EC2 Instance Type (Basic)

### variables.tf
```hcl
variable "instance_type" {}
```

### terraform.tfvars
```hcl
instance_type = "t2.micro"
```

👉 Terraform creates EC2 with **t2.micro**

---

## Example 2: Dev and Prod Environments

### variables.tf
```hcl
variable "instance_type" {}
```

### dev.tfvars
```hcl
instance_type = "t2.micro"
```

### prod.tfvars
```hcl
instance_type = "t3.medium"
```

### Commands
```bash
terraform apply -var-file=dev.tfvars
```
👉 Creates **Dev EC2**

```bash
terraform apply -var-file=prod.tfvars
```
👉 Creates **Prod EC2**

---

# 🚀 Full AWS EC2 Example Using `.tfvars`

## Folder Structure
```text
terraform-ec2/
│── main.tf
│── variables.tf
│── terraform.tfvars
```

---

## variables.tf (Questions)
```hcl
variable "region" {
  description = "AWS region"
}

variable "ami_id" {
  description = "AMI ID"
}

variable "instance_type" {
  description = "EC2 instance type"
}

variable "tags" {
  description = "EC2 tags"
  type        = map(string)
}
```

---

## terraform.tfvars (Answers)
```hcl
region        = "us-west2-1"
ami_id        = "ami-00f46ccd1cbfb363e"
instance_type = "t2.micro"

tags = {
  Name        = "Terraform-EC2"
  Environment = "Dev"
}
```

---

## main.tf (Actual Work)
```hcl
provider "aws" {
  region = var.region
}

resource "aws_instance" "example" {
  ami           = var.ami_id
  instance_type = var.instance_type

  tags = var.tags
}
```

---

## How to Run

```bash
terraform init
terraform apply
```

👉 Terraform automatically reads `terraform.tfvars`  
👉 EC2 instance is created in AWS

---

## Important Notes

- `.tfvars` contains **only values**
- No resources
- No logic
- Same code works for **dev / prod / test**

---

## One‑Line Interview Answer 🎯

> **`.tfvars` file is used to store variable values so the same Terraform code can be reused across environments like dev and prod.**

---

✅ Simple  
✅ Beginner Friendly  
✅ Real AWS Example  
✅ Interview Ready
