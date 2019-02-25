# Clean Up

1. run `docker rm -f $(docker ps -aq)` to stop and delete all containers
2. run `docker rmi $(docker images -a -q)` to delete all images