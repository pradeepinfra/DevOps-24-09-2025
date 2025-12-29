# Jenkins Declarative Pipeline

## Overview

A **Declarative Pipeline** is a structured and simplified way to define CI/CD pipelines in Jenkins using a file called `Jenkinsfile`. It provides a clear, opinionated syntax that makes pipelines easy to read, write, and maintain.
S
Declarative Pipelines are recommended for most Jenkins use cases, especially for beginners and teams working on shared CI/CD workflows.

---

## Why Use Declarative Pipeline?

Declarative Pipeline is preferred because it:

* Uses clean and readable syntax
* Enforces a standard pipeline structure
* Reduces scripting complexity
* Is easier to maintain and debug
* Clearly visualizes stages in the Jenkins UI

---

## Basic Declarative Pipeline Example

```groovy
pipeline {
    agent any

    stages {
        stage("Build") {
            steps {
                sh 'echo "Building project..."'
            }
        }

        stage("Test") {
            steps {
                sh 'echo "Running tests..."'
            }
        }

        stage("Deploy") {
            steps {
                sh 'echo "Deploying application..."'
            }
        }
    }
}
```

---

## Explanation of Pipeline Sections

### pipeline

* Root block of a Declarative Pipeline
* Mandatory for every Declarative Jenkinsfile
* Defines the complete CI/CD workflow

### agent

* Specifies where the pipeline runs
* `agent any` allows Jenkins to run on any available node

### stages

* Groups all stages together
* Defines the flow of the pipeline

### stage

* Represents a single phase of the pipeline
* Common stages include Build, Test, and Deploy

### steps

* Contains actual commands executed by Jenkins
* Examples include shell commands, scripts, and build tools

---

## Key Characteristics

* Uses predefined directives such as `agent`, `stages`, and `steps`
* Validates pipeline syntax before execution
* Reduces errors by enforcing structure
* Suitable for most CI/CD automation needs

---

## Summary

Declarative Pipeline allows you to describe **what** your pipeline should do in a clean and structured format. Jenkins handles the execution details, making CI/CD pipelines easier to manage and scale.

---

**File:** `README.md`
