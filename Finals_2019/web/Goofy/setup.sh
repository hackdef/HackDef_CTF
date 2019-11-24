#!/bin/bash

docker-compose up -d && docker exec -it goofy /bin/bash -c "apt-get update && apt-get install -y netcat && while true; do  echo -e '\nhackdef{C39A45ED1AA5974406C673BB527B760D}\nDescarga este archivo: http://70.37.70.47/archs/66838a357eb27/Datos_Bancarios' | nc -l 127.0.0.1 -p 1510 -q 1; done"
