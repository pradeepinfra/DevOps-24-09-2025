# Vote Flask App Deployment on Kubernetes (Minikube)

This guide explains how to deploy the Docker image
**infravyom/vote-flask-app:1.1** into a Kubernetes cluster using
Minikube.

------------------------------------------------------------------------

## Prerequisites

Make sure the following tools are installed:

-   Docker
-   Minikube
-   kubectl

Verify cluster status:

``` bash
minikube status
kubectl get nodes
```

------------------------------------------------------------------------

## Step 1 --- Create Deployment File

Create a file:

``` bash
nano vote-deployment.yaml
```

Add the following configuration:

``` yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: vote-app
spec:
  replicas: 2
  selector:
    matchLabels:
      app: vote-app
  template:
    metadata:
      labels:
        app: vote-app
    spec:
      containers:
      - name: vote-app
        image: infravyom/vote-flask-app:1.1
        ports:
        - containerPort: 80
```

Save and exit.

------------------------------------------------------------------------

## Step 2 --- Deploy Application

Apply deployment:

``` bash
kubectl apply -f vote-deployment.yaml
```

Check pods:

``` bash
kubectl get pods
```

------------------------------------------------------------------------

## Step 3 --- Expose Application

Create a service:

``` bash
kubectl expose deployment vote-app --type=NodePort --port=80
```

Check service details:

``` bash
kubectl get svc
```

------------------------------------------------------------------------

## Step 4 --- Access Application

Open service in browser:

``` bash
minikube service vote-app
```

Or manually:

``` bash
minikube ip
```

Open in browser:

    http://<minikube-ip>:<nodeport>

------------------------------------------------------------------------

## Useful Commands

Scale application:

``` bash
kubectl scale deployment vote-app --replicas=4
```

View pods:

``` bash
kubectl get pods -o wide
```

Delete deployment:

``` bash
kubectl delete deployment vote-app
```

Delete service:

``` bash
kubectl delete svc vote-app
```

------------------------------------------------------------------------

## Architecture Flow

User → Service → Pods → Container

Deployment manages replicas and ensures application availability.

------------------------------------------------------------------------

## Summary

-   Docker image is pulled from Docker Hub.
-   Deployment creates pods.
-   Service exposes the application.
-   Minikube runs Kubernetes locally.

------------------------------------------------------------------------

Happy Learning Kubernetes 🚀

