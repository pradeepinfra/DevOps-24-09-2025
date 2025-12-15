# 🌱 Terraform Conditional Expressions (Very Simple Guide)

## What is a Conditional Expression?

A **conditional expression** in Terraform is like an **IF–ELSE decision**.

👉 It helps Terraform **choose one value or another** based on a condition.

### Simple Formula
```hcl
condition ? value_if_true : value_if_false
```

### Real-Life Analogy 🧠
Think like this:
- **If it is raining** → take **umbrella**
- **Else** → take **cap**

Same logic in Terraform.

---

## 1️⃣ Simple Example (Basic Understanding)

```hcl
var.environment == "prod" ? "t3.medium" : "t2.micro"
```

- If environment is `prod` → instance type = `t3.medium`
- Else → instance type = `t2.micro`

---

## 2️⃣ Conditional Resource Creation (Create or Skip Resource)

### Question Terraform Asks:
👉 *Should I create this EC2 instance or not?*

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
| Value | Result |
|------|-------|
| `true`  | EC2 is created |
| `false` | EC2 is NOT created |

✅ `count = 0` means **skip resource**

---

## 3️⃣ Conditional Value Selection (Prod vs Dev)

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

### Use in Resource
```hcl
cidr_blocks = var.environment == "prod" ? [var.prod_cidr] : [var.dev_cidr]
```

### Meaning
- If `prod` → use **prod CIDR**
- Else → use **dev CIDR**

---

## 4️⃣ Conditional Security Rule (Enable or Disable SSH)

### Variable
```hcl
variable "enable_ssh" {
  type    = bool
  default = false
}
```

### Security Group Rule
```hcl
cidr_blocks = var.enable_ssh ? ["0.0.0.0/0"] : []
```

### Explanation
| enable_ssh | Result |
|----------|--------|
| true | SSH allowed |
| false | SSH blocked |

🔒 Empty list `[]` means **no access**

---

## 5️⃣ When Should You Use Conditional Expressions?

✅ Enable / disable resources  
✅ Prod vs Dev settings  
✅ Security rules  
✅ Cost control  
✅ Reusable Terraform code  

---

## 🧠 Final One-Line Summary

**Conditional expressions help Terraform make decisions using IF–ELSE logic.**

```hcl
condition ? true_value : false_value
```

---

🎯 **Tip:**  
If you understand **IF–ELSE**, you already understand Terraform conditionals.
