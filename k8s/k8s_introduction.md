# Kubernetes Architecture & Why We Use Minikube for Learning

## Kubernetes Architecture -- Simple Explanation

A Kubernetes cluster is mainly divided into two parts:

1.  Control Plane (Master Node)
2.  Worker Nodes

Think of it like:

-   Control Plane = Manager Office
-   Worker Nodes = Employees doing the work

------------------------------------------------------------------------

## 1. Control Plane (Master Node)

The control plane manages the entire cluster.

### Main Components

**API Server** - Entry point to Kubernetes. - All kubectl commands go
through it.

**Scheduler** - Decides which worker node runs a pod.

**Controller Manager** - Ensures desired state is maintained. -
Recreates pods if they fail.

**etcd** - Database storing cluster state and configuration.

------------------------------------------------------------------------

## 2. Worker Nodes

Worker nodes run applications.

### Components

**Kubelet** - Agent running on each node. - Communicates with control
plane. - Runs pods.

**Container Runtime** - Software used to run containers. - Examples:
containerd, Docker.

**Kube Proxy** - Handles networking and service communication.

------------------------------------------------------------------------

## Basic Workflow

1.  User deploys application using kubectl.
2.  API Server receives request.
3.  Scheduler selects worker node.
4.  Kubelet starts pods.
5.  Application becomes accessible.

------------------------------------------------------------------------

## Why We Use Minikube for Learning

### What is Minikube?

Minikube runs a full Kubernetes cluster locally on a single machine.

------------------------------------------------------------------------

### Advantages of Minikube

-   Easy to install
-   Runs locally on laptop or PC
-   No cloud cost
-   Perfect for practice
-   Same Kubernetes concepts as production

------------------------------------------------------------------------

### Without Minikube

You need: - Multiple servers - Networking setup - Cloud cost - Complex
setup

------------------------------------------------------------------------

### With Minikube

Run:

    minikube start

You instantly get a working Kubernetes cluster for learning.

------------------------------------------------------------------------

## Minikube vs Production Kubernetes

  Feature       Minikube   Production Kubernetes
  ------------- ---------- -----------------------
  Setup         Easy       Complex
  Cost          Free       Paid
  Nodes         Single     Multiple
  Purpose       Learning   Production
  Environment   Local      Cloud/Data Center

------------------------------------------------------------------------

## Suggested Learning Path

1.  Docker basics
2.  Minikube setup
3.  Pods & Deployments
4.  Services
5.  ConfigMaps & Secrets
6.  Helm
7.  Cloud Kubernetes (EKS, AKS, GKE)

------------------------------------------------------------------------

## Conclusion

Kubernetes manages containerized applications at scale.\
Minikube provides a simple way to learn Kubernetes locally before moving
to production environments.
