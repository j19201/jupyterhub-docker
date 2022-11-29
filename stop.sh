#!/bin/bash

#jupyterhubがスポーンしたコンテナを停止＆削除
docker rm --force `docker ps --all -f name=jupyterhub- -q`
#moodle関係のコンテナを削除
docker rm --force `docker ps --all -f name=docker-moodle- -q`
#jupyterhubコンテナとネットワークを削除
docker compose --profile with-moodle down
docker compose down