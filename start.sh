#!/bin/bash

source ./.env

help() {
    echo "使い方　./start.sh [引数]
    引数なし : jupyterhubのみを起動する
    -h --help : このヘルプを表示
    -m --with-moodle : moodleも同時に起動（起動まで時間がかかります）
    https://github.com/j19201/jupyterhub-docker/tree/include-moodle"
}
with-moodle(){
    echo "jupyterhubとmoodleを起動します"
    docker compose --profile with-moodle up -d --build
    docker image pull $JUPYTER_DOCKER_IMAGE
    echo "jupyterhub&moodleが起動しました
    moodleが使えるかどうかは
    docker compose logs moodle-php -f
    でご確認ください "
    exit 0 
}

#引数なしの場合
if [ $# = 0 ]; then
    echo "jupyterhubのみ起動します" 
    docker compose up -d --build
    docker image pull $JUPYTER_DOCKER_IMAGE
    echo "jupyterhubが起動しました"
    exit 0
fi

#引数を検知
while getopts ":hm-:" opt; do
    case "$opt" in
        -)
            case "${OPTARG}" in
                help)
                    help
                    ;;
                with-moodle)
                    with-moodle
                    ;;
            esac  
            ;;
        h)
            help
            ;;
        m)
            with-moodle
            ;;
    esac
done