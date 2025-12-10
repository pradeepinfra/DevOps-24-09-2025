# 🌱 Terraform `.tfvars`

## What is a `.tfvars` file?

A `.tfvars` file is where you keep the **values** for the variables you defined in Terraform.

### Simple Analogy
- `variables.tf` = **Questions**
- `.tfvars`      = **Your answers**

Terraform uses these answers when creating infrastructure.

---

## Why use `.tfvars`?

1. Keeps values separate from your main Terraform code  
2. Allows different values for **dev**, **test**, **prod**  
3. Lets you reuse the same Terraform code  
4. Helps store sensitive values safely  

---

## Example

### variables.tf
```hcl
variable "instance_type" {
  type = string
}

variable "environment" {
  type = string
}
```

### dev.tfvars
```hcl
instance_type = "t2.micro"
environment   = "dev"
```

### prod.tfvars
```hcl
instance_type = "t3.medium"
environment   = "prod"
```

---

## How to use `.tfvars`

### Apply dev values
```bash
terraform apply -var-file=dev.tfvars
```

### Apply prod values
```bash
terraform apply -var-file=prod.tfvars
```

---

## Summary
- `.tfvars` = **Place where your actual values live**
- Makes Terraform clean, reusable, and easy to manage across environments
