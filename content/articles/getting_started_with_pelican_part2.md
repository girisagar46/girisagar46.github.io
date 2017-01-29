Title: Building a static site and hosting in Github (part 2)
Date: 2017-1-28 17:00
Modified: 2017-1-28 17:00
Category: tutorial
Tags: tutorial, pelican
Slug: pelican-github-part2
Summary: In [Part 1], we just got started with our Pelican blog. In this part, we'll be hacking our blog to make it awesome.

> In [Part 1] we setup our github.io website and kick started out [Pelican] website. Now, in this second tutorial, we'll configure Fabric and Pelican configuration and when it's all done, we'll create blog post. And push it to github `source` branch.


# Let's setup our blog theme first.

Pelican has tons of themes. All themes can be previewed at [pelicanthemes.com](http://www.pelicanthemes.com/). You can pick any themes you like. If you are not satisfied, you can also create your [own theme](http://docs.getpelican.com/en/3.1.1/themes.html). For this tutorial, we'll be using a theme called [Flex](https://github.com/alexandrevicenzi/flex) by [Alexandre Vicenzi](https://www.alexandrevicenzi.com/). 

To setup a theme, create folder inside your `username.github.io` directory and name it `themes`. Now `cd` into that directory and clone the [Flex](https://github.com/alexandrevicenzi/Flex.git) repository.

```bash
$ git clone https://github.com/alexandrevicenzi/Flex.git
```

You can setup plugins in same way as the themes. The repository for plugins is [pelican-plugins](https://github.com/getpelican/pelican-plugins). We won't setup plugins in this tutorial. You can read the documentation yourself to setup the plugins or I'll be posting a tutorial on how to setup plugins shortly.

# Configuration

We have our Flex theme inside our theme directory. Our theme needs a site logo. Site logo should be placed in a images directory. So, create an `images` folder inside the `content` folder. Paste an image in that folder. If you don't have any, default image will be rendered.

For the configuration, we'll be working on `pelicanconf.py`, `publishconf.py` and `fabfile.py`.

First let's look at `pelicanconf.py`. Open it in a text editor and update it. See the comments beginning with `#` to know what's happening.

```python
from __future__ import unicode_literals

AUTHOR = u'Your Name'
SITENAME = u'Your Blog Name'
SITEURL = u'http://localhost:8000' #used for local build and preview
SITETITLE = AUTHOR
SITESUBTITLE = 'Your own text' #needed for theme
SITEDESCRIPTION = u'your site description' #used for meta tag for SEO purposes
PATH = 'content' # location to where your articles/posts are located

TIMEZONE = 'Asia/Kathmandu' # Your current time zone

DEFAULT_LANG = u'en'

DATE_FORMATS = {
    'en': '%B %d, %Y',
}

USE_FOLDER_AS_CATEGORY = False
COPYRIGHT_YEAR = 2017
DEFAULT_PAGINATION = 7

# Theme Settings
SITELOGO = '/images/Your picture' #your site logo
FAVICON = '/images/favicon.png' #your favicon
THEME = 'themes/Flex' #path to your theme
BROWSER_COLOR = '#333333'
PYGMENTS_STYLE = 'default' #for code highlighting

# Blogroll
# if you want to link to external page
LINKS = (('link1', 'Your link'),)

# Social widget
# You can add your own links for facebook, twitter
SOCIAL = (('Facebook', 'Your facebook link'),
         ('Twitter', '#'),)

DEFAULT_PAGINATION = 10
```

If you want to know more details about the configuration, go [here](https://github.com/alexandrevicenzi/Flex/wiki/Configuration-example).

Next, open `publishconf.py` file and modify these lines:

```python
SITEURL = 'https://your_username.github.io'
RELATIVE_URLS = False
```

# Our first post

`cd` to your `content` directory and create a folder called `articles`. Inside that `articles` folder create a new file called `FirstPost.md`.
Open that `FirstPost.md` file in a text editor and paste the lines as shown below:

```
Title: My super title
Date: 2010-12-03 10:20
Modified: 2010-12-05 19:30
Category: abc
Tags: abc, xyz
Slug: my-super-post
Authors: Your name
Summary: Short description

This is the content of my super blog post.
```
To know more, read the official [documentation](http://docs.getpelican.com/en/stable/content.html).

# Generate HTML

In the terminal, type `$ fab clean; fab build; fab serve` and browse to `http://localhost:8000`. You'll see new shining blog with new design.

# Commit and push to Github

** First, let's push our source code.**

Type these commands one by one.

```bash
$ git checkout source
$ git add .
$ git commit -m "Configuration, themes and first post"
$ git push
```

** Push the HTML contents in the `master` branch.**

```bash
$ ghp-import -m 'First push to github.io' -b master output"
$ git push -u origin master
```

Now, redirect your browser to 'https://your_username.github.io' to view your online blog.


Upto this you have your blog and is available to public access. Next, I'll be posting some small tutorials on how to add [disqus](https://disqus.com) comments, google analytics, automate publish using Fabric API, adding and configuring plugins and many more.


Keep visiting my [website](https://girisagar46.github.io).