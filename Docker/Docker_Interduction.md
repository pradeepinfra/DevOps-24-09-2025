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

# ✅ Docker Volumes (Persistent Storage) — Notes & Commands

## 🔹 What is a Docker Volume?
A **Docker Volume** is Docker-managed storage used to **persist data** (save data permanently) outside the container lifecycle.

✅ Even if the container is deleted or recreated, the volume data remains safe.

---

## ✅ When to Use Docker Volumes in Real-Time Projects
Use volumes when your application needs **permanent data storage**:

### ✅ 1) Databases (Most Common)
- MySQL / PostgreSQL / MongoDB

📌 Example: store DB data permanently
```bash
docker run -d --name db -v mydata:/var/lib/mysql mysql
```

### ✅ 2) App Uploads
- User uploaded files (images, pdfs, documents)
```bash
docker run -d --name app -v uploads:/app/uploads myapp-image
```

### ✅ 3) Logs Storage
- Keep logs safe even if container restarts
```bash
docker run -d --name app -v applogs:/var/log/app myapp-image
```

### ✅ 4) Production Containers
- Containers restart often during deployments
- Volumes help keep your important data safe

---

# ✅ Most Used Docker Volume Commands

## ✅ 1) Create a Volume
```bash
docker volume create mydata
```

---

## ✅ 2) List Volumes
```bash
docker volume ls
```

---

## ✅ 3) Inspect a Volume (Find actual storage path)
```bash
docker volume inspect mydata
```

Example output includes:
- **Mountpoint**: `/var/lib/docker/volumes/mydata/_data`

---

## ✅ 4) Run a Container with Volume (MySQL Example)
```bash
docker run -d --name db -v mydata:/var/lib/mysql mysql
```

### 🔍 Explanation
| Part | Meaning |
|------|---------|
| `-d` | Run container in background |
| `--name db` | Container name = `db` |
| `-v mydata:/var/lib/mysql` | Attach volume `mydata` to MySQL data directory |
| `mysql` | MySQL image |

✅ Database data will be stored inside volume `mydata`

---

## ✅ 5) Simple Volume Test (Ubuntu Example)
### Step 1: Run Ubuntu with volume
```bash
docker run -it --name test1 -v mydata:/data ubuntu
```

### Step 2: Create a file inside container
```bash
echo "hello docker volume" > /data/file1.txt
exit
```

### Step 3: Remove the container
```bash
docker rm test1
```

### Step 4: Run new container using same volume
```bash
docker run -it --name test2 -v mydata:/data ubuntu
cat /data/file1.txt
```

✅ You will still see the file → volume data is persistent 🎉

---

## ✅ 6) Remove a Volume (⚠️ Deletes all data permanently)
```bash
docker volume rm mydata
```

---

# ⭐ Quick Interview Rule
✅ **Use Volumes for persistent data** (DB, uploads, logs, production)  
❌ **Don’t use Volumes for temporary data**

---

✅ End of Docker Volumes Notes ✅


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
