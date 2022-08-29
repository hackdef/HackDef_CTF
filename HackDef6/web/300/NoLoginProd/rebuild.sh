#This script will deleta all data and rebuld the doker images

sudo docker stop mongo
sudo docker rm mongo
sudo docker stop nologin
sudo docker rm nologin
sudo docker-compose up -d --no-deps --build
