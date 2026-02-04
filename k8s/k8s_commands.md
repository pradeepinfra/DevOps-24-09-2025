# Kubernetes Commands with Explanation (kubectl Cheat Sheet)

This document provides commonly used Kubernetes commands along with
simple explanations for learning and daily DevOps usage.

------------------------------------------------------------------------

# 1. Cluster Commands

## Check cluster information

``` bash
kubectl cluster-info
```

Shows Kubernetes control plane and cluster services information.

## List nodes

``` bash
kubectl get nodes
```

Displays worker nodes available in the cluster.

## Node details

``` bash
kubectl describe node <node-name>
```

Shows CPU, memory, pods running, and node status.

------------------------------------------------------------------------

# 2. Namespace Commands

## List namespaces

``` bash
kubectl get ns
```

Shows all namespaces.

## Create namespace

``` bash
kubectl create ns dev
```

Creates a new namespace named dev.

## Delete namespace

``` bash
kubectl delete ns dev
```

Removes namespace and its resources.

------------------------------------------------------------------------

# 3. Pod Commands

## List pods

``` bash
kubectl get pods
```

Displays running pods in current namespace.

## Pods in all namespaces

``` bash
kubectl get pods -A
```

Lists pods across cluster.

## Pod details

``` bash
kubectl describe pod <pod-name>
```

Shows events, status, and configuration.

## Pod logs

``` bash
kubectl logs <pod-name>
```

Shows application logs.

## Live logs

``` bash
kubectl logs -f <pod-name>
```

Streams logs in real time.

## Enter pod container

``` bash
kubectl exec -it <pod-name> -- bash
```

Access container shell.

## Delete pod

``` bash
kubectl delete pod <pod-name>
```

Removes pod.

------------------------------------------------------------------------

# 4. Deployment Commands

## List deployments

``` bash
kubectl get deployments
```

Displays application deployments.

## Create deployment

``` bash
kubectl create deployment nginx --image=nginx
```

Creates deployment using nginx image.

## Deployment details

``` bash
kubectl describe deployment nginx
```

Shows deployment configuration.

## Delete deployment

``` bash
kubectl delete deployment nginx
```

Removes deployment and pods.

------------------------------------------------------------------------

# 5. Scaling Applications

## Scale deployment

``` bash
kubectl scale deployment nginx --replicas=3
```

Increases or decreases pod count.

------------------------------------------------------------------------

# 6. Service Commands

## List services

``` bash
kubectl get svc
```

Shows exposed services.

## Expose deployment

``` bash
kubectl expose deployment nginx --type=NodePort --port=80
```

Creates service to access app.

## Service details

``` bash
kubectl describe svc nginx
```

Shows service ports and endpoints.

------------------------------------------------------------------------

# 7. YAML Operations

## Create resources

``` bash
kubectl apply -f file.yaml
```

Creates or updates resources.

## Delete resources

``` bash
kubectl delete -f file.yaml
```

Removes resources defined in YAML.

------------------------------------------------------------------------

# 8. ConfigMaps & Secrets

## List ConfigMaps

``` bash
kubectl get configmap
```

Shows configuration objects.

## List Secrets

``` bash
kubectl get secrets
```

Shows stored sensitive data.

------------------------------------------------------------------------

# 9. Rollout & Updates

## Check rollout status

``` bash
kubectl rollout status deployment/nginx
```

Shows update progress.

## Rollback deployment

``` bash
kubectl rollout undo deployment/nginx
```

Reverts deployment version.

## Rollout history

``` bash
kubectl rollout history deployment/nginx
```

Shows previous versions.

------------------------------------------------------------------------

# 10. Debugging Commands

## Resource usage

``` bash
kubectl top pods
```

Shows CPU and memory usage.

## Events and errors

``` bash
kubectl describe pod <pod-name>
```

Useful for troubleshooting failures.

------------------------------------------------------------------------

# 11. File Copy Commands

## Copy file to pod

``` bash
kubectl cp file.txt pod:/tmp/
```

## Copy file from pod

``` bash
kubectl cp pod:/tmp/file.txt .
```

------------------------------------------------------------------------

# 12. Context Commands

## View contexts

``` bash
kubectl config get-contexts
```

## Switch context

``` bash
kubectl config use-context minikube
```

------------------------------------------------------------------------

# 13. Most Frequently Used Commands

Daily commands used in DevOps:

``` bash
kubectl get pods
kubectl get nodes
kubectl get svc
kubectl logs pod
kubectl exec -it pod -- bash
kubectl apply -f file.yaml
kubectl delete -f file.yaml
kubectl scale deployment app --replicas=3
```

------------------------------------------------------------------------

# Conclusion

kubectl is the main tool used to control Kubernetes clusters. Mastering
these commands allows deploying, scaling, debugging, and managing
applications efficiently in Kubernetes environments.
