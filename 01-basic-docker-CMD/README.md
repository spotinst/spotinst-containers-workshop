# Basic Docker command
This is your  first steps in the container world,
so the following tasks going to over the basic command in the docker.

In each section, I will describe is the needed action and you need to find the Docker command to execute the action

for example:
``` base
pull ubuntu image version 18.10
```

<details><summary>tell me the answer</summary>
<p>

```bash
docker pull ubuntu:18.10
```
</p>
</details>

If you struggle with the answer take 5 minutes before looking in the answer

## Pull Image
***

 pull centos image version 6


<details><summary>tell me the answer</summary>
<p>

```bash
docker pull centos:6
```
</p>
</details>

***
what tag/version we will pull if we run
```bash
docker pull ubuntu
```
<details><summary>tell me the answer</summary>
<p>

the docker image with tag `ubuntu`
</p>
</details>

***

## Create Container
***
run ubntu versio 18.10 in interactive mode
(mean you can see the container terminal)

<details><summary>tell me the answer</summary>
<p>

```
docker run -it  ubuntu bash
``` 

</p>
</details>

***
run ubntu versio 18.10 in detach mode 
(hint, run with the command `/usr/bin/top -b`)
<details><summary>tell me the answer</summary>
<p>
the trick is to pick a  command the never close for example 

```
docker run -d ubuntu /usr/bin/top -b
``` 

or

```
docker run -d ubuntu yes > /dev/null
``` 

</p>
</details>

***
run opensuse and give the continer the name "lizard" in interactive mode

<details><summary>tell me the answer</summary>
<p>

```
docker run -it --name lizard opensuse /bin/sh
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