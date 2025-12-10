# 🌱 Terraform Variables – Input & Output (with Simple Analogies)

Think of **Terraform** as an engineer building your cloud setup.

To work smartly instead of hard-coding everything, the engineer asks:
- **Questions before work starts** → 🔹 *Input Variables*
- **Gives you key answers after work is done** → 🔹 *Output Variables*

---

## 1️⃣ What Are Variables in Terraform?

Variables are **placeholders for values**.

- Instead of writing the same value in many places (like a region, instance type, or name),  
  you store it in a **variable** and reuse it.
- This makes your code:
  - ✅ Reusable  
  - ✅ Easy to change  
  - ✅ Easy to share

### 🧠 Analogy

Imagine ordering a custom T-shirt online:

- The website asks you: **size, color, text on T-shirt** → These are **input variables**.
- After you place the order, the website shows: **order ID, price, delivery date** → These are **output variables**.

Terraform works in the same way.  
It asks for **inputs** and gives **outputs**.

---

## 2️⃣ Input Variables – “Questions Terraform Asks You”

Input variables let you **pass values into Terraform** from the outside, instead of hard-coding them.

### Example: Declaring an Input Variable

```hcl
variable "example_var" {
  description = "An example input variable"
  type        = string
  default     = "default_value"
}
```

**Explanation:**

- `variable "example_var"` – This creates a variable named `example_var`.
- `description` – Human-friendly explanation of what this variable is for.
- `type` – What kind of value is allowed (e.g., `string`, `number`, `bool`, `list`, `map`).
- `default` – Value used if you don’t explicitly provide one.

### Using the Variable in a Resource

```hcl
resource "example_resource" "example" {
  name = var.example_var
}
```

- `var.example_var` – This is how you **refer to** the variable in your code.
- Wherever `var.example_var` is used, Terraform will substitute the value you give.

### 🧠 Analogy

Think of an **input variable** as a blank field on a form:
- Terraform: “What instance type do you want?”  
- You: “t3.micro”  
- Terraform fills that answer wherever `var.instance_type` is used.

### How Do You Set Input Variable Values? (Common Ways)

You don’t have to only use `default`. You can set values in several ways:

1. **Use default value** (if defined in the variable block)  
2. **`terraform.tfvars` file**  
3. **Command line** using `-var`:
   ```bash
   terraform apply -var="example_var=custom_value"
   ```

---

## 3️⃣ Output Variables – “Answers Terraform Gives You”

Output variables let Terraform **show you important information** after it finishes creating resources.

They are useful for:
- Showing values in the terminal after `apply`
- Passing values from one module to another
- Feeding information to other tools (like scripts or CI/CD)

### Example: Declaring an Output Variable

```hcl
output "example_output" {
  description = "An example output variable"
  value       = resource.example_resource.example.id
}
```

**Explanation:**

- `output "example_output"` – This creates an output named `example_output`.
- `description` – What this output represents.
- `value` – What Terraform should return (usually some resource attribute).

### 🧠 Analogy

Imagine you booked a movie ticket online:

- You entered inputs like **movie name, date, seat** (input variables).
- The system shows your **booking ID and seat number** on the screen → those are like **output variables**.

Terraform outputs work the same:
- After `terraform apply`, Terraform prints the values you asked for as outputs.

---

## 4️⃣ Connecting Modules with Outputs

When using **modules**, outputs are how a child module gives values back to the root (or parent) module.

### In the Module (child):

```hcl
output "example_output" {
  value = resource.example_resource.example.id
}
```

### In the Root Module:

```hcl
output "root_output" {
  value = module.example_module.example_output
}
```

- `module.example_module.example_output` – This reads the output from `example_module`.
- It’s like getting a **report** from a sub-team and then using it in the main project.

---

## 5️⃣ Mini End-to-End Example

### `variables.tf`

```hcl
variable "instance_name" {
  description = "Name of the EC2 instance"
  type        = string
  default     = "my-example-instance"
}
```

### `main.tf`

```hcl
resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"

  tags = {
    Name = var.instance_name
  }
}
```

### `outputs.tf`

```hcl
output "instance_id" {
  description = "ID of the created EC2 instance"
  value       = aws_instance.example.id
}

output "instance_public_ip" {
  description = "Public IP of the EC2 instance"
  value       = aws_instance.example.public_ip
}
```

### After `terraform apply`

Terraform will show something like:

```text
Outputs:

instance_id = "i-0abcd1234efgh5678"
instance_public_ip = "3.111.222.33"
```

Now you can **copy-paste** this IP to SSH into the instance or share the ID with others.

---

## 6️⃣ Quick Memory Tricks

- **Input variable** = Terraform asking **you** something  
  👉 “What values should I use?”

- **Output variable** = Terraform telling **you** something  
  👉 “Here’s the important information you might need.”

- Inputs = 🎛️ *Settings you choose before building*  
- Outputs = 📋 *Results you get after building*

---

## ✅ Summary

- Use **input variables** to make your Terraform code flexible and reusable.
- Use **output variables** to expose important information from your infrastructure.
- Together, they make your Terraform configurations **clean, modular, and easy to manage**.

You can now safely think of Terraform as a smart system that:
- Asks for the right **inputs** 📝
- And returns the right **outputs** 📦
