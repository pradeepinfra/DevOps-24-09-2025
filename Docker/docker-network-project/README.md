# Docker Network Project (Web + Database)

This is a **simple Docker Network demo project**.

## 📌 What this project shows
- How Docker containers communicate using a **Docker network**
- How **service names** work instead of IP addresses
- Real-world DevOps style setup

## 🧱 Architecture
Web (Nginx)  --->  Database (MySQL)
Both containers are connected using a **bridge network**.

## 📁 Project Structure
```
docker-network-project/
├── docker-compose.yml
├── README.md
└── app/
    └── index.html
```

## 🐳 Docker Network Used
- Custom bridge network: `my-network`
- Containers communicate using service names

## ▶️ How to Run
```bash
docker-compose up -d
```

## 🌍 Access Application
Open browser:
```
http://localhost:8080
```

## 🔎 Verify Network
```bash
docker network ls
docker network inspect docker-network-project_my-network
```

## 🧠 Key Learning
- No hard-coded IPs
- Better security
- Easy service discovery
- Same concept used in Kubernetes

## ✅ Result
You will see:
Docker Network Working ✅
