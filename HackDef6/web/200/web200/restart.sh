docker container restart $(docker container ls  | grep 'web-200' | awk '{print $1}')
