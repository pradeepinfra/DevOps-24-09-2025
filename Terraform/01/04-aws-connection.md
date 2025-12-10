# 🚀 Setup Terraform for AWS

Think of **Terraform** as an engineer who builds your cloud infrastructure.

Before this engineer can work inside AWS, you must:

1. Provide **ID proof** (AWS credentials)
2. Give them a **walkie‑talkie** (AWS CLI)
3. Grant **permissions** (IAM user)

---

## ❓ Why Use AWS CLI?
**Analogy:**  
AWS CLI is like giving Terraform a **walkie-talkie + address book** so it knows *how* to reach AWS and *who* it is while talking.

### Simple Explanation  
Terraform does **not** store your AWS credentials.  
It relies on AWS CLI to:

- Store your **Access Key & Secret Key**
- Set your **default region**
- Authenticate Terraform whenever it talks to AWS
- Make communication smooth between Terraform → AWS

### In short:  
**AWS CLI = communication bridge** between your machine and AWS.  
Without it, Terraform wouldn't know *who you are* or *which AWS account to use*.

---

## 🛠️ 1. Install AWS CLI  
**Analogy:** AWS CLI is like giving Terraform a walkie‑talkie so it can talk to AWS.

Install AWS CLI:  
https://aws.amazon.com/cli/

Check version:

```bash
aws --version
```

---

## 👤 2. Create an AWS IAM User  
**Analogy:** IAM User = worker badge for Terraform inside AWS.

### Steps  
1. Log in to AWS console  
2. Go to **IAM → Users → Add user**  
3. Choose username  
4. Select **Programmatic access**  
5. Attach permissions  
   Example:  
   - `AmazonEC2FullAccess`  
6. Create user  
7. Save **Access Key ID** and **Secret Access Key**

---

## 🔑 3. Configure AWS CLI Credentials  
**Analogy:**  
You're giving Terraform its locker key, AWS address (region), and communication method.

Run:

```bash
aws configure
```

Enter:  
- Access Key ID  
- Secret Access Key  
- Default region (e.g., ap-south-1)  
- Output format (json)

---

Terraform is now ready to build AWS resources! 🚀
