Title: Docker 101 (Part 1)
Date: 2018-12-2 0:1
Modified: 2018-12-2 0:1
Category: tech, docker
Tags: docker, docker
Slug: docker-101
Summary: I don't have any prior experience with docker. To everyone who is reading, this post is just my experience and as well as a kind of personal note for me for future reference. :)

## Step 1: Install Docker

Docker can be installed in pretty much any OS platform, be it Windows, Mac or Linux. Since I use a Linux machine this whole article is based on the Linux system. For installing docker in Windows and Mac, refer the official documentation.

Ok, enough talk. Let's get started.

Docker is a company as well as a software. And docker is released every month which is called edge release. And every quarter, a stable version of docker is released. 

One of the ways to install docker on a Linux machine is by using the apt package manager but, the problem with this is approach is that you'll not get the current release of docker which sucks IMO because in every new release new features are baked in. So, I advise you to not install via the apt package manager (if you are in Debian ubuntu variant of Linux) or any other package manager for other Linux distributions.

There are two versions of docker available to download and install. One being free aka Community Edition and another paid version Enterprise Edition. For learning purpose, we'll install Community Edition docker. Hey! who does not like free software? ;)

Okay, to install the latest and greatest version of community edition docker, fire up your terminal and execute the following command:

```bash
$ wget -qO- https://get.docker.io/ | sh
```

What this command does is that it pulls the installation script from the [https://get.docker.io/](https://get.docker.io/) and execute as a shell command. After the installation is complete, check the version of docker that is installed in your system by:

```bash
$ docker --version
```
You'll see that the current stable release of the docker has been installed.

```bash
Docker version 18.09.0, build 4d60db4
```

## Step 2: Configure Docker

Couple of things you need to configure after installing Docker. At the time of installation, docker is attached to the root user and every time you need to execute a docker command, you have to pass the sudo command. This situation is not idle for many cases. To fix this, we should bind docker to another user. Execute the following command to attach docker to another user:

```bash
$ sudo usermod -aG docker ubuntu
```

*Note: Replace ubuntu with your username*

After this, install docker machine. Docker machine should also be the latest version. For Windows and Mac user, docker machine is already installed while installing Docker. To install docker machine, head over to this link [https://github.com/docker/machine/release](https://github.com/docker/machine/release). You'll see the command which is like this...

```bash
$ curl -L https://github.com/docker/machine/releases/download/v0.16.0/docker-machine-`uname -s`-`uname -m` >/tmp/docker-machine && chmod +x /tmp/docker-machine && sudo cp /tmp/docker-machine /usr/local/bin/docker-machine
```

Execute the above command and check if docker machine is installed or not by executing

```bash
$ docker-machine version
docker-machine version 0.16.0, build 702c267f
```

Now, install docker compose.

Head over to this link [https://github.com/docker/compose/release](https://github.com/docker/compose/release). You'll see the command which is like this...

```bash
$ curl -L https://github.com/docker/compose/releases/download/1.23.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
$ chmod +x /usr/local/bin/docker-compose
```

Grab that command and execute it. Once complete, check if docker machine is installed or not by executing

```bash
$ docker-compose version
docker-compose version 1.23.2, build 1110ad01
docker-py version: 3.6.0
CPython version: 3.6.7
OpenSSL version: OpenSSL 1.1.0f  25 May 2017
```

That's pretty much it. Now you have docker installed in your Linux machine.

PS. If you are using windows or MAC, visit the official docker website [https://docs.docker.com/docker-for-windows/install/](https://docs.docker.com/docker-for-windows/install/) to get more details.

In the next part, well dive deeper into the Docker world. 
