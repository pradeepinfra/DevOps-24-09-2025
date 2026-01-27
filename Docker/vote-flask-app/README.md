# ✅ Vote Flask App (Dockerized) 🗳️🐳

This is a simple **Voting Web Application** built using **Flask (Python)** and packaged using **Docker**.

Users can vote:
✅ YES  
✅ NO  
And view results instantly.

---

## 📁 Project Structure

```
vote-flask-app/
├── app.py
├── requirements.txt
├── Dockerfile
├── templates/
│   └── index.html
└── README.md
```

---

# ✅ What is Dockerfile?

A **Dockerfile** is a **text file** that contains step-by-step instructions to build a **Docker Image**.

✅ Think like this:

- **Dockerfile** = Recipe 📜  
- **Docker Image** = Packed App (Ready to Ship) 📦  
- **Docker Container** = Running App 🚀  

---

# ✅ Why we use Dockerfile? (Real-time Usecase)

In real-time projects, Dockerfile is used to solve:

✅ "Works on my laptop" problem  
✅ Same environment in all servers  
✅ Easy deployment to EC2 / ECS / EKS  
✅ Faster onboarding for new engineers  
✅ CI/CD automation in Jenkins/GitHub Actions

### 🔥 Real-time example
Developer machine:
- Python 3.10 ✅
- Flask installed ✅

Server machine:
- Python missing ❌
- Flask missing ❌
- App fails ❌

✅ With Dockerfile, everything is packed inside the image and works anywhere.

---

# ✅ How Dockerfile is used in this project?

This project uses Dockerfile to:

✅ Download base image `python:3.10-slim`  
✅ Install Flask dependency from `requirements.txt`  
✅ Copy application code into container  
✅ Run the Flask app automatically

---

# ✅ Dockerfile used for this project

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

### ✅ Dockerfile Line by Line Explanation
- `FROM python:3.10-slim` → gives OS + Python
- `WORKDIR /app` → sets working directory inside container
- `COPY requirements.txt .` → copy dependency file
- `RUN pip install ...` → install Flask inside container
- `COPY . .` → copy full project into container
- `EXPOSE 5000` → app will run on port 5000
- `CMD ["python", "app.py"]` → starts app when container runs

---

# ✅ Build Docker Image

Run this inside the project folder:

```bash
docker build -t vote-flask-app .
```

✅ Output: Docker image will be created.

Check:
```bash
docker images
```

---

# ✅ Run Docker Container

```bash
docker run -d -p 5000:5000 --name voteapp vote-flask-app
```

Check running container:
```bash
docker ps
```

---

# ✅ Access the Application

✅ Open in browser:

Local:
```
http://localhost:5000
```

Vote and see results ✅

---

# ✅ Reset Votes

Open:
```
http://localhost:5000/reset
```

---

# ✅ Useful DevOps Commands

### View container logs
```bash
docker logs voteapp
```

### Follow logs
```bash
docker logs -f voteapp
```

### Stop container
```bash
docker stop voteapp
```

### Remove container
```bash
docker rm -f voteapp
```

---

# ✅ Deploy to AWS EC2 (Quick Steps)

### 1) Install Docker on EC2 (Amazon Linux)
```bash
sudo yum update -y
sudo yum install docker -y
sudo service docker start
sudo usermod -aG docker ec2-user
newgrp docker
```

### 2) Build and run
```bash
docker build -t vote-flask-app .
docker run -d -p 5000:5000 --name voteapp vote-flask-app
```

### 3) Open port in Security Group
Inbound Rules:
✅ Custom TCP → Port **5000** → Source `0.0.0.0/0`

### 4) Access from browser
```
http://<EC2-PUBLIC-IP>:5000
```

---

# ⚠️ Note (Important - Real Time)
This project stores votes in **memory**, so if container restarts votes become **0** again.

✅ In real projects, we use DB like:
- Redis
- MySQL
- PostgreSQL

---

# ✅ Push Docker Image to Docker Hub

```bash
docker login
docker tag vote-flask-app pradeepdevops/vote-flask-app:1.0
docker push pradeepdevops/vote-flask-app:1.0
```

Run anywhere:
```bash
docker run -d -p 5000:5000 pradeepdevops/vote-flask-app:1.0
```

---

# ⚠️ Note
Votes reset on container restart. Use DB in real projects.
