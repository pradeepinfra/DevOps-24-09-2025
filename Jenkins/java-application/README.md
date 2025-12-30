# 🌱 Java CI/CD Beginner Project – Step by Step Guide

This project demonstrates a **very simple Java application** and explains **each step clearly** to build, test, containerize, and automate it using Maven, Docker, and Jenkins.

---

## 📌 Step 1: Create Project Folder

```bash
mkdir java-application
cd java-application
```

**Why:**  
Creates a root folder to keep Java, Docker, and Jenkins files together.

---

## 📌 Step 2: Create Maven Directory Structure

```bash
mkdir -p src/main/java/com/message
mkdir -p src/test/java/com/message
```

**Why:**  
Maven expects this standard structure for source code and tests.

---

## 📂 Project Structure

```
java-application/
│── src/
│   ├── main/java/com/message/MessageApp.java
│   └── test/java/com/message/MessageAppTest.java
│── pom.xml
│── Dockerfile
│── docker-compose.yml
│── Jenkinsfile
│── README.md
```

---

## 📌 Step 3: Java Application

**MessageApp.java**
```java
package com.message;

public class MessageApp {

    public static String getMessage() {
        return "Learning DevOps step by step makes life easier!";
    }

    public static void main(String[] args) {
        System.out.println(getMessage());
    }
}
```

**Why:**  
Simple logic makes CI/CD easy to understand.

---

## 📌 Step 4: Unit Test

**MessageAppTest.java**
```java
package com.message;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class MessageAppTest {

    @Test
    void verifyMessage() {
        assertEquals(
            "Learning DevOps step by step makes life easier!",
            MessageApp.getMessage()
        );
    }
}
```

**Why:**  
Ensures code correctness before Docker/Jenkins steps.

---

## 📌 Step 5: Maven Build File

**pom.xml**
```xml
<project xmlns="http://maven.apache.org/POM/4.0.0">
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.message</groupId>
  <artifactId>java-application</artifactId>
  <version>1.0</version>

  <properties>
    <maven.compiler.source>17</maven.compiler.source>
    <maven.compiler.target>17</maven.compiler.target>
  </properties>

  <dependencies>
    <dependency>
      <groupId>org.junit.jupiter</groupId>
      <artifactId>junit-jupiter</artifactId>
      <version>5.9.3</version>
      <scope>test</scope>
    </dependency>
  </dependencies>
</project>
```

---

## 📌 Step 6: Build & Test

```bash
mvn clean package
```

**Result:**  
Creates JAR file in `target/` directory.

---

## 📌 Step 7: Run Locally

```bash
java -jar target/java-application-1.0.jar
```

---

## 📌 Step 8: Dockerfile

```dockerfile
FROM eclipse-temurin:17-jre-alpine
WORKDIR /app
COPY target/java-application-1.0.jar app.jar
CMD ["java","-jar","app.jar"]
```

---

## 📌 Step 9: Docker Run

```bash
docker build -t java-message-app .
docker run --rm java-message-app
```

---

## 📌 Step 10: Docker Compose

```yaml
version: '3'
services:
  message-app:
    image: java-message-app
```

```bash
docker-compose up --build
docker-compose down
```

---

## 📌 Step 11: Jenkins Pipeline

```groovy
pipeline {
    agent any
    stages {
        stage('Build') {
            steps { sh 'mvn clean package' }
        }
        stage('Docker') {
            steps { sh 'docker build -t java-message-app .' }
        }
        stage('Run') {
            steps { sh 'docker run --rm java-message-app' }
        }
    }
}
```

---

## 📌 Step 12: GitHub Push

```bash
git init
git add .
git commit -m "Java CI/CD beginner project"
git branch -M main
git remote add origin <repo-url>
git push -u origin main
```

---

## 📜 License
MIT License