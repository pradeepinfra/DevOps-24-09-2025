# 🧰 Install AWS CLI on Ubuntu

The **AWS Command Line Interface (CLI)** allows you to manage AWS services directly from your terminal.

---

## ✅ Step 1: Update your System

```bash
sudo apt update && sudo apt upgrade -y
```

---

## ✅ Step 2: Install Required Dependencies

```bash
sudo apt install unzip curl -y
```

---

## ✅ Step 3: Download the AWS CLI Installer

```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
```

---

## ✅ Step 4: Unzip the Downloaded File

```bash
unzip awscliv2.zip
```

---

## ✅ Step 5: Run the Installer

```bash
sudo ./aws/install
```

---

## ✅ Step 6: Verify the Installation

```bash
aws --version
```

**Example output:**
```
aws-cli/2.15.30 Python/3.11.2 Linux/5.15.0-113-generic exe/x86_64.ubuntu.22 prompt/off
```

---

## ✅ Step 7: Configure AWS CLI

```bash
aws configure
```

You will be prompted for:

```
AWS Access Key ID [None]: <your-access-key>
AWS Secret Access Key [None]: <your-secret-key>
Default region name [None]: ap-south-1
Default output format [None]: json
```

---

## ✅ Step 8: Test Your Setup

List all S3 buckets (to confirm it’s working):

```bash
aws s3 ls
```

---

## 🧹 Optional: Clean Up Installer Files

```bash
rm -rf awscliv2.zip aws/
```

---

## 🧩 Useful Commands

| Description | Command |
|--------------|----------|
| Check AWS CLI version | `aws --version` |
| View all configured profiles | `cat ~/.aws/credentials` |
| Change default region | `aws configure set region us-east-1` |

---

## ✅ Uninstall AWS CLI

To uninstall later if needed:

```bash
sudo /usr/local/aws-cli/v2/current/dist/aws uninstall
```

---

## 🎯 Done!

Your AWS CLI is now installed and ready to use on Ubuntu 🎉
