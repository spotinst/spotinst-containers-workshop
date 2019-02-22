# Basic DockerFile command

## Basic Commands

***

Choose the base image for `python` version `2.7.15`

<details><summary>tell me the answer</summary>
<p>

```bash
FROM  python:2.7.15
```
</p>
</details>


***

Choose the base image for `openjdk` version `12`

<details><summary>tell me the answer</summary>
<p>

```bash
FROM  openjdk:12
```
</p>
</details>

***

How to copy the file `./data` to the folder `/info`

<details><summary>tell me the answer</summary>
<p>

```bash
COPY ./data /info
```
</p>
</details>

***

How to copy the file `./conif.json` to the folder `/var/configs`

<details><summary>tell me the answer</summary>
<p>

```bash
COPY ./conif.json /var/configs
```
</p>
</details>

***

How to add the env ver key `hello` value `world`

<details><summary>tell me the answer</summary>
<p>

```bash
ENV hello=world
```
</p>
</details>

***

Change the ENTRYPOINT into `/run/db-java -c config.json`

<details><summary>tell me the answer</summary>
<p>

```bash
ENTRYPOINT /run/db-java -c config.json
```
</p>
</details>

