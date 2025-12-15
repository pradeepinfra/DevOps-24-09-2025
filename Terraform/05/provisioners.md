
# 🚀 Terraform EC2 + Flask App (Step-by-Step)

This project demonstrates **how Terraform creates AWS infrastructure and then configures an EC2 instance using provisioners**.

You will:
- Create VPC, Subnet, Security Group
- Launch an EC2 instance
- Copy a Flask app to EC2
- Run the app automatically

---

## 🧱 Architecture Overview

Terraform creates resources in this order:

1. AWS Provider connection
2. VPC
3. Subnet
4. Internet Gateway
5. Route Table
6. Security Group (SSH + HTTP)
7. Key Pair
8. EC2 Instance
9. File Provisioner (copy app)
10. Remote-Exec Provisioner (install & run app)

---

## 📁 Project Structure

```
.
├── main.tf
└── app.py
```

---

## 📄 main.tf (What it does)

- Creates AWS networking (VPC, subnet, routes)
- Launches EC2
- Uses **file provisioner** to copy `app.py`
- Uses **remote-exec provisioner** to:
  - Install Python & Flask
  - Run the Flask app

---

## 📄 app.py

A simple Flask application:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Terraform!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
```

---

## ▶️ How to Run

### 1️⃣ Initialize Terraform
```bash
terraform init
```

### 2️⃣ Apply Configuration
```bash
terraform apply
```
Type `yes` when asked.

---

## 🌐 Access the Application

After apply completes, open:

```
http://<EC2_PUBLIC_IP>
```

You should see:

```
Hello, Terraform!
```

---

## 🧠 Provisioners Explained (Simple)

### 📤 file provisioner
Copies files from your local machine to EC2.

### ⚙️ remote-exec provisioner
Runs Linux commands inside EC2.

### 💻 local-exec provisioner
Runs commands on your local machine (not used here).

---

## ⚠️ Important Note (Interview Tip)

Provisioners are **not recommended for production**.

Preferred options:
- user_data
- Ansible
- Packer AMIs

Provisioners are best for:
- Learning
- Demo
- Proof of Concept (PoC)

---

## ✅ One-Line Summary

Terraform builds infrastructure first, then provisioners configure the server.

---

Happy Learning 🚀
