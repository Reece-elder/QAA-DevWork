# Lesson

kubectl get pods -l environment=production

# Demo
`kubectl get ns` - Gets all Namespaces in the current k8s cluster
resources are created in default namespace without any config

Namespace can be created by command line or with a manifest
`kubectl create ns new-namespace`
```yaml
kind: Namespace
apiVersion: v1
metadata:
  name: development
  labels:
    name: development
```
Namespaces 

# Tutorial

Create new yaml
```yaml
kind: Namespace
apiVersion: v1
metadata:
  name: dev
  labels:
    name: dev
```
`kubectl apply -f namespace.yaml`

nginx manifest with the following
```yaml
apiVersion: v1
kind: Pod
metadata: 
  name: nginx
  labels:
    app: nginx
  namespace: dev
spec: 
  containers:
  - name: nginx
    image: nginx: alpine
```
Apply the manifest `kubectl apply -f nginx.yaml`
Delete the manifest `kubectl delete ns dev` (DELETES ALL RESOURCES ASSOCIATED WITH NAMESPACE)