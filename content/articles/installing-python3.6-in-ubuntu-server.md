Title: Installing Python3.6 in Ubuntu 16.04 LTS Instance Server
Date: 2018-5-23 23:32
Modified: 2018-5-23 23:32
Category: tutorial
Tags: tutorial, python3.6, python, installation
Slug: installing-python3.6-in-ubuntu-server
Summary: Installing Python 3.6.3 in your freshly installed Ubuntu 16.04 Desktop, Linux Mint Desktop or even in AWS/Azure Ubuntu 16.04 server instance is pain in the a**. This article will teach you how to install Python 3.6.3 from source including the dependencies you need to install inorder to work it correctly.

Here is the step by step guide to install `Python 3.6.3` in your AWS EC2's Ubuntu 16.04 server instance or in your local machine with Ubuntu 16.04 LTS Desktop or in Linux Mint.

**Note: If you are using Ubuntu 18.04 LTS, then it ships with Python 3.6.3 by default.**

Check which Python version is pre-installed in the system by typing `$ python3 -V` in the terminal. Generally it is `Python 3.5.2` for Ubtuntu 16.04 LTS.

## Pre-requisites

1. First you need to upgrade and update your system.

    `$ sudo apt update && sudo apt -y upgrade`

2. Then you need to install `zlib1g-dev` package because of [this](https://github.com/pypa/pip/issues/1919) issue. 

    `$ sudo apt -y install zlib1g-dev`
    To make sure it is installed correctly, type `$ cat /usr/include/zlib.h`. It'll show you the source of `zlib` header file.

3. Because of [this](https://stackoverflow.com/questions/893053/seeing-escape-characters-when-pressing-the-arrow-keys-in-python-shell) issue, you also have to install another package called `libreadline-dev`

    `$ sudo apt install libreadline-dev`

4. Now, install `build-essential` and other bunch of stuffs which is required by `Python 3.6.3` afterwards.

    `$ sudo apt install build-essential checkinstall libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev`

    These packages are needed for setting up SSL for downloading packages over PIP, for setting up `sqlite`, `g++` and so on.

5. Export `LD_LIBRARY_PATH` for secure SSL connection.

    `$ export LD_LIBRARY_PATH=/usr/local/ssl/lib/`

## Begin installation of Python 3.6.3

1. First, download tar zipped file from Python FTP server.

    `wget https://www.python.org/ftp/python/3.6.3/Python-3.6.3.tgz`

2. Extract the zipped file:

    `$ tar zxvf Python-3.6.3.tgz`

3. Move Python3.6.3 directory to `/opt/` directory and `cd` into it.

    `$ sudo mv Python-3.6.3 /opt/`
    
    `$ cd /opt/Python-3.6.3/`

4. Configure Python directory.

    `$./configure --enable-optimizations`

5. Make it:
    
    `$ make`

6. Test the Make if you want (this is optional)

    `$ make test`

7. Install it via Make:

    `sudo make install`

8. Verify that Python 3.6.3 is installed in your system by typing

    `$ python3`


    If it again shows Python 3.5.2 then type `$ python3.6`. To make things easier, set up an alias. To set up alias do the following:

    Edit `.bashrc` file located in your home directory.

    `$ nano ~/.bashrc`

    Add following line at the end

    `alias python3=/usr/local/bin/python3.6`

*At this point, Python 3.6.3 is correctly installed in your system*

## Further steps:

1. Make sure yout PIP is correct. In Python2 is `pip` and in Python3 its `pip3`

    `$ pip3 -V` shows you which Python it is pointing to.

2. If you are using `pyodbc` then you need to install `unixodbc-dev`

    `$ sudo apt -f install unixodbc-dev`

    Then you can insall `pyodbc` with:
    
    `$ pip3 install pyodbc`
