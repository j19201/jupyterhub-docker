#!/bin/bash

source ./.env
docker-compose up -d --build
sleep 3
docker-compose exec jupyterhub docker image pull $JUPYTER_DOCKER_IMAGE
echo jupyterhubが起動しました
