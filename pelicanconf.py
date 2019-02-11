#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

from markdown.extensions.codehilite import CodeHiliteExtension

AUTHOR = u'Sagar Giri'
SITEURL = u'http://localhost:8000'
SITENAME = u"Sagar Giri's Blog"
SITETITLE = AUTHOR
SITESUBTITLE = '<pre>$ cd /pub && more beer</pre>'
SITEDESCRIPTION = u's programming, pelican, python, computer science, logic, algorithm'
PATH = 'content'

TIMEZONE = 'Asia/Kathmandu'

DEFAULT_LANG = u'en'
OG_LOCALE = 'en_US'
LOCALE = 'en_US'
DATE_FORMATS = {
    'en': '%B %d, %Y',
}

USE_FOLDER_AS_CATEGORY = False
COPYRIGHT_YEAR = 2017
DEFAULT_PAGINATION = 7

# Theme Settings
SITELOGO = '/images/title.png'
FAVICON = '/images/favicon.png'
THEME = 'themes/Flex'
BROWSER_COLOR = '#333333'
PYGMENTS_STYLE = 'default'


# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Main Menu
MAIN_MENU = True
MENUITEMS = (('Archives', '/archives'),('Categories', '/categories'),('Tags', '/tags'),)

# Blogroll
LINKS = (('Project', 'https://girisagar46.github.io/FYPFruitClassifier/'),)

# Social widget
SOCIAL = (('linkedin', 'https://linkedin.com/in/girisagar46'),
          ('github', 'https://github.com/girisagar46'),
          ('twitter', 'https://twitter.com/sagargiri46'),
          ('stack-overflow', 'http://stackoverflow.com/story/girisagar46.github.io'),
          )

# Plugins
# See: http://docs.getpelican.com/en/latest/plugins.html
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['sitemap', 'post_stats', 'feed_summary']

# Sitemap Settings
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.6,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}

STATIC_PATHS = ['images', 'extras']

EXTRA_PATH_METADATA = {
    'extras/custom.css': {'path': 'static/custom.css'},
    # 'extra/CNAME': {'path': 'CNAME'},
    # 'extra/robots.txt': {'path': 'robots.txt'}
}

CUSTOM_CSS = 'static/custom.css'
HOME_HIDE_TAGS = True
USE_LESS = False
FEED_USE_SUMMARY = True

GOOGLE_ANALYTICS = 'UA-73000395-1'
GOOGLE_TAG_MANAGER = 'GTM-5K6D7ZG'
DISQUS_SITENAME = 'girisagar46-github-io'
# GOOGLE_ADSENSE = {
#     'ca_id' : 'ca-pub-6204331251488075',
#     'ads': {
#         'aside': '1234561',          # Side bar banner (all pages)
#         # 'main_menu': '1234562',      # Banner before main menu (all pages)
#         # 'index_top': '1234563',      # Banner after main menu (index ofabnly)
#         # 'index_bottom': '1234564',   # Banner before footer (index only)
#         # 'article_top': '1234565',    # Banner after article title (article only)
#         # 'article_bottom': '1234566', # Banner after article content (article only)
#     }
# }

# SHARING
ADD_THIS_ID = 'ra-589c9f9f19d6a715'


# Formatting for URLS
ARTICLE_URL = '{slug}'
PAGE_URL = 'pages/{slug}'
CATEGORY_URL = 'category/{slug}'
TAG_URL = 'tag/{slug}'
AUTHOR_SAVE_AS = False
AUTHORS_SAVE_AS = False


#CUSTOM_AD

# AD_IMAGE = '/images/merohostel.jpg'
# AD_URL = 'http://merohostel.com/'
# AD_ALT = 'banner for merohostel ad'
# AD_TITLE = 'www.merohostel.com'
# AD_HEIGHT = '250px'
# AD_WIDTH = '200px'

FLAIR = True
FLAIR_URL = "https://stackexchange.com/users/5684581/sgiri"
FLAIR_IMAGE_URL = "https://stackexchange.com/users/flair/5684581.png"
FLAIR_USER_NAME = "sgiri"


READERS = {'html': None}

# DEFAULT_CONFIG['MD_EXTENSIONS'] =

# MD_EXTENSIONS = []
MD_EXTENSIONS = [CodeHiliteExtension(css_class='highlight', linenums=True), 'extra']
