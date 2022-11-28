FROM php:8.0-rc-apache-buster

#moodle動作要件パッケージインストール＆設定
RUN apt update && apt -y install libzip-dev zip libpng-dev libicu-dev git netcat sudo
RUN docker-php-ext-install zip mysqli gd intl
RUN cp /usr/local/etc/php/php.ini-development /usr/local/etc/php/php.ini
RUN echo "max_input_vars = 5000" >> /usr/local/etc/php/php.ini
#moodleダウンロード＆ドキュメントルートに移動
RUN cd /var/www/html && git clone -b MOODLE_400_STABLE https://github.com/moodle/moodle.git && mv moodle/* . && rm -rf moodle
#lticontainerをインストール
RUN mkdir /var/www/html/mod/lticontainer
RUN git clone https://gitlab.nsl.tuis.ac.jp/iseki/mod_lticontainer.git /var/www/html/mod/lticontainer/
#パーミッション設定
RUN chown www-data.www-data /var && chown -R www-data.www-data /var/www
#dockerをインストール
RUN apt update && apt -y install ca-certificates curl gnupg lsb-release
RUN mkdir -p /etc/apt/keyrings
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg
RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null
RUN apt update && apt -y install docker-ce docker-ce-cli containerd.io docker-compose-plugin
#インストール用バッチファイルをコピー
COPY moodle/install.sh /var/www/html
RUN chmod 755 /var/www/html/install.sh
#デフォルトコマンド設定
CMD ["/var/www/html/install.sh"]
