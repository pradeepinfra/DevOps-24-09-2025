# 🌱 When Do We Use `.tfvars` in Terraform?

Terraform uses **variables** to make infrastructure code flexible and reusable.  
The **`.tfvars` file** is used to provide *actual values* for those variables.

---

## 🧠 Simple Analogy

Think of Terraform like filling an online form:

- `variables.tf` → ❓ Questions (What do you want?)
- `main.tf` → 🏗️ Work (Create infrastructure)
- `.tfvars` → ✍️ Answers (Your chosen values)

Same questions, different answers = different environments.

---

## ❌ Without `.tfvars` (Not Recommended)

```hcl
variable "instance_type" {
  default = "t3.micro"
}
```

### Problems
- Values are hard-coded  
- Not flexible  
- Difficult to manage multiple environments  

---

## ✅ With `.tfvars` (Recommended)

### 1️⃣ `variables.tf` (Questions)

```hcl
variable "instance_type" {
  type = string
}

variable "environment" {
  type = string
}
```

---

### 2️⃣ `dev.tfvars` (Answers for Dev)

```hcl
instance_type = "t3.micro"
environment   = "dev"
```

---

### 3️⃣ `prod.tfvars` (Answers for Prod)

```hcl
instance_type = "t3.medium"
environment   = "prod"
```

✔ Same Terraform code  
✔ Different values  
✔ Different infrastructure  

---

## 📌 When EXACTLY Do We Use `.tfvars`?

### ✅ Use `.tfvars` when:

### 1️⃣ Multiple Environments

```text
dev.tfvars
test.tfvars
prod.tfvars
```

---

### 2️⃣ Values Change Frequently

- Instance type  
- Region  
- AMI ID  
- Instance count  

---

### 3️⃣ Team Collaboration

- Code remains same  
- Each team/environment uses its own `.tfvars`  

---

### 4️⃣ Avoid Hard-Coding Values

❌ Bad Practice:
```hcl
instance_type = "t3.micro"
```

✅ Good Practice:
```hcl
instance_type = var.instance_type
```

---

### 5️⃣ Environment-Specific or Sensitive Data

- Passwords  
- CIDR blocks  
- Sizes and names  

📌 Usually `.tfvars` files are added to `.gitignore`.

---

## ▶️ How Terraform Loads `.tfvars`

### 🔹 Automatic Loading

Terraform automatically loads:

```text
terraform.tfvars
*.auto.tfvars
```

---

### 🔹 Manual Loading

```bash
terraform apply -var-file="dev.tfvars"
```

---

## 🧪 Real EC2 Example

### `variables.tf`

```hcl
variable "instance_type" {}
variable "name" {}
```

---

### `main.tf`

```hcl
resource "aws_instance" "example" {
  ami           = "ami-0abcd1234"
  instance_type = var.instance_type

  tags = {
    Name = var.name
  }
}
```

---

### `dev.tfvars`

```hcl
instance_type = "t3.micro"
name          = "dev-server"
```

---

### `prod.tfvars`

```hcl
instance_type = "t3.large"
name          = "prod-server"
```

---

## 🎯 Interview One-Line Answer

> **We use `.tfvars` to separate configuration values from Terraform code so the same code can be reused for multiple environments like dev, test, and prod.**

---

✅ Clean code  
✅ Easy changes  
✅ Real-world best practice
