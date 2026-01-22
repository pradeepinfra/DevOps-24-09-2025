# ✅ Docker Complete Guide🚀

## 📌 What is Docker?
Docker is a **containerization platform** used to:
✅ Build applications  
✅ Package app + dependencies  
✅ Run anywhere (Laptop / Server / Cloud)  

### 🔥 Why Docker?
Without Docker:
- Works in my laptop ✅  
- Fails in server ❌  
- Different dependency versions ❌  

With Docker:
- Same environment everywhere ✅  
- Fast deployment ✅  
- Easy scaling ✅  

---

## ✅ Docker Key Terms

### ✅ Image
- Image = **Template / Blueprint**
- It contains:
  - OS base
  - Runtime (Java/Python/Node)
  - Libraries
  - App code

Example images:
- `nginx`
- `ubuntu`
- `python:3.10-slim`

---

### ✅ Container
- Container = **Running instance of Image**
- Containers are lightweight + fast

Example:
```bash
docker run nginx
```

---

## ✅ Docker Architecture (Important)

Docker follows **Client → Engine → Images/Containers → Registry** model.

### 🏗 Docker Architecture Diagram
```
+--------------------+
|   Docker Client    |
| (docker commands)  |
+---------+----------+
          |
          | REST API
          v
+-----------------------------+
|       Docker Engine         |
|   (Docker Daemon / dockerd) |
+-------------+---------------+
              |
     +--------+--------+
     |                 |
     v                 v
+-----------+     +-----------+
|  Images   |     | Containers|
+-----------+     +-----------+
     |
     v
+----------------------+
|  Docker Registry     |
| (DockerHub / ECR)    |
+----------------------+
```

---

## ✅ Docker Components Explained

### 1️⃣ Docker Client
You run commands like:
```bash
docker build
docker run
docker ps
docker pull
```

---

### 2️⃣ Docker Engine (Docker Daemon)
Runs in background:
✅ Builds images  
✅ Runs containers  
✅ Manages networking + storage  

---

### 3️⃣ Docker Registry
Where images are stored:
✅ DockerHub  
✅ AWS ECR  
✅ Azure ACR  

Example:
```bash
docker pull nginx
docker push myrepo/myimage:1.0
```

---

## ✅ Docker Image Architecture (Layers)

Docker images are built in **layers**:

```
Layer 4: App Code
Layer 3: Dependencies (pip/npm)
Layer 2: Runtime (Python/Node)
Layer 1: Base OS (Ubuntu/Alpine)
```

### ✅ Benefits of Layers
✅ Faster builds (cache reuse)  
✅ Saves storage  
✅ Efficient updates  

---

## ✅ Docker Installation (Ubuntu)

### Step 1: Update packages
```bash
sudo apt update
```

### Step 2: Install Docker
```bash
sudo apt install docker.io -y
```

### Step 3: Start Docker
```bash
sudo systemctl start docker
sudo systemctl enable docker
```

### Step 4: Check Docker version
```bash
docker --version
```

### Step 5: Run Docker without sudo (optional)
```bash
sudo usermod -aG docker $USER
newgrp docker
```

---

# ✅ Docker Commands (Basic → Advanced)

## ✅ 1. Check Docker
```bash
docker --version
docker info
```

---

## ✅ 2. Download an Image
```bash
docker pull nginx
docker pull ubuntu
```

---

## ✅ 3. List Images
```bash
docker images
```

---

## ✅ 4. Run a Container
### Run nginx container (foreground)
```bash
docker run nginx
```

### Run nginx container in background
```bash
docker run -d nginx
```

✅ `-d` means **Detached mode (runs in background)**

---

## ✅ 5. Run with Custom Container Name
```bash
docker run -d --name web nginx
```

---

## ✅ 6. Port Mapping
Run nginx and open in browser:
```bash
docker run -d -p 8080:80 nginx
```

✅ Access: `http://localhost:8080`

---

## ✅ 7. List Running Containers
```bash
docker ps
```

### List all containers (including stopped)
```bash
docker ps -a
```

---

## ✅ 8. Stop / Start Container
```bash
docker stop web
docker start web
```

---

## ✅ 9. Remove Container
```bash
docker rm web
```

Force remove (even running):
```bash
docker rm -f web
```

---

## ✅ 10. Remove Images
```bash
docker rmi nginx
```

Remove all unused images:
```bash
docker image prune -a
```

---

## ✅ 11. Logs (Important)
```bash
docker logs web
```

Follow logs live:
```bash
docker logs -f web
```

---

## ✅ 12. Enter into Container (Shell Access)

### For Ubuntu containers
```bash
docker exec -it myubuntu bash
```

### For Alpine containers
```bash
docker exec -it myalpine sh
```

---

## ✅ 13. Run Ubuntu Container
```bash
docker run -it ubuntu bash
```

---

## ✅ 14. Volumes (Persistent Storage)

### Create volume
```bash
docker volume create mydata
```

### Run container with volume
```bash
docker run -d --name db -v mydata:/var/lib/mysql mysql
```

---

## ✅ 15. Bind Mount (Local folder)
```bash
docker run -it -v $(pwd):/app ubuntu bash
```

---

## ✅ 16. Networks
List networks:
```bash
docker network ls
```

Create network:
```bash
docker network create mynet
```

Run container inside network:
```bash
docker run -d --name web --network mynet nginx
```

---

# ✅ Dockerfile (Build Your Own Image)

## ✅ Example: Python App Dockerfile

📌 Create file: `Dockerfile`
```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

---

## ✅ Build Image
```bash
docker build -t mypythonapp:1.0 .
```

---

## ✅ Run Container
```bash
docker run -d --name pythonapp -p 5000:5000 mypythonapp:1.0
```

---

# ✅ Docker Compose (Run Multiple Containers)

📌 Create file: `docker-compose.yml`
```yaml
version: "3.8"

services:
  web:
    image: nginx
    ports:
      - "8080:80"
```

Run compose:
```bash
docker compose up -d
```

Stop compose:
```bash
docker compose down
```

---

# ✅ Real-Time Docker Use Cases

✅ Deploy web apps (React / Node / Python)  
✅ Microservices architecture  
✅ CI/CD Jenkins pipelines  
✅ Run databases (MySQL, Postgres)  
✅ AWS deployment (ECS / EKS / EC2)  

---

# ✅ Quick Interview Notes

### ✅ Image vs Container
| Image | Container |
|------|-----------|
| Blueprint | Running instance |
| Stored | Executes |
| Read-only layers | Writable layer |

### ✅ What is `-d` in docker run?
✅ Runs container in background (detached mode)

---

# ✅ Best Practice Commands (Daily Use)
```bash
docker ps
docker ps -a
docker images
docker logs -f <container>
docker exec -it <container> bash
docker rm -f <container>
docker rmi <image>
```

---

✅ **Done 🎉**
