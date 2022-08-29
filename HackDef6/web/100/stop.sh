docker container stop $(docker container ls  | grep '100_flask' | awk '{print $1}')
