
# 🌱 Terraform Variables – Input & Output (Simple Way)

Think of Terraform like a machine that builds cloud resources.

Before starting → it asks questions (Input Variables)  
After finishing → it shows results (Output Variables)

---

## 1. What Are Variables?

Variables are containers to store values.

Instead of repeating values like region, instance type, or names,
you store them once and reuse them.

Benefits:
- Easy to change
- Reusable code
- Same code for dev / test / prod

---

## Simple Analogy

Ordering food online:

You select item and size → Input variables  
App shows order ID → Output variables

Terraform works the same way.

---

## 2. Input Variables

Input variables are values you give before Terraform runs.

Example:
```hcl
variable "instance_type" {
  type    = string
  default = "t2.micro"
}
```

Usage:
```hcl
resource "aws_instance" "example" {
  instance_type = var.instance_type
}
```

Ways to pass values:
1. Default value
2. terraform.tfvars
3. Command line

---

## 3. Output Variables

Output variables show results after apply.

```hcl
output "instance_id" {
  value = aws_instance.example.id
}
```

---

## 4. Mini EC2 Example

variables.tf
```hcl
variable "instance_name" {
  type    = string
  default = "my-server"
}
```

main.tf
```hcl
resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"

  tags = {
    Name = var.instance_name
  }
}
```

outputs.tf
```hcl
output "public_ip" {
  value = aws_instance.example.public_ip
}
```

---

## 5. Variable Types

string  → "t2.micro"  
number  → 1, 2  
bool    → true / false  
list    → ["a","b"]  
map     → { env = "dev" }

---

## Summary

Input variables = questions Terraform asks  
Output variables = answers Terraform gives  

Inputs before build  
Outputs after build
