# jupyterhub & moodle in docker
jupyterhub-lti in moodleの環境をdockerで動かせるようにしたもの（Privileged不使用）
> **Warning**
> ホストマシンのdocker.sockをバインドマウントしているため、ホストのdocker環境に影響を与えます  

## 使用方法

### 起動
```
./start.sh
```

### 停止
```
./stop.sh
```

## 未実装要素
* Culler（接続の切れた docker コンテナを削除する）
* Ltictr_Proxy

## 参考ページ
[moodle+jupyterhub動作方法](https://www.nsl.tuis.ac.jp/xoops/modules/xpwiki/?Moodle%2BJupyterHub)  
[configファイルのベース](https://gitlab.nsl.tuis.ac.jp/iseki/lticontainerspawner/-/blob/main/etc/jupyterhub_docker_config.py)  
[moodle側の設定方法](https://qiita.com/t-kita/items/eabe79de57fb223d5300)
