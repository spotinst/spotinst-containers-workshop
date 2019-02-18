# Your First Container

Now you will build your first image,
then we will create from the image a container instance.
the container will be the traditional hello world HTTP servers

## Build the image
please follow the steps below

 ### the first step is to create the Docker File
1. create a DockerFile
2. for the base image choose python 3.7
3. create the directory `~/my-hello-world-code`
3. copy the directory from your pc `hello-wold-code` to the new directory in the container
4. change the working directory in the container to `~/my-hello-world-code`
5. run the cmd in the container `pip install -r ./requmint.txt`
6. the entry point for the pgrogram is `python ./main.py`

### Create the Image
1. create the image with the tag `my-hello-world`

## Build thhe Contianer
1. run the contianer with the params:
    * map the container port 2019 to 2020 in the host
    * call the contianer my-hello-world-v1
2. in your terminal run the commad 
3. get the contianer logs


1. run the contianer with the params:
    * map the container port 2019 to 2020 in the host
    * add env ver `MY-NAME`:{you name} 
    * call the contianer my-hello-world-v1
2. in your terminal run the commad 
3. get the contianer logs


And we done,
we have a new container from the image you build


Notes:
1. see how we can maplted the code by adding env ver
2. please 