# 🌱 Terraform `.tfvars` Files (With Analogies & Examples)

Think of Terraform like a **master chef** following a recipe:

- The **recipe** = your Terraform code (`.tf` files)
- The **ingredients list** = your **variables** (`variables.tf`)
- The **shopping list for today** = your **`.tfvars` file** (actual values to use *this time*)

You can cook the **same recipe** (same Terraform code) with **different shopping lists** (`dev.tfvars`, `prod.tfvars`, etc.) to match each environment.

---

## 🤔 What is a `.tfvars` File?

A `.tfvars` file is a simple text file where you **assign values** to the input variables you defined in your Terraform configuration.

- File names usually end with: `.tfvars` or `.auto.tfvars`
- Example names: `dev.tfvars`, `prod.tfvars`, `secrets.tfvars`

It helps you:

1. Separate **configuration values** from **Terraform code**
2. Manage **multiple environments** easily
3. Handle **sensitive values** more safely
4. Let each team member have their **own settings**

---

## 🧩 Analogy: Code vs `.tfvars`

Imagine you run a burger shop:

- The **Terraform code** is the **burger machine** – how to assemble burgers.
- **Variables** are like **options**: which bread, which patty, which sauce.
- A **`.tfvars` file** is a **predefined combo**: “Dev Burger Combo”, “Prod Burger Combo”.

You don’t change the **machine** each time.  
You just change the **combo values** using different `.tfvars` files.

---

## 🗂 File Structure Example

```bash
terraform-tfvars-demo/
├── main.tf
├── variables.tf
├── dev.tfvars
└── prod.tfvars
```

### `variables.tf` – Define the “questions”

```hcl
variable "environment" {
  description = "Name of the environment"
  type        = string
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
}

variable "instance_count" {
  description = "Number of instances to create"
  type        = number
  default     = 1
}
```

### `dev.tfvars` – Answers for **Dev environment**

```hcl
environment    = "dev"
instance_type  = "t2.micro"
instance_count = 1
```

### `prod.tfvars` – Answers for **Production environment**

```hcl
environment    = "prod"
instance_type  = "t3.medium"
instance_count = 3
```

### `main.tf` – Using those variables

```hcl
resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = var.instance_type
  count         = var.instance_count

  tags = {
    Name        = "demo-${var.environment}-instance"
    Environment = var.environment
  }
}
```

Here:

- Same code in `main.tf`
- Different behavior based on **which `.tfvars` file** you pass

---

## ⚙️ How to Use `.tfvars` Files

### 1️⃣ Apply using a specific `.tfvars` file

```bash
terraform apply -var-file=dev.tfvars
```

or

```bash
terraform apply -var-file=prod.tfvars
```

It’s like telling Terraform:

> “Run the same recipe, but use the values from **this** file.”

### 2️⃣ Plan with a `.tfvars` file

```bash
terraform plan -var-file=dev.tfvars
```

This lets you **preview** exactly what will happen with that set of values.

---

## 🔐 Using `.tfvars` for Sensitive Values

Analogy: `.tf` file is the **menu on the wall**, visible to everyone.  
`.tfvars` with secrets is like a **private notebook in the kitchen** – only staff can see it.

Example `secrets.tfvars`:

```hcl
db_username = "admin_user"
db_password = "super-secret-password"
```

> 💡 **Important:** Add sensitive `.tfvars` files to `.gitignore` so they don’t go into Git.

Example `.gitignore` entry:

```bash
*.tfvars
!example.tfvars   # keep only a non-sensitive sample in Git
```

You can still keep a **sample file** like `example.tfvars` with fake values to show the structure to your teammates.

---

## 🧠 `.auto.tfvars` – Auto-Loaded Files

Terraform automatically loads files that end with `*.auto.tfvars`.

Example:

- `dev.auto.tfvars`

Then you can simply run:

```bash
terraform apply
```

No need to pass `-var-file`.  
Analogy: These are **default settings** Terraform picks up automatically if found.

---

## 👥 Collaboration Benefits

In a team:

- Everyone shares the **same `.tf` code**
- Each person can have their **own `.tfvars`** file (like `pradeep.dev.tfvars`)
- No need to constantly edit the main Terraform files

This avoids annoying merge conflicts and keeps your repo clean.

---

## ✅ Quick Summary

- **`.tfvars` files** store **values** for Terraform variables.
- They help you:
  - Separate **code** and **configuration**
  - Reuse the **same Terraform code** for **multiple environments**
  - Keep **secrets outside** your main code and Git
  - Let each person/team/environment have their **own settings**

### Basic Workflow

1. Define variables in `variables.tf`
2. Create one or more `.tfvars` files (`dev.tfvars`, `prod.tfvars`, `secrets.tfvars`)
3. Run Terraform with:

   ```bash
   terraform plan  -var-file=dev.tfvars
   terraform apply -var-file=dev.tfvars
   ```

Terraform is your **builder**, variables are its **questions**, and `.tfvars` files are your **answer sheets** for each environment 🎯
