# ToDo List Application

This **ToDo List Application** is a web application designed to make task management simple and efficient. It is built using the following technologies:

- **Frontend:** React.js  
- **Backend:** Flask  
- **Database:** MongoDB  

The application supports two deployment methods:
1. **Docker Containers**
2. **Kubernetes Clusters**

---

## Running the Application Using Docker Containers　(is maintained now)

1. Navigate to the `setup` directory in your project.
2. Execute the `setup.sh` script:
   ```bash
   ./setup.sh
   ```
3. Once the setup is complete, open your browser and navigate to **[http://localhost:3000](http://localhost:3000)** to access the application.

---

## Running the Application Using Kubernetes (only way to use now)

1. Ensure that Kubernetes is enabled and running in your environment. You can use one of the following methods to set up Kubernetes easily:
   - [Minikube](https://minikube.sigs.k8s.io/docs/start/)
   - [Kubernetes on Docker Desktop](https://docs.docker.com/desktop/kubernetes/)

2. Navigate to the `k8s` folder in your project and execute the provided setup file:
   ```bash
   ./setup.sh
   ```

3. Verify that all Pods are running correctly using the following command:
   ```bash
   kubectl get pods
   ```
   Ensure that the `STATUS` of all Pods is `Running`.

4. Once confirmed, open your browser and navigate to **[http://localhost](http://localhost)** to access the application.

---

Feel free to explore, add, edit, and manage your tasks effortlessly with this ToDo List Application!
