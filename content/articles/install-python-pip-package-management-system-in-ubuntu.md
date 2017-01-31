Title: Install Python pip package management system in Ubuntu
Date: 2017-1-31 19:21
Modified: 2017-1-31 19:21
Category: tutorial, python, pip
Tags: tutorial, python, pip
Slug: install-python-pip-package-management-system-in-ubuntu
Summary: pip is a package management system used to install and manage software packages written in Python. 

`pip` is the replacement for the `easy_install` python package management tool. 

If you're running Python 2.7.9+ or Python 3.4+ pip is already installed in the bundle.

If you are below Python 2.7.9 then these are the steps you need to follow to install PIP.

# For Ubuntu

```bash
$ sudo apt-get update
$ sudo apt-get -y install python-pip
```
But, even if you are running python 3.4+ version, and pip is not available in the sytem, you can install by:

```bash
$ sudo apt-get install python3-pip
```

# For Mac OS

```bash
$ sudo easy_install pip
```

or

```bash
$ brew install python
```

# For Windows

You can install pip via installer. 

Download, [pip-1.1.win32.exe](http://download.sjsoft.com/opensource/pip-1.1.win32.exe) and run setup.


# Verify the pip setup

Check version of the pip via from command line.

```bash
pip -V
```

# pip usage

```bash
$ sudo pip install some-package-name
```
Users can also easily remove the package:

```bash
$ sudo pip uninstall some-package-name
```
pip has a feature to manage full lists of packages and corresponding version numbers, possible through a "requirements" file. And is mainly used for `virtual enviromnent`

```bash
$ pip install -r requirements.txt
```

Sources:

1. [http://stackoverflow.com/questions/17271319/how-to-install-pip-on-mac-os-x](http://stackoverflow.com/questions/17271319/how-to-install-pip-on-mac-os-x)
2. [http://stackoverflow.com/questions/4750806/how-do-i-install-pip-on-windows](http://stackoverflow.com/questions/4750806/how-do-i-install-pip-on-windows)
3. [https://www.liquidweb.com/kb/how-to-install-pip-on-ubuntu-14-04-lts/](https://www.liquidweb.com/kb/how-to-install-pip-on-ubuntu-14-04-lts/)
4. [https://en.wikipedia.org/wiki/Pip_(package_manager)](https://en.wikipedia.org/wiki/Pip_(package_manager))