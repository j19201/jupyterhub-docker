# jupyterhub & moodle in docker
jupyterhub-lti-lti in moodleの環境をdockerで動かせるようにしたもの（Privileged不使用）
> **Warning**
> ホストマシンのdocker.sockをバインドマウントしているため、ホストのdocker環境に影響を与えます  

## 使用方法

### 起動

#### jupyterhubのみの起動
```
./start.sh
```

#### moodleとjupyterhub両方の起動
```
./start.sh --with-moodle
```
or
```
./start.sh -m
```

### 停止
```
./stop.sh
```

### moodle側の設定例
* ツールURL https://localhost:8000/hub/lti/launch
* コンシューマ鍵 .envファイルのLTI_CLIENT_KEY
* 共有秘密鍵 .envファイルのLTI_SHARED_SECRET

## 未実装要素
* Culler（接続の切れた docker コンテナを削除する）
* Ltictr_Proxy

## 参考ページ
[moodle+jupyterhub動作方法](https://www.nsl.tuis.ac.jp/xoops/modules/xpwiki/?Moodle%2BJupyterHub)  
[configファイルのベース](https://gitlab.nsl.tuis.ac.jp/iseki/lticontainerspawner/-/blob/main/etc/jupyterhub_docker_config.py)  
[moodle側の設定方法](https://qiita.com/t-kita/items/eabe79de57fb223d5300)
