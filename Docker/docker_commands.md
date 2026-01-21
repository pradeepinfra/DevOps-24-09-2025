# 🐳 Docker Commands (Basic → Advanced) with Examples

This guide covers Docker commands from beginner to advanced level with practical examples.

---

## ✅ 1) Check Docker Installation

```bash
docker --version
docker info
docker version
```

---

## ✅ 2) Images (Pull / List / Remove)

### Pull an Image
```bash
docker pull ubuntu
docker pull nginx
docker pull python:3.10-slim
```

### List Images
```bash
docker images
```

### Remove Image
```bash
docker rmi nginx
docker rmi <image_id>
```

### Remove All Unused Images
```bash
docker image prune
docker image prune -a
```

---

## ✅ 3) Containers (Run / Start / Stop / Remove)

### Run a Container (Foreground)
```bash
docker run ubuntu
```

### Run Interactive Container
```bash
docker run -it ubuntu bash
```

### Run in Background (Detached Mode)
```bash
docker run -d nginx
```

### List Running Containers
```bash
docker ps
```

### List All Containers
```bash
docker ps -a
```

### Stop Container
```bash
docker stop <container_id>
```

### Start Container
```bash
docker start <container_id>
```

### Restart Container
```bash
docker restart <container_id>
```

### Remove Container
```bash
docker rm <container_id>
```

### Remove Container Forcefully (Running Container)
```bash
docker rm -f <container_id>
```

---

## ✅ 4) Container Naming

```bash
docker run -d --name mynginx nginx
docker ps
```

---

## ✅ 5) Port Mapping (Important)

### Run nginx on port 8080
```bash
docker run -d -p 8080:80 --name web nginx
```

Open in browser:

- Local: http://localhost:8080
- AWS EC2: http://<EC2-PUBLIC-IP>:8080

---

## ✅ 6) Container Logs

```bash
docker logs <container_id>
docker logs -f <container_id>
```

---

## ✅ 7) Execute Commands Inside Running Container (Exec)

### Enter into container shell
```bash
docker exec -it <container_id> bash
```

Example:
```bash
docker exec -it web bash
```

### Run one command inside container
```bash
docker exec web ls -l
```

---

## ✅ 8) Copy Files (Host ↔ Container)

### Copy file from Host → Container
```bash
docker cp index.html web:/usr/share/nginx/html/index.html
```

### Copy file from Container → Host
```bash
docker cp web:/etc/nginx/nginx.conf .
```

---

## ✅ 9) Inspect Container Details

```bash
docker inspect <container_id>
docker inspect web
```

---

## ✅ 10) Resource Usage (CPU / RAM / Network)

```bash
docker stats
```

---

## ✅ 11) Container Networking Basics

### List Docker Networks
```bash
docker network ls
```

### Create New Network
```bash
docker network create mynet
```

### Run container in a custom network
```bash
docker run -d --name app1 --network mynet nginx
```

### Inspect Network
```bash
docker network inspect mynet
```

---

## ✅ 12) Volumes (Persistent Storage)

### List Volumes
```bash
docker volume ls
```

### Create Volume
```bash
docker volume create mydata
```

### Use Volume in Container
```bash
docker run -d --name nginx-vol -p 8081:80 \
  -v mydata:/usr/share/nginx/html \
  nginx
```

### Inspect Volume
```bash
docker volume inspect mydata
```

### Remove Volume
```bash
docker volume rm mydata
```

---

## ✅ 13) Bind Mount (Local Folder to Container)

Example (Mount local folder into container):
```bash
docker run -d --name nginx-bind -p 8082:80 \
  -v $(pwd):/usr/share/nginx/html \
  nginx
```

Now any file in your current folder will show in nginx.

---

## ✅ 14) Dockerfile (Build Your Own Image)

### Example Dockerfile (Python App)
Create `Dockerfile`:
```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install flask
EXPOSE 5000
CMD ["python", "app.py"]
```

Build image:
```bash
docker build -t mypythonapp .
```

Run container:
```bash
docker run -d -p 5000:5000 --name myapp mypythonapp
```

---

## ✅ 15) Tag & Push Image to DockerHub

Login:
```bash
docker login
```

Tag image:
```bash
docker tag mypythonapp <dockerhub_username>/mypythonapp:v1
```

Push:
```bash
docker push <dockerhub_username>/mypythonapp:v1
```

---

## ✅ 16) Docker Compose (Multi-container setup)

### Install check
```bash
docker compose version
```

### Example `docker-compose.yml`
```yaml
version: "3.8"
services:
  web:
    image: nginx
    ports:
      - "8080:80"

  redis:
    image: redis
```

Start services:
```bash
docker compose up -d
```

Check running:
```bash
docker compose ps
```

Logs:
```bash
docker compose logs -f
```

Stop:
```bash
docker compose down
```

---

## ✅ 17) Advanced Cleanups

### Remove stopped containers
```bash
docker container prune
```

### Remove all unused (containers/images/networks)
```bash
docker system prune
```

### Remove everything unused (Including Images)
```bash
docker system prune -a
```

### Remove unused volumes
```bash
docker volume prune
```

---

## ✅ 18) Useful Debug Commands

### Check port mapping
```bash
docker port web
```

### Check processes inside container
```bash
docker top web
```

### Check container environment variables
```bash
docker exec web env
```

### See Docker disk usage
```bash
docker system df
```

---

# ✅ Quick Demo (AWS / Local)

Run nginx:
```bash
docker run -d --name demo-nginx -p 8080:80 nginx
```

Test inside server:
```bash
curl http://localhost:8080
```

Browser open:
```bash
http://<EC2-PUBLIC-IP>:8080
```

Stop & remove:
```bash
docker stop demo-nginx
docker rm demo-nginx
```

---

# ✅ Summary

✅ Basic: pull, run, ps, stop, rm  
✅ Intermediate: exec, logs, inspect, ports, stats  
✅ Advanced: volumes, networks, dockerfile build, compose, prune  

---
