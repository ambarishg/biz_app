sudo chmod 666 /var/run/docker.sock

az acr create --resource-group rg-openai-demo --name bizacr007 --sku Basic

az acr login -n bizacr007

docker tag bizapp:latest bizacr007.azurecr.io/bizapp:v1

docker push bizacr007.azurecr.io/bizapp:v1