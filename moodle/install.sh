#!/bin/bash
#データベースが起動しているかどうかをチェック
echo "データベース待機中"
while ! nc -w 1 docker-moodle-mariadb 3306; do
    echo -n ".";
    sleep 1;
done

cd /var/www/html/ && sudo -u www-data php admin/cli/install.php \
--non-interactive \
--agree-license \
--allow-unstable \
--skip-database \
--lang=ja \
--wwwroot=http://localhost \
--dataroot=/var/www/moodledata \
--dbtype=mariadb \
--dbhost=docker-moodle-mariadb \
--dbport=3306 \
--dbname=moodle \
--dbuser=root \
--dbpass=moodle \
--fullname="mdl-docker" \
--shortname="mdl-docker" \
--adminuser=admin \
--adminpass=admin \
--adminemail=admin@example.com \
--supportemail=support@example.com

cd /var/www/html/ && sudo -u www-data php admin/cli/install_database.php \
--lang=ja \
--adminuser=admin \
--adminpass=admin \
--adminemail=admin@example.com \
--fullname="mdl-docker" \
--shortname="mdl-docker" \
--agree-license

#apache2起動
apache2-foreground
