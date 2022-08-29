docker container restart $(docker container ls  | grep 'web-100' | awk '{print $1}')
