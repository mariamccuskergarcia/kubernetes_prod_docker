# Company APP run on Minikube

TIP: use the exercise 1 as starting point:
- https://dev.azure.com/kubrick-training/ce06/_git/ricos_kubernetes_ex_fastapi

In a GIT repo synced with the cloud
Use gitignore

With this app:
* Inventory app: https://dev.azure.com/kubrick-training/ce06/_git/ricos_fastapi_fresh_repo1?path=/code/fastapi_inventory_app.py

* Create an image (docker image)
* Create a kubernetes deployment that uses the image
* Local, using minikube
* Start with 1 pod, later scale to 3 replicas
* Deploy with LoadBalancer
* Use yaml files to deploy (use ducktales)
* Want to create a namespace just for this
* Make sure you run the dashboard so you have some visibility of the cluster
* Make a change to your python code >> apply it as rollout strategy

## Additional challenge:
* Find way to save json file in a folder/area where all pods can read/write from so that additions/removals work regardless of which pod acted on the request