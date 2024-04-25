# Docker

- Creating the image
```
docker build -f \<Dockerfile\> -t \<IMAGE NAME> .
docker build -t company_app_img .
```

- Running it
```
docker run -it -p 3000:8080 company_app_img
```

- Deploy image to registry
```
docker build . -t localhost:5000/company_app_img:v1
docker push localhost:5000/company_app_img:v1
```

# Kubernetes
```
kubectl apply -f .\prod.yaml --force=true --grace-period=0

minikube tunnel
```

# Rollout update
```
kubectl rollout restart deployment company-app-prod --namespace=company-app-prod

kubectl rollout status deployment company-app-prod --namespace=company-app-prod 
```