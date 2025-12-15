# 🌱 Terraform Conditional Expressions (Very Simple Guide)

## What is a Conditional Expression?

A **conditional expression** in Terraform is like an **IF–ELSE decision**.

👉 It helps Terraform **choose one value or another** based on a condition.

### Simple Formula
```hcl
condition ? value_if_true : value_if_false
```

### Real-Life Analogy 🧠
- **If salary is high** → buy **car**
- **Else** → buy **bike**

Terraform works the same way.

---

## 1️⃣ Very Basic Example (Start Here)

```hcl
var.environment == "prod" ? "t3.medium" : "t2.micro"
```

### Meaning
- If environment = `prod` → use `t3.medium`
- Else → use `t2.micro`

---

## 2️⃣ Example Resource 1: Create or Skip EC2 Instance

### Use Case
👉 *Create EC2 only when required*

### Variable
```hcl
variable "create_instance" {
  type    = bool
  default = true
}
```

### Resource
```hcl
resource "aws_instance" "example" {
  count = var.create_instance ? 1 : 0

  ami           = "ami-123456"
  instance_type = "t2.micro"
}
```

### Explanation
| create_instance | Result |
|----------------|--------|
| true | EC2 created |
| false | EC2 skipped |

✅ `count = 0` means **no resource**

---

## 3️⃣ Example Resource 2: Different Instance Types for Dev & Prod

### Variable
```hcl
variable "environment" {
  default = "dev"
}
```

### Resource
```hcl
resource "aws_instance" "env_example" {
  ami = "ami-123456"

  instance_type = var.environment == "prod" ? "t3.medium" : "t2.micro"
}
```

### Explanation
- Dev → cheap instance
- Prod → powerful instance 💰

---

## 4️⃣ Example Resource 3: Conditional Security Group (Enable SSH)

### Variable
```hcl
variable "enable_ssh" {
  type    = bool
  default = false
}
```

### Resource
```hcl
resource "aws_security_group" "ssh_example" {
  name = "ssh-sg"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = var.enable_ssh ? ["0.0.0.0/0"] : []
  }
}
```

### Explanation
| enable_ssh | SSH Access |
|----------|------------|
| true | Allowed |
| false | Blocked 🔒 |

---

## 5️⃣ Example Resource 4: Conditional Subnet CIDR (Prod vs Dev)

### Variables
```hcl
variable "environment" {
  default = "dev"
}

variable "prod_cidr" {
  default = "10.0.1.0/24"
}

variable "dev_cidr" {
  default = "10.0.2.0/24"
}
```

### Resource
```hcl
resource "aws_subnet" "example" {
  vpc_id     = "vpc-123456"
  cidr_block = var.environment == "prod" ? var.prod_cidr : var.dev_cidr
}
```

### Explanation
- Prod → prod network
- Dev → dev network

---

## 6️⃣ Example Resource 5: Conditional Tags

### Resource
```hcl
resource "aws_instance" "tag_example" {
  ami           = "ami-123456"
  instance_type = "t2.micro"

  tags = {
    Backup = var.environment == "prod" ? "enabled" : "disabled"
  }
}
```

### Meaning
- Prod → backups enabled
- Dev → backups disabled

---

## 7️⃣ When Should You Use Conditional Expressions?

✅ Create / skip resources  
✅ Dev vs Prod configuration  
✅ Security enable / disable  
✅ Cost control  
✅ Reusable Terraform code  

---

## 🧠 One-Line Summary (Interview Ready)

**Terraform conditional expressions use IF–ELSE logic to control resource creation and configuration.**

```hcl
condition ? true_value : false_value
```

🎯 If you understand **IF–ELSE**, you understand Terraform conditionals.
