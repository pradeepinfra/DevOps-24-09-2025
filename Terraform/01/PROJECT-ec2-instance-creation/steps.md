# 🚀 Getting Started with Terraform

Think of **Terraform** as a skilled *construction engineer* who builds your AWS infrastructure exactly the way you draw it on paper.  
Your Terraform files are the **blueprints**, and AWS is the **land** where everything will be constructed.

---

# 🧱 Step 1: Create Your Terraform Project

Make a directory for your Terraform project and create a file named **`main.tf`** inside it.  
This file acts like your **project blueprint** that explains:

- Which cloud (provider) to talk to  
- What infrastructure (resources) to build  

## Example Blueprint (`main.tf`)

```hcl
provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
}
```

---

# ⚙️ Step 2: Initialize Terraform

```
terraform init
```

---

# 🚧 Step 3: Apply Your Blueprint

```
terraform apply
```

---

# 🔍 Step 4: Verify Resources

Use AWS Console or AWS CLI to confirm your instance is created.

---

# 🗑️ Step 5: Destroy Resources

```
terraform destroy
```
Be careful: this will delete everything Terraform created.

---
