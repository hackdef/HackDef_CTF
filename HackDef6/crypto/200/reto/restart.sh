#!/bin/bash
sudo docker stop $(sudo docker ps | grep "node-crypto-200"|awk '{print $1}')
sudo docker run -p 3002:5000 -d node-crypto-200
