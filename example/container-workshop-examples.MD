# Example for pull:
1.  pull centops 
`docker pull centos`
2. got to docker hub choose random tag and pull with tag

# Example list images:
1. run `docker images`
2. and point out there is our image

# Create containers
## in foreground
### let them see the contaienr is deleted when exit
1. run `docker run --name my-ubuntu -it ubuntu bash`
2. point out the run without pull will pull the image 
3. list the container and see there is a new container  
4. exit the contianer 
5. list the container and see the container has stopped (con only be seen with -a )
`docker ps -a`

### let them see the name givan to a contaiener where there is no name flag
1. run `docker run --name my-ubuntu -it ubuntu bash` with name
2. run `docker run  -it ubuntu bash` without name
3. list the containers
4. point out the names

## In background
1. run `docker run --name background_mode -d  ubuntu bash`
2. point out the contianer stoped immediately
3. this is because PID 1 has stopped 

### In background
1. now run with `docker run --name background_mode_v2 -d ubuntu yes > /dev/null`
2) explain the command `yes > /dev/null`

## run with env ver
run `docker run -rm --name my-ubuntu-env -e "HELLO=WORLD" -e "FUN=DAY" -it ubuntu bash` 

## Stop start logs for background
1. run the container `docker pull noam0stein/print_hello_world`
2. explain what the container does and let them see the code
3. run `docker run -d --name loop noam0stein/print_hello_world`
4. open terinal with logs
5. stop the container 
6. let tehm see the logs stoped
7. start the conatiner
8. what going to heppen to the logs




