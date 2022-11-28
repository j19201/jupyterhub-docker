#!/bin/bash

#jupyterhubがスポーンしたコンテナを停止＆削除
docker rm --force `docker ps --all -f name=jupyterhub- -q`
#jupyterhubコンテナとネットワークを削除
docker compose down
