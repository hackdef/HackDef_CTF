#!/bin/bash
sudo docker stop $(sudo docker ps | grep "node-crypto-300"|awk '{print $1}')
sudo docker run -p 4004:5000 -d node-crypto-300
