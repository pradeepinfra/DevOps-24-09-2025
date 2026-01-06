# 🚀 Jenkins Agent Setup Using SSH Authentication (Step by Step)

This guide explains how to set up a **Jenkins Agent (Worker Node)** and connect it securely to the **Jenkins Master** using **SSH key-based authentication**.

---

## 🧠 What is a Jenkins Agent?

In Jenkins, an **agent** is a machine that executes build jobs and pipelines.  
The **master** schedules jobs, and the **agent** performs the actual work.

### Why use agents?
- Distribute build load
- Run jobs on different environments
- Improve performance and scalability

---

## 📌 Prerequisites

- Jenkins Master installed and running
- Agent server (Ubuntu / EC2 instance)
- SSH access between master and agent
- Port **22** open in Security Group
- Java installed on agent

---

## 🔐 STEP 1: Generate SSH Key Pair on Jenkins Master

### Why?
SSH keys allow Jenkins to connect securely to the agent **without passwords**.

```bash
cd ~/.ssh
ssh-keygen -t ed25519
```

Files created:
- `id_ed25519` → Private key (used by Jenkins)
- `id_ed25519.pub` → Public key (copied to agent)

---

## ⚙️ STEP 2: Add Jenkins Agent Node in Jenkins UI

- Manage Jenkins → Nodes & Clouds → New Node
- Node name: `worker-node`
- Type: Permanent Agent

---

## ⚙️ STEP 3: Configure Agent Settings

| Field | Value |
|-----|------|
| Remote root directory | /home/ubuntu |
| Labels | worker-node |
| Launch method | Launch agents via SSH |
| Host | Agent Public IP |

---

## 🔑 STEP 4: Add SSH Credentials in Jenkins

- Kind: SSH Username with private key
- Username: ubuntu
- Private Key: Paste `id_ed25519`
- ID: worker-node-ssh

---

## 🖥️ STEP 5: Configure Agent Server

```bash
mkdir -p ~/.ssh
vim ~/.ssh/authorized_keys
```

Paste `id_ed25519.pub`

---

## 🔒 STEP 6: Fix Permissions

```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
```

---

## ☕ STEP 7: Install Java

```bash
sudo apt update
sudo apt install -y openjdk-21-jdk
```

---

## 🔐 STEP 8: Open Port 22 in Security Group

Allow SSH (22) from Jenkins Master IP.

---

## ▶️ STEP 9: Launch Agent

- Manage Jenkins → Nodes → Launch Agent
- Status should show Connected

---

## 🧪 STEP 10: Test with Pipeline

```groovy
pipeline {
    agent { label 'worker-node' }
    stages {
        stage('Test') {
            steps {
                sh 'hostname'
                sh 'java -version'
            }
        }
    }
}
```

---

## 🧾 Summary

Jenkins agent configured successfully using SSH authentication.
