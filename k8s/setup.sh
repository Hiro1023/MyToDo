#!/bin/bash

echo "============================"
echo "Create docker image for k8s"
echo "============================"

cd ../todo-app # into todo-app
cd backend
docker build -t todo-app-backend:latest .

cd ../frontend
docker build -t todo-app-frontend:latest .

cd ..
cd ..

echo "============================"
echo "Apply nginx controller..."
echo "============================"

kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/cloud/deploy.yaml




echo "============================"
echo "Apply all .yml file in k8s..."
echo "============================"

kubectl apply -f k8s

echo "============================"
echo "Restart forntend and backend pods..."
echo "============================"

kubectl rollout restart deployment backend frontend


