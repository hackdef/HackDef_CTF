#!/bin/bash
sudo docker stop $(sudo docker ps | grep "node-crypto-300"|awk '{print $1}')
