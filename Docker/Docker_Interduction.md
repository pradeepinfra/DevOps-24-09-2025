# 🐳 Docker End-to-End Guide (Installation + Commands + Usage)

This README explains **Docker from scratch**:
✅ What Docker is  
✅ Why to use Docker  
✅ When to use Docker  
✅ Docker installation steps (Linux + Windows)  
✅ Most used Docker commands with "when to use"  
✅ Dockerfile + Build + Run  
✅ Volumes + Network + Docker Compose  
✅ Troubleshooting commands  

---

## ✅ 1) What is Docker?

Docker is a **containerization platform** that helps you package:
- Application code
- Runtime (Python/Java/Node)
- Libraries & dependencies
- OS-level requirements

into a single unit called an **Image** and run it as a **Container**.

✅ Benefit: **Same app works in Laptop / Server / Cloud**

---

## ✅ 2) Why Docker?

Docker solves the common problem:

> "Works in my laptop but not in production"

### Without Docker:
- Different OS versions
- Dependency mismatch
- Missing libraries
- Manual setup issues

### With Docker:
✅ Portable  
✅ Fast deployments  
✅ Consistent environment  
✅ Easy scaling  
✅ Useful in CI/CD pipelines  

---

## ✅ 3) When to Use Docker?

✅ Use Docker when:
- You want same environment in Dev/Test/Prod
- You have microservices architecture
- You want faster deployments
- You need CI/CD pipeline automation (Jenkins/GitHub Actions)
- You want easy setup for new developers
- You want app portability across AWS/Servers/Cloud

❌ Don’t use Docker when:
- Heavy GUI applications
- Extremely high-performance bare-metal requirement
- Very small scripts (not needed)

---

# ✅ 4) Docker Installation Steps

---

## ✅ 4.1 Install Docker on Ubuntu (Recommended)

### Step 1: Update packages
```bash
sudo apt update -y
```

### Step 2: Install Docker
```bash
sudo apt install docker.io -y
```

### Step 3: Start Docker service
```bash
sudo systemctl start docker
sudo systemctl enable docker
```

### Step 4: Verify Docker
```bash
docker --version
docker info
```

### Step 5: Allow running docker without sudo (Optional but recommended)
```bash
sudo usermod -aG docker $USER
newgrp docker
```

✅ Now run:
```bash
docker ps
```

---

## ✅ 4.2 Install Docker on Amazon Linux 2 / RHEL / CentOS

### Step 1: Update system
```bash
sudo yum update -y
```

### Step 2: Install Docker
```bash
sudo yum install docker -y
```

### Step 3: Start and enable Docker
```bash
sudo systemctl start docker
sudo systemctl enable docker
```

### Step 4: Add user permission (Optional)
```bash
sudo usermod -aG docker ec2-user
newgrp docker
```

### Step 5: Verify
```bash
docker --version
docker ps
```

---

## ✅ 4.3 Install Docker on Windows (Docker Desktop)

1. Download Docker Desktop
2. Enable WSL2 backend
3. Restart system
4. Verify using PowerShell:
```powershell
docker --version
docker ps
```

---

# ✅ 5) Most Used Docker Commands (With When to Use)

---

## ✅ 5.1 Check Docker status/version
```bash
docker --version
docker info
```
✅ Use when:
- Verify Docker installed
- Check Docker engine running

---

## ✅ 5.2 Download Image from DockerHub
```bash
docker pull nginx
docker pull ubuntu:22.04
```
✅ Use when:
- You want prebuilt apps like nginx/mysql/redis

---

## ✅ 5.3 List Images
```bash
docker images
```
✅ Use when:
- Check what images are available locally

---

## ✅ 5.4 Run a Container
```bash
docker run nginx
```
✅ Use when:
- Start a container quickly for testing

---

## ✅ 5.5 Run container in background (Detached mode)
```bash
docker run -d nginx
```
✅ Use when:
- Run web servers/apps in background

---

## ✅ 5.6 Port Mapping (Access in browser)
```bash
docker run -d -p 8080:80 nginx
```
✅ Use when:
- You want to expose container app outside

📌 Format:
**HostPort : ContainerPort**

---

## ✅ 5.7 Name the container (Recommended)
```bash
docker run -d --name mynginx -p 8080:80 nginx
```
✅ Use when:
- Easy manage by name instead of ID

---

## ✅ 5.8 List Running Containers
```bash
docker ps
```
✅ Use when:
- Check active containers

---

## ✅ 5.9 List All Containers
```bash
docker ps -a
```
✅ Use when:
- See stopped + running containers

---

## ✅ 5.10 Stop Container
```bash
docker stop mynginx
```
✅ Use when:
- Stop running service safely

---

## ✅ 5.11 Start Container Again
```bash
docker start mynginx
```
✅ Use when:
- Start stopped container without new creation

---

## ✅ 5.12 Restart Container
```bash
docker restart mynginx
```
✅ Use when:
- Restart service quickly after changes

---

## ✅ 5.13 Remove Container
```bash
docker rm mynginx
```
✅ Use when:
- Delete unused/stopped containers

If running:
```bash
docker stop mynginx && docker rm mynginx
```

---

## ✅ 5.14 Remove Image
```bash
docker rmi nginx
```
✅ Use when:
- Free disk space
- Remove unused versions

---

## ✅ 5.15 View Logs (Debugging)
```bash
docker logs mynginx
docker logs -f mynginx
```
✅ Use when:
- Check container errors
- `-f` follow/live logs

---

## ✅ 5.16 Go Inside Container (Troubleshooting)
```bash
docker exec -it mynginx bash
```
If bash not present:
```bash
docker exec -it mynginx sh
```
✅ Use when:
- Verify config/files inside container

---

## ✅ 5.17 Inspect Container (IP, mounts, details)
```bash
docker inspect mynginx
```
✅ Use when:
- Find IP address
- Debug volume/network mapping

---

## ✅ 5.18 Resource Usage Monitoring
```bash
docker stats
```
✅ Use when:
- Check CPU/RAM usage for containers

---

# ✅ 6) Build Your Own Image (Dockerfile)

---

## ✅ 6.1 Example Dockerfile (Python Flask)
Create `Dockerfile`:
```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

Build image:
```bash
docker build -t flask-demo:v1 .
```

Run container:
```bash
docker run -d -p 5000:5000 flask-demo:v1
```

---

# ✅ 7) Docker Volumes (Persistence)

Containers are temporary.
If container deleted → data lost.

### Example with volume:
```bash
docker run -d -v mydata:/var/lib/mysql mysql:8
```
✅ Use when:
- Database containers (MySQL/Postgres)
- Persistent app files needed

---

# ✅ 8) Docker Networking

Check networks:
```bash
docker network ls
```

Create custom network:
```bash
docker network create mynet
```

Run container in network:
```bash
docker run -d --name web --network mynet nginx
```

✅ Use when:
- App container needs to talk with DB container
- Microservices environment

---

# ✅ 9) Docker Compose (Multi-container)

Create `docker-compose.yml`:
```yaml
version: "3.8"
services:
  web:
    build: .
    ports:
      - "5000:5000"
```

Run:
```bash
docker compose up -d
```

Stop:
```bash
docker compose down
```

✅ Use when:
- Multiple services needed
- Easy local environment setup

---

# ✅ 10) Registry: Push Image to DockerHub

Login:
```bash
docker login
```

Tag image:
```bash
docker tag flask-demo:v1 yourname/flask-demo:v1
```

Push:
```bash
docker push yourname/flask-demo:v1
```

✅ Use when:
- Deploying images to servers/cloud

---

# ✅ 11) Cleanup Docker (Free Disk Space)

Remove unused containers/images:
```bash
docker system prune -a
```

✅ Use when:
- Docker consuming too much disk space

⚠️ Warning: Removes unused images/containers.

---

# ✅ 12) Troubleshooting Commands

Check docker service:
```bash
sudo systemctl status docker
```

Restart docker:
```bash
sudo systemctl restart docker
```

Common issue: Permission denied
Fix:
```bash
sudo usermod -aG docker $USER
newgrp docker
```

---

# ✅ Quick Docker Cheat Sheet

```bash
docker pull nginx
docker images
docker build -t myapp:v1 .
docker run -d -p 8080:80 --name myapp myapp:v1
docker ps
docker logs -f myapp
docker exec -it myapp bash
docker stop myapp
docker rm myapp
docker rmi myapp:v1
docker compose up -d
docker system prune -a
```

---

✅ Done! Now you have full Docker end-to-end notes in one README.md 🎉
