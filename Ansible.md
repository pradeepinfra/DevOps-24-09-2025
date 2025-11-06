
# 🧠 Ansible Learning Guide

This document provides a complete overview of Ansible concepts and setup steps — perfect for learning or project setup on AWS Ubuntu.

---

## 1️⃣ Ansible Introduction

Ansible is an **open-source automation tool** used for:

- Configuration management (installing software, managing files)
- Application deployment
- Orchestration (managing multiple servers)
- Infrastructure provisioning

✅ It uses **YAML playbooks** to define automation.  
✅ It is **agentless** – connects over SSH (no client software needed on target systems).

---

## 2️⃣ Why Ansible is Stateless?

Ansible is **stateless** because it doesn’t store system state information.  
Every time you run a playbook, it checks and ensures that the desired configuration is applied.

🧠 **Idempotency:** Running a play multiple times gives the same end result.

---

## 3️⃣ Ansible Project Structure

A clean project structure helps organize your automation logically:

```
ansible-project/
├── inventory/                # Target servers
│   └── hosts.ini
├── playbooks/
│   └── site.yml              # Main playbook
├── roles/                    # Reusable roles
│   └── webserver/
│       ├── tasks/main.yml
│       ├── handlers/main.yml
│       ├── templates/
│       └── vars/main.yml
├── group_vars/               # Common variables
│   └── all.yml
└── ansible.cfg               # Config file
```

---

## 4️⃣ Ansible & SSH Key Management for Secure Connection

Ansible connects securely using **SSH keys**.

- No need for passwords
- Secure and encrypted communication

Example command:

```bash
ansible all -m ping --key-file ~/.ssh/id_rsa
```

To distribute keys automatically:

```yaml
- name: Copy SSH key
  authorized_key:
    user: ubuntu
    state: present
    key: "{{ lookup('file', '~/.ssh/id_rsa.pub') }}"
```

---

## 5️⃣ YAML and Ansible

Ansible uses **YAML (Yet Another Markup Language)** for writing playbooks.

Example:

```yaml
- name: Install Nginx
  hosts: web
  become: yes
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
```

---

## 6️⃣ Ansible Handlers

Handlers are special tasks that only run when notified.

Example:

```yaml
tasks:
  - name: Copy nginx config
    template:
      src: nginx.conf.j2
      dest: /etc/nginx/nginx.conf
    notify: Restart nginx

handlers:
  - name: Restart nginx
    service:
      name: nginx
      state: restarted
```

---

## 7️⃣ Ansible Variables

Variables store values (like usernames, ports, etc.) for reusability.

```yaml
vars:
  app_port: 8080

tasks:
  - name: Configure app
    template:
      src: app.conf.j2
      dest: /etc/app.conf
```

---

## 8️⃣ Ansible Environment Variables

Used to pass environment-level data to playbooks or commands.

```yaml
- name: Print environment variable
  shell: echo $HOME
  environment:
    PATH: /usr/local/bin
```

---

## 9️⃣ Ansible Conditional

Allows tasks to run only when specific conditions are true.

```yaml
- name: Install nginx on Ubuntu
  apt:
    name: nginx
    state: present
  when: ansible_os_family == "Debian"
```

---

## 🔟 Ansible Roles and Tasks

Roles make automation modular by grouping **tasks, handlers, templates, and variables**.

```
roles/
  webserver/
    tasks/main.yml
    handlers/main.yml
    templates/
    vars/main.yml
```

Example task file:

```yaml
- name: Install Nginx
  apt:
    name: nginx
    state: present
```

---

## 11️⃣ Jinja2 Templates

Jinja2 is used to dynamically generate configuration files.

Template (`nginx.conf.j2`):

```
server {
  listen {{ app_port }};
  server_name {{ inventory_hostname }};
}
```

Playbook example:

```yaml
vars:
  app_port: 8080
```

Result: Ansible fills variables when creating the real file.

---

## ⚙️ Ansible Installation on AWS Ubuntu

### 1. Connect to EC2
```bash
ssh -i "aws-key.pem" ubuntu@<your-ec2-public-ip>
```

### 2. Update system
```bash
sudo apt update -y && sudo apt upgrade -y
```

### 3. Add repository and install
```bash
sudo apt install software-properties-common -y
sudo add-apt-repository --yes --update ppa:ansible/ansible
sudo apt install ansible -y
```

### 4. Verify installation
```bash
ansible --version
```

### 5. Create project structure
```bash
mkdir ~/ansible-project && cd ~/ansible-project
nano inventory
```

Example inventory:

```
[web]
192.168.1.10 ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/id_rsa
```

### 6. Test connection
```bash
ansible all -i inventory -m ping
```

### 7. Create and run playbook
```yaml
- name: Install Nginx
  hosts: web
  become: yes
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
```

Run it:
```bash
ansible-playbook -i inventory install_nginx.yml
```

---

## ✅ Summary

| Step | Description | Command |
|------|--------------|----------|
| 1 | Update Ubuntu | `sudo apt update && sudo apt upgrade -y` |
| 2 | Install Ansible | `sudo apt install ansible -y` |
| 3 | Verify install | `ansible --version` |
| 4 | Create inventory | `nano inventory` |
| 5 | Test connection | `ansible all -i inventory -m ping` |
| 6 | Run playbook | `ansible-playbook -i inventory install_nginx.yml` |

---

**Author:** AWS & DevOps Learning Notes  by pradeep
**Tool:** Ansible 🧩  
**Platform:** AWS Ubuntu EC2  
