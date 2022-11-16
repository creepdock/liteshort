# Liteshort
A multi-arch (arm64 and amd64) docker image for liteshort

docker-compose.yml :

```yml
version: '3'
services:
    liteshort:
        restart: unless-stopped
        container_name: arewedown
        image: ghcr.io/creepdock/liteshort:latest
        ports:
            - 8080:8080
        volumes:
            - ./data/:/data/
```

don't forgot to add config.yml inside data folder
