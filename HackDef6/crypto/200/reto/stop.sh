#!/bin/bash
sudo docker stop $(sudo docker ps | grep "node-crypto-200"|awk '{print $1}')
