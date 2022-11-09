#!/bin/bash

sed -i "1imy_ip_addr = \'`hostname -i`\'" /opt/jupyterhub_config.py
jupyterhub -f /opt/jupyterhub_config.py
