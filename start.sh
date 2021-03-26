#!/bin/bash

app="docker.domain_app"
docker build -t ${app} .
docker run -d -p 80:80 --name=${app} -v $PWD:/var/www/domain_app $app
