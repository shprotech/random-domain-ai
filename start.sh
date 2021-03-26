#!/bin/bash

APP_NAME="docker.domain_app"
docker build -t ${APP_NAME} .
docker run -d -p 80:80 --name=${APP_NAME} -v $PWD:/var/www/domain_app $APP_NAME
