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
apiVersion: apps/v1          # Kubernetes API version for Deployment resource
kind: Deployment             # Resource type we are creating (Deployment)

metadata:
  name: vote-app             # Name of the deployment

spec:
  replicas: 2                # Number of pod copies to run

  selector:                  # How deployment finds pods it manages
    matchLabels:
      app: vote-app          # Must match pod labels below

  template:                  # Template used to create pods
    metadata:
      labels:
        app: vote-app        # Label applied to pods

    spec:
      containers:            # Container details inside pod
      - name: vote-app       # Container name
        image: infravyom/vote-flask-app:1.1  # Docker image from Docker Hub
        ports:
        - containerPort: 80  # Container listens on port 80
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

