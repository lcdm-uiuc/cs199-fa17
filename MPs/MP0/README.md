# MP 0: Introduction to Docker

## Introduction

This lab will introduce Docker and Dockerfiles. You will be creating a container that runs Ubuntu, and python3.

### Windows Users Only
**Disclaimer:** Docker is available for windows, but we recommend using a UNIX-based system.

Start off by downloading VirtualBox. VirtualBox can be downloaded from this link:

https://www.virtualbox.org/wiki/Downloads

For instructions on how to setup Linux on a virtual machine to start the MP, follow this link:

http://www.psychocats.net/ubuntu/virtualbox

## Docker Setup
Create an account with Docker and install docker community (not enterprise). This can be found under these two links:

https://hub.docker.com/

https://docs.docker.com/engine/installation/#supported-platforms

In this MP, you will create a Dockerfile that has the following properties:

#### Goals
1. Inherits from the Ubuntu public image.
2. Implements labels for a maintainer and a class.
3. Installs python3.
4. Creates a few environment variables.
5. Writes to a file in the container
6. Sets the current user to root.
7. Runs bash whenever the container is run.

For information on building a Dockerfile, look at the [docs](https://docs.docker.com/engine/reference/builder/).

### Problem 1
* Open up your terminal
* Create a new directory and `cd` into it.
* Create a file called `Dockerfile` and open it in your favorite editor.

_These questions should be viewed as guiding questions, you don't need to submit answers for these_

Inherit from the standard `ubuntu` image on dockerhub. (Why do we do this?)

You can build and test your Dockerfile by running these commands:

```
$ docker build -t <container name> .
```
Now, you have a container named whatever you specified. Try running.
```
$ docker run -i -t <container name>
```

If you see something like:

```
root@8a788562c667:/# 
```

You've been launched into bash, and you have made your first container!

### Problem 2
Once you have your initial Dockerfile up and running, you can exit out of it by typing `exit`, or `Ctrl-D`. Now, we are going to make some modifications to the Dockerfile. Include the following docker LABELs in the file:
* `NETID` as your net-id
* `CLASS` as CS199

Now, if you `docker build ...` and `docker run ...` and then run `docker inspect <container name>` outside your container you should be able to see the two labels like:
```
"NETID":<your net-id>
"CLASS":"CS199"
```

### Problem 3
Stop your container instance again and with your labels set up, download python 3.6.1 in the container. A simple way of doing this is by using `apt-get` commands.

You should be able to do the following once python3 is setup in your container:

```
root@8a788562c667:/# python3
>>>
```

##### Note:
You might need to look into `conda`, `apt-get update` and `pip` to install python3.

### Problem 4
Finally, Create `/data/info.txt` and put `Karl the fog is the best cloud computing platform`. You should do this in the Dockerfile, not in the container (Hint: use the `RUN` command with cat). When you run your container, you should be able to see this file in the data folder. Also, specify the user that the container should run

You should now be able to run `cat /data/info.txt` in your container to see your text message.

### Problem 5
Create a new user called `cs199`. Change the user who logs in to the default shell to be the `cs199` user. Also, set and environment variable called `NAME` to be your first name. When you log run the dockerfile, you should see something like.

```
cs199@8a788562c667:/# whoami
cs199
cs199@8a788562c667:/# echo $NAME
me
```

## Deliverables
By the end of the Lab, you should have **one** Dockerfile that solves all 4 of the problems. We will check off if you have all **7** of the requirements listed above for one point each, totaling 7 points for this lab. Please, if you are having any troubles setting up, let us know during office hours.

Submit your Dockerfile as MP0 on Moodle. That's it!
