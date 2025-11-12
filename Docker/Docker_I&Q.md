# 🐳 Docker Troubleshooting & Interview Q&A

This document covers **common Docker troubleshooting questions** with detailed explanations and examples.

---

## 🔹 77. Docker Container Exits Immediately — How to Troubleshoot?

### 🧠 Root Cause
- The container runs **a single process**, and when that process exits, the container stops.
- Example: `docker run ubuntu` exits immediately because there’s no running process.

### ✅ Fix
Run the container **interactively** or specify a process to keep it alive.

```bash
docker run -it ubuntu bash
```

Or use a process that keeps running:
```bash
docker run -d nginx
```

Use logs to check why it exited:
```bash
docker logs <container_id>
```

---

## 🔹 78. Purpose of EXPOSE in Dockerfile

### 🧠 Common Misconception
`EXPOSE` **does not publish** the port — it only **documents** which ports the container listens on.

### ✅ Example
```dockerfile
EXPOSE 8080
```
This tells others (and tools like Docker Compose) that the app listens on `8080`, but you must still **map ports manually** when running:

```bash
docker run -p 8080:8080 myapp
```

---

## 🔹 79. Port Not Accessible on localhost Even After Port Mapping

### 🧠 Possible Causes
- Application binds only to `127.0.0.1` inside container.
- Firewall or SELinux restrictions.
- Wrong port mapping.

### ✅ Fix
Ensure the app listens on all interfaces:

```bash
# Inside your app config or command
app.listen('0.0.0.0', 8080)
```

Run with proper mapping:
```bash
docker run -p 8080:8080 myapp
```

---

## 🔹 80. Data Lost When Container Restarts

### 🧠 Root Cause
Data inside containers is **ephemeral** — it’s removed when the container is deleted.

### ✅ Fix — Use Volumes

```bash
docker run -d -v /mydata:/data myapp
```
or in `docker-compose.yml`:
```yaml
volumes:
  - ./data:/data
```

---

## 🔹 81. Code Changes Not Reflected After Rebuild

### 🧠 Possible Causes
- Docker caching layers.
- You didn’t rebuild the image correctly.

### ✅ Fix
Force rebuild without cache:
```bash
docker build --no-cache -t myapp .
```

Or ensure your **COPY** instruction in Dockerfile is after dependency installation to avoid caching issues.

---

## 🔹 82. App Crashes with "Permission Denied" in Container

### 🧠 Causes
- File permissions or user mismatch.
- Trying to write to a directory with restricted access.

### ✅ Fix
Check user permissions:
```bash
ls -l /path/to/file
```
Run container as root (for debugging only):
```bash
docker run -u 0 myapp
```
Or fix file permissions in Dockerfile:
```dockerfile
RUN chmod -R 755 /app
```

---

## 🔹 83. Docker Host Running Out of Disk Space

### 🧠 Reason
Unused containers, images, and volumes take up space.

### ✅ Fix
Clean up unused resources:
```bash
docker system prune -a
docker volume prune
```

Check disk usage:
```bash
docker system df
```

---

## 🔹 84. How to Debug a Live Container

### ✅ Use `exec` to get inside the container:
```bash
docker exec -it <container_id> /bin/bash
```

Or inspect logs and environment:
```bash
docker logs <container_id>
docker inspect <container_id>
```

Use `docker top` to see running processes.

---

## 🔹 85. Which Container Registry Do You Use?

### ✅ Common Answers
- **Docker Hub**
- **AWS ECR**
- **Azure Container Registry**
- **Google Container Registry (GCR)**
- **Harbor (On-prem)**

Example of pushing an image:
```bash
docker tag myapp:latest myregistry.com/myapp:1.0
docker push myregistry.com/myapp:1.0
```

---

## 🔹 86. Difference Between CMD and ENTRYPOINT

| Feature | CMD | ENTRYPOINT |
|----------|-----|------------|
| Purpose | Default command | Main executable |
| Override | Can be overridden by user command | Harder to override |
| Usage | For default arguments | For enforcing a specific script |

### ✅ Example

```dockerfile
ENTRYPOINT ["python3", "app.py"]
CMD ["--help"]
```

If you run:
```bash
docker run myapp --version
```
It becomes:
```
python3 app.py --version
```

---

## 🔹 87. Common Docker Commands Used Daily

```bash
docker ps -a               # List containers
docker images              # List images
docker logs <id>           # Check logs
docker exec -it <id> bash  # Enter container
docker rm -f <id>          # Remove container
docker rmi <image>         # Remove image
docker compose up -d       # Start services
```

---

## 🔹 88. When Will You Forcefully Remove a Container and How?

When a container is **stuck, corrupted**, or **not stopping normally**.

### ✅ Command
```bash
docker rm -f <container_id>
```
This forcibly removes the container even if it’s still running.

---

### 🧩 Summary Table

| ID | Question | Key Concept |
|----|-----------|-------------|
| 77 | Container exits | Process lifecycle |
| 78 | EXPOSE | Documentation only |
| 79 | Port issue | Network binding |
| 80 | Data loss | Volumes |
| 81 | Code not updated | Build cache |
| 82 | Permission denied | File ownership |
| 83 | Disk cleanup | System prune |
| 84 | Debugging | `exec` & logs |
| 85 | Registries | ECR / Hub / GCR |
| 86 | CMD vs ENTRYPOINT | Execution control |
| 87 | Daily commands | Docker usage |
| 88 | Force remove | Troubleshooting |

---

💡 **Pro Tip:** Use Docker Compose and named volumes for consistent environments and persistent data.

