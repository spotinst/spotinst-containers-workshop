# Docker command

Basic training is over, from now there are no more answers for the questions

In the following sections, we will run different programs in Docker containers

## Drupal server
first read about [Drupal](https://www.drupal.org/)
1. run `drupal` container with:
    * create port mapping from container port 80 to the host port 8080
    * name the container `drupal`
2. go to the url [http://localhost:8080/](http://localhost:8080/)
3. see the logs for the container

## MySql server

we whant to run a mysql server in docker.

to run server follow the following steps:
1. run `mysql` server version `5.7` with:
    *  port mapping of port `3306` to `3306` 
    *  env key `MYSQL_PASSWORD` the value is the password you whant to use for log in 
    *  name  `sql-server-1`
    *  run the server with argument `--old-passwords=2`

2. conncet to your new mysql server:
    * Host:  127.0.0.1
    * uset: root
    * password: you password
3. don't stop the container `sql-server-1` and run other MySQL server with name `sql-server-2`
4. stop `sql-server-1` and `sql-server-2`
5. remove only the image for `mysql:5.7`

if you stuck try to find the answer the link below.
[link below](https://hub.docker.com/_/mysql)