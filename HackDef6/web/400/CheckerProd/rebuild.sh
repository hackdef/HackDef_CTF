#This script will deleta all data and rebuld the doker images

sudo docker stop checkerprod-db-1
sudo docker rm checkerprod-db-1
sudo docker stop checkerprod-app-1
sudo docker rm checkerprod-app-1
sudo docker-compose up -d --no-deps --build
