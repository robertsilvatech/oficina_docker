# README.md

# Comandos

Deploy dev
```
docker compose -p dev -f docker-compose-common.yaml -f docker-compose-dev.yaml up -d
```

Deploy prod
```
docker compose -p prod -f docker-compose-common.yaml -f docker-compose-prod.yaml up -d
```