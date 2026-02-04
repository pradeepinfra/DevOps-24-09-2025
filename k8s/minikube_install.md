# Minikube Installation Guide on Ubuntu

This guide explains **system requirements** and **step-by-step
installation** of Minikube on Ubuntu for learning Kubernetes.

------------------------------------------------------------------------

## System Requirements

Minimum recommended configuration:

-   OS: Ubuntu 20.04 / 22.04 or later
-   RAM: Minimum 4 GB (8 GB recommended)
-   CPU: 2 cores or more
-   Disk Space: 20 GB free space
-   Internet connection required
-   Docker installed
-   kubectl installed

Optional but recommended: - Virtualization enabled in BIOS (VT-x or SVM)

Check virtualization support:

``` bash
egrep -c '(vmx|svm)' /proc/cpuinfo
```

If output is greater than 0, virtualization is enabled.

------------------------------------------------------------------------

## Installation Steps

### Step 1 --- Update System

``` bash
sudo apt update && sudo apt upgrade -y
```

------------------------------------------------------------------------

### Step 2 --- Install Docker

Install Docker container runtime:

``` bash
sudo apt install docker.io -y
```

Enable Docker service:

``` bash
sudo systemctl enable docker
sudo systemctl start docker
```

Add current user to Docker group:

``` bash
sudo usermod -aG docker $USER
```

Logout and login again after running the command.

Verify Docker:

``` bash
docker --version
```

------------------------------------------------------------------------

### Step 3 --- Install kubectl

Install kubectl using snap:

``` bash
sudo snap install kubectl --classic
```

Verify installation:

``` bash
kubectl version --client
```

------------------------------------------------------------------------

### Step 4 --- Install Minikube

Download Minikube binary:

``` bash
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
```

Install Minikube:

``` bash
sudo install minikube-linux-amd64 /usr/local/bin/minikube
```

Verify installation:

``` bash
minikube version
```

------------------------------------------------------------------------

### Step 5 --- Start Minikube Cluster

Start cluster using Docker driver:

``` bash
minikube start --driver=docker
```

Check cluster nodes:

``` bash
kubectl get nodes
```

------------------------------------------------------------------------

## Useful Minikube Commands

Start cluster:

``` bash
minikube start
```

Stop cluster:

``` bash
minikube stop
```

Delete cluster:

``` bash
minikube delete
```

Open dashboard:

``` bash
minikube dashboard
```

Check cluster status:

``` bash
minikube status
```

------------------------------------------------------------------------

## Troubleshooting Tips

If virtualization shows 0:

-   Enable virtualization in BIOS OR
-   Use Docker driver instead of VM driver.

If Docker permission error occurs:

``` bash
sudo usermod -aG docker $USER
```

Then logout/login.

------------------------------------------------------------------------

## Conclusion

Minikube provides an easy way to run Kubernetes locally for learning and
testing without cloud infrastructure.

You are now ready to deploy applications in Kubernetes.
