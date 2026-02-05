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

# Kubernetes Vote App Demo --- Step-by-Step Guide

This README provides a complete **step-by-step explanation** of
deploying and demonstrating an application on Kubernetes.

It is designed for: - Learning Kubernetes - Demo presentations -
Interviews - Hands-on practice

The demo covers:

-   Application deployment
-   Service exposure
-   Browser access
-   Pod scaling
-   Rolling updates
-   Self-healing
-   Autoscaling

------------------------------------------------------------------------

# Step 1 --- Architecture Overview

Application flow:

User Browser ↓ NodePort / Port Forward ↓ Kubernetes Service ↓ Deployment
↓ Pods ↓ Container (Flask App)

Kubernetes ensures application availability even if pods fail.

------------------------------------------------------------------------

# Step 2 --- Application Details

Application: Flask Vote App\
Docker Image: `infravyom/vote-flask-app:1.1`\
Application Port: **5000**

------------------------------------------------------------------------

# Step 3 --- Deployment YAML

Deployment creates and manages pods.

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
        - containerPort: 5000
        resources:
          requests:
            cpu: 100m
          limits:
            cpu: 200m
```

Deployment ensures pods are always running.

------------------------------------------------------------------------

# Step 4 --- Service YAML

Service exposes pods inside or outside cluster.

``` yaml
apiVersion: v1
kind: Service
metadata:
  name: vote-app-service
spec:
  type: NodePort
  selector:
    app: vote-app
  ports:
  - protocol: TCP
    port: 80
    targetPort: 5000
    nodePort: 30007
```

Traffic flow:

Browser → NodePort → Service → Pods

------------------------------------------------------------------------

# Step 5 --- Deploy Application

Apply resources:

``` bash
kubectl apply -f vote-app.yaml
kubectl apply -f vote-app-service.yaml
```

Verify:

``` bash
kubectl get pods
kubectl get svc
```

Pods must be **Running**.

------------------------------------------------------------------------

# Step 6 --- Access Application

Open browser:

    http://<SERVER-IP>:30007

Ensure firewall/security group allows port **30007**.

------------------------------------------------------------------------

# Step 7 --- Port Forward (Optional)

Alternative method:

``` bash
kubectl port-forward svc/vote-app-service 8090:80 --address 0.0.0.0
```

Access:

    http://SERVER-IP:8090

Run in background:

``` bash
nohup kubectl port-forward svc/vote-app-service 8090:80 --address 0.0.0.0 > pf.log 2>&1 &
```

------------------------------------------------------------------------

# Step 8 --- Scaling Demo

Increase replicas:

``` bash
kubectl scale deployment vote-app --replicas=4
```

Verify:

``` bash
kubectl get pods
```

Application continues running without downtime.

------------------------------------------------------------------------

# Step 9 --- Rolling Update Demo

Restart deployment:

``` bash
kubectl rollout restart deployment vote-app
```

Pods update gradually without affecting users.

------------------------------------------------------------------------

# Step 10 --- Self-Healing Demo

Delete a pod:

``` bash
kubectl delete pod <pod-name>
```

Watch recreation:

``` bash
kubectl get pods -w
```

Kubernetes automatically creates a new pod.

------------------------------------------------------------------------

# Step 11 --- Enable Metrics Server

Autoscaling requires metrics server.

``` bash
minikube addons enable metrics-server
```

Verify:

``` bash
kubectl top nodes
```

------------------------------------------------------------------------

# Step 12 --- Create Autoscaler

``` bash
kubectl autoscale deployment vote-app --cpu=20% --min=2 --max=6
```

Check:

``` bash
kubectl get hpa
```

------------------------------------------------------------------------

# Step 13 --- Generate Load

Create load generator:

``` bash
kubectl run -i --tty load-generator --rm --image=busybox -- /bin/sh
```

Inside container:

``` bash
while true; do wget -q -O- http://vote-app-service; done
```

Watch scaling:

``` bash
kubectl get hpa -w
kubectl get pods
```

Pods increase automatically.

------------------------------------------------------------------------

# Step 14 --- Stop Load

Stop load:

``` bash
kubectl delete pod load-generator
```

Pods scale down after a few minutes.

------------------------------------------------------------------------

# Step 15 --- Demo Explanation Points

You can explain:

• Deployment manages application pods\
• Service exposes application\
• Pods auto-recover on failure\
• Rolling updates avoid downtime\
• Autoscaling adjusts pods automatically

------------------------------------------------------------------------

# Step 16 --- Common Issues

## App not reachable

Check:

``` bash
kubectl get svc
kubectl get pods
```

## Autoscaling not working

Ensure CPU requests defined.

## Port-forward stops

Restart port-forward or use NodePort.

------------------------------------------------------------------------

# Step 17 --- Final Demo Flow

1.  Show pods running
2.  Access application
3.  Scale pods
4.  Delete pod
5.  Rolling restart
6.  Autoscaling demo

------------------------------------------------------------------------

# Conclusion

This demo proves Kubernetes provides:

-   Scalability
-   High availability
-   Automatic recovery
-   Zero-downtime deployment

