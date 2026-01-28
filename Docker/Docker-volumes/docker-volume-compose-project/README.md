# Docker Volumes with Docker Compose – Step by Step 🚀

This project shows **how Docker Volumes work using Docker Compose**.
We do NOT run containers manually.

---

## 1️⃣ What is a Docker Volume?

A Docker Volume is a storage space managed by Docker.
It stores data **outside containers**, so data is not lost.

---

## 2️⃣ Why We Use Volumes

- Containers are temporary
- Volumes keep data permanent
- Used for databases, logs, uploads

---

## 3️⃣ Project Structure

docker-volume-compose/
├── docker-compose.yml
└── README.md

---

## 4️⃣ docker-compose.yml Explained

```yaml
version: "3.8"

services:
  app:
    image: ubuntu
    container_name: volume_demo_app
    command: sleep infinity
    volumes:
      - mydata:/data

volumes:
  mydata:
```

Explanation:
- ubuntu → base image
- sleep infinity → keep container running
- mydata:/data → volume attached
- volumes section → creates Docker volume

---

## 5️⃣ Start the Project

```bash
docker compose up -d
```

---

## 6️⃣ Create Data Inside Volume

```bash
docker exec -it volume_demo_app bash
cd /data
echo "Hello Docker Volume" > test.txt
ls
exit
```

---

## 7️⃣ Stop Containers

```bash
docker compose down
```

Volume is NOT deleted.

---

## 8️⃣ Start Again & Verify

```bash
docker compose up -d
docker exec -it volume_demo_app bash
cd /data
ls
cat test.txt
```

Data is still there 🎉

---

## ✅ Summary

Docker Volumes keep data safe even when containers are removed.
Docker Compose makes everything clean and repeatable.
