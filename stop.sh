#!/bin/bash

#jupyterhubがスポーンしたコンテナを停止＆削除
docker rm --force `docker ps --all -f name=jupyter- -q`
#jupyterhubコンテナとネットワークを削除
docker compose down
