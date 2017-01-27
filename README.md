# girisagar46.github.io

This repository hosts the [Pelican](http://getpelican.com/) source code for my personal blog *[girisagar46.github.io](https://girisagar46.github.io)*

If you want to view the HTML rendered, then checkout [master branch](https://github.com/girisagar46/girisagar46.github.io/tree/master) of this repo.

This is a static website and is powered by [Pelican](http://getpelican.com/) — a static site generator written in pure Python. Theme used for this blog is [Flex](https://github.com/alexandrevicenzi/Flex).


## Build and run locally
> I am assuming you have linux environment. For windows workout yourself.

First you need to install [virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/). 

`$ sudo apt-get install virtualenv`

### Create a Virtual Environment

Once you have `virtualenv` installed, create a virtual environment to hold Pelican and its dependencies:

    $ mkdir dirName
    $ cd dirName
    $ virtualenv venv
    $ source venv/bin/activate

This creates a virtual environment and then activates it. If you want to exit the virtual environment, type:

    $ deactivate

### Fork / Clone the Repo

Clone this repo of source code.

    $ git clone https://github.com/girisagar46/girisagar46.github.io.git
    $ cd girisagar46.github.io

### Install Pelican and it's dependencies

Use `pip` to install the list of dependencies (including Pelican) into your virtual environment. If you don't have pip installed, see [here](http://www.saltycrane.com/blog/2010/02/how-install-pip-ubuntu/)

    $ pip install -r requirements.txt

### Generate the Website

Now, build the website using Fabric and it'a API's.

    $ fab build

This spits out HTML pages from the Markdown files in the `content/` directory.

### Preview the Website

Previewed the website in your browser:

    $ fab serve

And you should see the blog if you visit [http://localhost:8000](http://localhost:8000).

## Blog Workflow

Interested in writing a blog post?

- [Fork](https://github.com/girisagar46/girisagar46.github.io.git/fork) the repository
- Write a blog post using Markdown in the `content` directory
- Push the changes to a your custom branch on *your* fork of the repository
- Make a [pull request](https://help.github.com/articles/using-pull-requests/) against the `source` branch


## Hosting

This blog is hosted by [GitHub Pages](https://pages.github.com/) for *free.


## Contact

If you have any questions, or issues regarding the repository then open a [issue ticket](https://github.com/girisagar46/girisagar46.github.io/issues/new) for this repo. Love to hear your feedback.