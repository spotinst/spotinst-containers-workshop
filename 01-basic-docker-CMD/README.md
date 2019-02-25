# Basic Docker command
This is your  first steps in the container world,
so the following tasks going to over the basic command in the docker.

In each section, you will find a questions about docker command, 
try to run the command in your terminal and see if you succeed.
try to think a least 5 minutes about the answer before looking in the answer.


for example:
``` base
what the command to pull ubuntu image version 18.10?
```

<details><summary>tell me the answer</summary>
<p>

```bash
docker pull ubuntu:18.10
```
</p>
</details>


## Pull Image
***

 what the command to pull centos image version 6


<details><summary>tell me the answer</summary>
<p>

```bash
docker pull centos:6
```
</p>
</details>

***
what tag/version we will pull if we run?
```bash
docker pull ubuntu
```
<details><summary>tell me the answer</summary>
<p>

the docker image with tag `latest`
</p>
</details>

***

## Create Container

***
how to run ubntu versio 18.10 in interactive mode?
(mean you can see the container terminal)

<details><summary>tell me the answer</summary>
<p>

```
docker run -it  ubuntu bash
``` 
remeber for interactive mode you need to run docker with `-it`
</p>
</details>

***
how to run ubntu versio 18.10 in detach mode?
(hint, run with the command `/usr/bin/top -b`)
<details><summary>tell me the answer</summary>
<p>
the trick is to pick a  command the never close for example 

```
docker run -d ubuntu /usr/bin/top -b
``` 
you need to run with `-d` and command that will not exit

</p>
</details>

***
how to run run opensuse in interactive mode with container the name `lizard`?

<details><summary>tell me the answer</summary>
<p>

```
docker run -it --name lizard opensuse /bin/sh
``` 

</p>
</details>

***

how to run `ubuntu` in interactive mode with envs name `OS` key `ubuntu` name `creator` key `spotisnt`?
 
<details><summary>tell me the answer</summary>
<p>

```
docker run -it -e "OS=ubuntu"  -e "creator=spotisnt" ubuntu /bin/sh
``` 

</p>
</details>

***

how to run `mageia` with tag `5.1` in interactive mode and env name `OS` key `mageia` and container name `prod`?
 
<details><summary>tell me the answer</summary>
<p>

```
docker run -it --name prod -e "OS=mageia" mageia:5.1 /bin/sh
``` 

</p>
</details>

## Stop and Start Container
***
this task have 3 steps:
1. create ubntu image in detached with name `myUbntu`
2. stop `myUbntu`
3. start `myUbntu`

<details><summary>tell me the answer for step 1</summary>
<p>

```
docker run -d --name myUbntu ubuntu /usr/bin/top -b
``` 

</p>
</details>

<details><summary>tell me the answer for step 2</summary>
<p>

```
docker stop myUbntu
``` 

</p>
</details>


<details><summary>tell me the answer for step 2</summary>
<p>

```
docker stop myUbntu
``` 

</p>
</details>


## General Commands

***

find out the name for container that run without the `--name` flag

<details><summary>tell me the answer</summary>
<p>
first run a container

```
docker run -it  ubuntu bash
``` 

open a secnd terimnal and run
```
docker ps
``` 

</p>
</details

***

how to list all containers include container in stop state?

<details><summary>tell me the answer</summary>
<p>

```
docker ps -a
``` 

</p>
</details

***


## Network

***

how to run `ubuntu` with container port `2018` map to host port `2019`?

<details><summary>tell me the answer</summary>
<p>

```
docker run -it  -p 2019:2018 ubuntu bash
``` 

</p>
</details

***

how to run `ubuntu` with container port `8080` map to host port `7070` and container port `8081` to host port `2045`?

<details><summary>tell me the answer</summary>
<p>

```
docker run -it  -p 7070:8080 -p  2045:8081 ubuntu bash
``` 

</p>
</details

