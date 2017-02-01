Title: Installing Git Version Control System
Date: 2017-2-1 19:1
Modified: 2017-2-1 19:1
Category: tutorial
Tags: tutorial, github, git, vcs, version control
Slug: installing-git-version-control-system
Summary: Git is most widely used modern (VCS) version control system. Git is an open source project and originally developed to maintain code for Linux kernel and developed in 2005 by [Linus Torvalds](https://en.wikipedia.org/wiki/Linus_Torvalds).

> "Software is like sex: it's better when it's free." - Linus Torvalds

Git is available for all platforms Linux, Mac OS X and Windows.

# Install Git on Mac OS X
There are different ways to install Git on a Mac. If you've installed XCode (or it's Command Line Tools), Git may already be installed. To find out, open a terminal and enter `git --version`.
Inorder to install a newer version of Git, use one of these methods:

## Git for Mac Installer

The easiest way to install Git on a Mac is via the stand-alone installer:

1. Download the latest [Git for Mac](https://sourceforge.net/projects/git-osx-installer/files/) installer.
2. Follow the prompts to install Git.
3. Open a terminal and verify the installation was successful by typing `git --version`
4. Configure your Git username and email using the following command

```bash 
$ git config --global user.name "Your Name" 
$ git config --global user.email "yourvalidemail@company.com"
```

## Git for Windows stand-alone installer

1. Download the latest Git for Windows [installer](https://git-for-windows.github.io/).
2. Execute the installer, finish the Git Setup wizard screen with default options.
3. Open a Command Prompt or Git Bash (search git in all programs).
4. Run the following commands to configure your Git username and email using the following command. These details will be associated with any commits that you create:

```bash
$ git config --global user.name "Your Name"
$ git config --global user.email "yourvalidemail@company.com"
```

## Git for Linux (Debian/ Ubuntu)

1 From your shell, install Git using apt-get (Ubuntu 14.04) or apt (Ubuntu 16.04 or later):

```bash
$ sudo apt-get update
$ sudo apt-get install git
```
2. Verify the installation was successful by typing git --version:

```bash
$ git --version
git version 2.9.2
```
3. Configure your Git username and email using the following command. These details will be associated with any commits that you create:

```bash
$ git config --global user.name "Your Name"
$ git config --global user.email "yourvalidemail@company.com"
```

source: [https://www.atlassian.com/git/tutorials/install-git](https://www.atlassian.com/git/tutorials/install-git)