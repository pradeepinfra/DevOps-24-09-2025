# 🌱 Java CI/CD Pipeline with Jenkins, Maven & Docker (Beginner Friendly)

This project demonstrates a **complete end-to-end CI/CD pipeline** using **Git, Maven, Jenkins, and Docker**.
Each step is explained clearly so even **absolute beginners** can understand **what happens and why**.

---

## 📌 What This Project Does

- Cleans Jenkins workspace
- Pulls Java code from GitHub
- Builds and tests the application using Maven
- Packages the Java application
- Builds a Docker image
- Tags and pushes the image to Docker Hub
- Cleans workspace after pipeline completion

---

## 📂 Project Structure

```
DevOps-24-09-2025/
└── Jenkins/
    └── java-application/
        ├── src/
        │   ├── main/java/com/message/MessageApp.java
        │   └── test/java/com/message/MessageAppTest.java
        ├── pom.xml
        ├── Dockerfile
        ├── Jenkinsfile
        └── README.md
```

---

## 🧹 Stage 1: Clean Workspace (Before Build)

```groovy
cleanWs()
```

Removes old files from previous builds to avoid conflicts.

---

## 📥 Stage 2: Git Checkout

```groovy
git branch: 'main',
    url: 'https://github.com/pradeepinfra/DevOps-24-09-2025.git'
```

Pulls latest code from GitHub.

---

## 🧱 Stage 3: Maven Clean

```bash
mvn clean
```

Deletes old compiled files.

---

## 🛠 Stage 4: Compile

```bash
mvn compile
```

Compiles Java source code.

---

## 🧪 Stage 5: Test

```bash
mvn test
```

Runs unit tests.

---

## 📦 Stage 6: Package

```bash
mvn package
```

Creates deployable JAR file.

---

## 🐳 Stage 7: Docker Build

```bash
docker build -t java-jenkins-docker:latest .
```

Builds Docker image.

---

## 🏷 Stage 8: Docker Tag

```bash
docker tag java-jenkins-docker:latest infravyom/java-app:v1
```

Tags image for Docker Hub.

---

## 🔐 Stage 9: Docker Login (Learning Purpose)

```bash
docker login -u infravyom -p ******
```

Authenticates Docker Hub.

---

## 🚀 Stage 10: Docker Push

```bash
docker push infravyom/java-app:v1
```

Pushes image to Docker Hub.

---

## 🧹 Post Action: Clean Workspace (After Build)

```groovy
post {
    always {
        cleanWs()
    }
}
```

Cleans workspace after build.

---

## ✅ Complete CI/CD Flow

```
Clean Workspace
→ Git Checkout
→ Maven Clean
→ Compile
→ Test
→ Package
→ Docker Build
→ Docker Tag
→ Docker Login
→ Docker Push
→ Clean Workspace
```

---

## 🎯 Real-World Best Practices

- Store Jenkinsfile in Git
- Store artifacts in Nexus/S3
- Store Docker images in Docker Hub/ECR
- Jenkins should be rebuildable anytime

---

