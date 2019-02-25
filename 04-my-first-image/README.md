# Your First Container

Now you will build your first image,
then we will create from the image a container instance.
the container will be the traditional hello world HTTP servers

## Create the image
please follow the steps below

 ### the first step is to create DockerFile
1. create a DockerFile
2. for the base image choose `python` with tag `3.7`
3. copy the directory from your pc `./hello-wold-code` to the  directory in the container `./`
5. run the cmd in the container `pip install -r ./requirement.txt`
6. add the env ver `port`:`2019`  
7. the entry point for the pgrogram is `python ./main.py`

### Create the Image
1. create the image with the tag `my-hello-world`

## Build the Contianer
1. run the contianer with the params:
    * map the container port 2019 to 2020 host port
    * call the contianerhello-world-v1
2. in your browser go to [http://127.0.0.1:2020](http://127.0.0.1:2020)
3. get the contianer logs

now we will run it again with env var

1. run the contianer with the params:
    * map the container port 2019 to 2021 in the host
    * add env ver `MY-NAME`:{you name} 
    * call the contianer my-hello-world-v1
2. in your browser go to [http://127.0.0.1:2021](http://127.0.0.1:2021)
3. get the contianer logs


And we done,
we have a new container from the image you build.



Notes:
1. see how we can maplted the code by adding env ver
2. please 