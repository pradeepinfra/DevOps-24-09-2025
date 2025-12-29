
# Jenkins Scripted Pipeline

## Overview
This repository explains **Jenkins Scripted Pipeline** in a very simple and beginner-friendly way.

Scripted Pipeline is written using **Groovy scripting** and provides **full control** over how your CI/CD pipeline behaves.

---

## What is Scripted Pipeline?
A Scripted Pipeline is a Jenkins pipeline written in Groovy code.  
It is powerful and flexible, but slightly harder to read compared to Declarative Pipeline.

### When to use Scripted Pipeline?
- When you need complex logic (if-else, loops)
- When you want custom functions
- When you need full control over pipeline execution

---

## Basic Scripted Pipeline Example

```groovy
node {
    stage('Build') {
        sh 'echo "Building project..."'
    }

    stage('Test') {
        sh 'echo "Running tests..."'
    }

    stage('Deploy') {
        sh 'echo "Deploying application..."'
    }
}
```

---

## Explanation

### node block
- Allocates a Jenkins agent
- Creates a workspace
- Executes all steps inside it

### stage block
- Divides pipeline into logical steps
- Helps visualize progress in Jenkins UI

### steps
- Actual commands that run
- Examples: sh, bat, Groovy logic

---

## Workspace Example using ws

```groovy
node {
    ws('custom-workspace') {
        stage('Build') {
            sh 'pwd'
            sh 'echo "Running inside custom workspace"'
        }
    }
}
```

### Why use ws?
- Keeps files organized
- Useful when multiple jobs run on same agent
- Avoids workspace conflicts

---

## Key Points
- Scripted Pipeline uses Groovy
- Very flexible and powerful
- Best for advanced pipelines
- Declarative Pipeline is easier for beginners

---

## Conclusion
Scripted Pipeline is ideal when you need advanced logic and customization in Jenkins CI/CD workflows.
