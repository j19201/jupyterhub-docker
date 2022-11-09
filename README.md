# jupyterhub-docker
jupyterhubの環境をdockerで動かせるようにしたもの

## 起動方法
```
docker build -t jupyter .
docker run --privileged --name jupyterhub -p 8000:8000 jupyter:latest
```
