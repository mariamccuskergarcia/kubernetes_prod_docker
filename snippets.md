## Docker

# building image
docker build -t mmg_image .

# running image to check it works on docker desktop
docker run -it -p 3000:8080 mmg_image

# deploying image to registry to then be used in Kubernetes

docker build . -t <image_name:version>
docker push <image_name:version>

## Kubernetes

kubectl apply -f prod.yaml --force=true --grace-period=0

minikube tunnel

# Rollout update

kubectl rollout restart deployment mmg-again --namespace mmg-again

kubectl rollout status deployment mmg-again --namespace mmg-again 


<!-- kubectl run mmg-pod --image=localhost:5000/mmg_ex5 --port 8080 --namespace=mmg-namespace

curl http://localhost:5000/v2/_catalog

kubectl create namespace ducktales-dev

kubectl port-forward service/ducktales-dev 8100:8100  --namespace=ducktales-dev
curl http://localhost:8101 -->