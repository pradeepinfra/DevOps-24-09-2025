
# 🗳️ Docker Compose Vote App Project

## 📌 Project Overview
This is a **simple Voting Application** built to understand **Docker Compose** clearly and practically.

The application allows users to:
- Vote for **Python 🐍** or **Java ☕**
- Store votes in **Redis**
- View live voting results

This project demonstrates how **multiple containers** work together as **one application** using Docker Compose.

---

## 🏗️ Architecture

- **Vote Service** → Flask web app for voting
- **Result Service** → Flask web app for displaying results
- **Redis Service** → In-memory database to store votes

All services run in **separate containers** but communicate over a **Docker network**.

---

## 📁 Project Structure

```
vote-app/
│
├── docker-compose.yml     # Main Docker Compose file
│
├── vote/                  # Vote application
│   ├── app.py
│   └── Dockerfile
│
└── result/                # Result application
    ├── app.py
    └── Dockerfile
```

---

## 🐳 Docker Compose Explanation

### docker-compose.yml

```yaml
version: "3.8"

services:
  vote:
    build: ./vote
    ports:
      - "5000:5000"
    depends_on:
      - redis

  result:
    build: ./result
    ports:
      - "5001:5001"
    depends_on:
      - redis

  redis:
    image: redis:alpine
```

### Explanation:
- **version** → Docker Compose file format
- **services** → Defines all containers
- **vote** → Voting web application container
- **result** → Result web application container
- **redis** → Database container
- **build** → Builds image from Dockerfile
- **image** → Pulls image from Docker Hub
- **ports** → Exposes container ports to host
- **depends_on** → Ensures Redis starts first

---

## ▶️ How to Run the Project

### Prerequisites
- Docker installed
- Docker Compose installed

### Steps

```bash
docker compose up -d --build
```

---

## 🌐 Access the Application

- Vote App: http://localhost:5000
- Result App: http://localhost:5001

---

## 🔄 How Services Communicate

- Docker Compose creates a **default network**
- Services communicate using **service names**
- Both apps connect to Redis using hostname `redis`

No IP addresses required.

---

## 💡 Why Docker Compose is Used Here

- Run multiple containers with **one command**
- Easy service dependency management
- Clean and reusable configuration
- Perfect for learning, demos, and development

---

## 📌 Key Learning Outcomes

- Understanding Docker Compose
- Multi-container application setup
- Container networking
- Service dependencies
- Real-world DevOps project structure

---

## ✅ Conclusion

Docker Compose simplifies running multi-container applications.
This project is a clear example of how frontend, backend, and database services work together seamlessly.

---

🚀 Happy Learning!
