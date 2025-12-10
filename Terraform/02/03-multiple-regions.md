# 🌍 Multi-Region Setup in Terraform

Sometimes you need to deploy infrastructure **in more than one AWS region** — for example, one server in **US-East-1** and another in **US-West-2**. Terraform allows this using the **`alias`** keyword.

---

## 🧠 Analogy: Multiple Offices, Multiple Managers

Imagine your company has **two offices**:

- 🏢 Office A — US-East-1  
- 🏢 Office B — US-West-2  

Each office has its own **manager** who understands that region.

In Terraform:

- A **provider** = the *manager*  
- An **alias** = the *manager's name*  
- A **resource** = a *task you assign to the manager*  

So you create two AWS provider managers and assign tasks (resources) to the correct one.

---

## ✅ Terraform Example

```hcl
# Manager for Office A (US-East-1)
provider "aws" {
  alias  = "us-east-1"    # Manager name
  region = "us-east-1"    # Office location
}

# Manager for Office B (US-West-2)
provider "aws" {
  alias  = "us-west-2"    # Manager name
  region = "us-west-2"    # Office location
}

# Task assigned to Manager of Office A
resource "aws_instance" "example" {
  ami           = "ami-0123456789abcdef0"
  instance_type = "t2.micro"
  provider      = aws.us-east-1
}

# Task assigned to Manager of Office B
resource "aws_instance" "example2" {
  ami           = "ami-0123456789abcdef0"
  instance_type = "t2.micro"
  provider      = aws.us-west-2
}
```

---

## 🎯 Summary

- Use **multiple providers** for multiple regions  
- Give each one an **alias**  
- Assign resources to the correct region using `provider = aws.alias-name`  

Just like assigning tasks to different office managers!

