
# Jenkins – Complete Guide (CI/CD, Plugins, Architecture)

---

## 1. What is CI/CD?

CI/CD is a DevOps practice that automates software delivery.

### CI – Continuous Integration
- Developers push code frequently to Git
- Jenkins automatically builds and tests the code
- Bugs are detected early

### CD – Continuous Delivery / Deployment
- **Continuous Delivery**: Code is ready for production (manual approval)
- **Continuous Deployment**: Code is deployed automatically

---

## 2. What is Jenkins?

Jenkins is an **open-source automation tool** used to implement CI/CD pipelines.

### Jenkins is used to:
- Pull code from Git repositories
- Build applications
- Run automated tests
- Deploy applications to servers or cloud

---

## 3. Jenkins Overview (How it Works)

1. Developer pushes code to Git
2. Git webhook triggers Jenkins
3. Jenkins pulls code
4. Jenkins builds the application
5. Jenkins runs tests
6. Jenkins deploys the application

---

## 4. Jenkins Installation (Ubuntu / Linux)

### Step 1: Update system
```bash
sudo apt update
```

### Step 2: Install Java (Required for Jenkins)
```bash
sudo apt install openjdk-17-jdk -y
java -version
```

### Step 3: Add Jenkins Repository
```bash
curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | sudo tee /usr/share/keyrings/jenkins-keyring.asc > /dev/null
```

```bash
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian-stable binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null
```

### Step 4: Install Jenkins
```bash
sudo apt update
sudo apt install jenkins -y
```

### Step 5: Start Jenkins
```bash
sudo systemctl start jenkins
sudo systemctl enable jenkins
sudo systemctl status jenkins
```

### Step 6: Access Jenkins UI
```
http://<server-ip>:8080
```

### Step 7: Unlock Jenkins
```bash
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```

---

## 5. Jenkins Plugins

Plugins extend Jenkins functionality.

### Commonly Used Jenkins Plugins

1. **Git Plugin**
   - Connects Jenkins with GitHub/GitLab

2. **Pipeline Plugin**
   - Enables Jenkinsfile (CI/CD as code)

3. **GitHub Integration Plugin**
   - Triggers builds using webhooks

4. **Credentials Plugin**
   - Stores passwords, SSH keys, tokens securely

5. **Docker Plugin**
   - Builds Docker images and runs containers

6. **Kubernetes Plugin**
   - Runs Jenkins agents as Kubernetes pods

7. **Blue Ocean Plugin**
   - Modern UI for pipelines

8. **Email Extension Plugin**
   - Sends email notifications

---

## 6. Jenkins Architecture (Master & Node)

### Jenkins Master (Controller)
- Provides Jenkins UI
- Manages jobs and pipelines
- Schedules builds
- Manages plugins and credentials

⚠️ Heavy builds should not run on master

---

### Jenkins Node (Agent)
- Executes build jobs
- Runs tests and deployments
- Can be Linux, Windows, Docker, Kubernetes, EC2

---

## 7. Difference Between Jenkins Master and Node

| Feature | Master | Node |
|------|--------|------|
| UI Access | Yes | No |
| Job Scheduling | Yes | No |
| Build Execution | Limited | Yes |
| Scalability | No | Yes |
| Purpose | Manage Jenkins | Execute jobs |

---

## 8. Simple CI/CD Pipeline Example

```groovy
pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Building application'
      }
    }
    stage('Test') {
      steps {
        echo 'Running tests'
      }
    }
    stage('Deploy') {
      steps {
        echo 'Deploying application'
      }
    }
  }
}
```

---

## 9. Interview Ready Answer

**Q: What is Jenkins?**  
Jenkins is an open-source CI/CD automation tool used to build, test, and deploy applications.

**Q: What are plugins?**  
Plugins extend Jenkins functionality like Git, Docker, and Kubernetes integration.

**Q: Difference between Master and Node?**  
Master manages jobs and scheduling, while nodes execute the actual builds.

---

## 10. Summary
- Jenkins automates CI/CD
- Plugins add extra features
- Master manages, nodes execute
- Used widely in DevOps projects
