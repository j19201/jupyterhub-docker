# jupyterhub-docker
jupyterhubの環境をdockerで動かせるようにしたもの（Privileged不使用）

## 使用方法

### 起動
```
./start.sh
```

### 停止
```
./stop.sh
```

### ボリュームの削除
```
docker volume rm `docker volume ls -q|grep jupyterhub-user`
```
