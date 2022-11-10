FROM python:3.9.15

#必要なパッケージをインストール
RUN apt-get update && apt-get -y install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release \
    npm

#dockerインストール
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null
RUN apt-get update && apt-get -y install docker-ce docker-ce-cli containerd.io docker-compose-plugin
COPY setting/etc/docker/daemon.json /etc/docker/daemon.json

#jupyter環境構築
RUN npm install -g configurable-http-proxy
RUN pip install --upgrade pip && \
    pip install setuptools_rust jupyterhub dockerspawner && \
    pip install --upgrade notebook && \
    pip install --upgrade jupyterlab

#テストユーザ追加
RUN adduser --disabled-password --gecos "" test && \
    echo test:test | chpasswd

#設定ファイルをコピー
COPY setting/opt/jupyterhub_config.py /opt/jupyterhub_config.py

#起動に必要なファイルをコピー
COPY setting/opt/start_jupyter.sh /opt/start_jupyter.sh
COPY setting/etc/systemd/system/jupyterhub.service /etc/systemd/system/jupyterhub.service
RUN ln -s /etc/systemd/system/jupyterhub.service /etc/systemd/system/multi-user.target.wants/jupyterhub.service
COPY .env /opt/.env

CMD ["/sbin/init"]
