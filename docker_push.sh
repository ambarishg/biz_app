sudo chmod 666 /var/run/docker.sock

az acr create --resource-group rg-openai-demo --name misronacr --sku Basic

az acr login -n misronacr

docker tag bizapp:latest misronacr.azurecr.io/bizapp:v1

docker push misronacr.azurecr.io/bizapp:v1