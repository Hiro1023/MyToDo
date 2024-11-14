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
pwd
cd ..
pwd
ls
echo "============================"
echo "Apply all .yml file in k8s..."
echo "============================"


kubectl apply -f k8s

