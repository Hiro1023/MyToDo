#!/bin/bash

set -e 

# Go to root
cd ..
cd ..

echo "============================"
echo "Creating Docker images for Kubernetes"
echo "============================"

# Build docker image
build_image() {
    local service=$1
    echo "Building Docker image for $service..."
    cd "$service"
    docker build -t "todo-app-$service:latest" .
    cd ..
}

build_image "backend"
build_image "frontend"

cd k8s # Go into k8s directory

echo "============================"
echo "Applying Nginx Ingress Controller..."
echo "============================"

kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/cloud/deploy.yaml

echo "============================"
echo "Applying Kubernetes YAML configurations..."
echo "============================"

# apply all .yaml files in components
kubectl apply -f components

echo "============================"
echo "Restarting frontend and backend pods..."
echo "============================"

# restart deployments 
kubectl rollout restart deployment backend frontend

echo "============================"
echo "Deployment completed successfully!"
echo "============================"

# remove all docker images named as none
cd setup
chmod +x remove_none_images.sh
./remove_none_images.sh

