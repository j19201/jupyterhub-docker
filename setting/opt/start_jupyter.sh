#!/bin/bash

source /opt/.env

#設定ファイルに書き込み
sed -i "1ic.DockerSpawner.image = \'`echo $JUPYTER_DOCKER_IMAGE`\'" /opt/jupyterhub_config.py
sed -i "1imy_ip_addr = \'`hostname -i`\'" /opt/jupyterhub_config.py

#起動
jupyterhub -f /opt/jupyterhub_config.py
