#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from datetime import datetime

from markdown.extensions.codehilite import CodeHiliteExtension

AUTHOR = "Sagar Giri"
# SITEURL = "https://sagargiri.com"
SITENAME = """Sagar's Blog"""
SITETITLE = AUTHOR
SITESUBTITLE = "<pre>$ cd /pub && more beer</pre>"
SITEDESCRIPTION = "programming, python, CS, AWS, Django"
BROWSER_COLOR = "#333333"
PATH = "content"

TIMEZONE = "Asia/Tokyo"

DEFAULT_LANG = "en"
OG_LOCALE = "en_US"
LOCALE = "en_US"
DATE_FORMATS = {
    "en": "%B %d, %Y",
}

USE_FOLDER_AS_CATEGORY = False
COPYRIGHT_YEAR = datetime.now().year
DEFAULT_PAGINATION = 5

# Theme Settings
SITELOGO = "/images/title.png"
FAVICON = "/images/favicon.png"
THEME = "themes/Flex"
PYGMENTS_STYLE = "default"

# Feed generation is usually not desired when developing
# FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Main Menu
MAIN_MENU = True
MENUITEMS = (
    ("Archives", "/archives"),
    ("Categories", "/categories"),
    ("Tags", "/tags"),
)

# Blogroll
LINKS = (("Project", "https://girisagar46.github.io/FYPFruitClassifier/"),)

# Social widget
SOCIAL = (
    ("linkedin", "https://linkedin.com/in/girisagar46"),
    ("github", "https://github.com/girisagar46"),
    ("stack-overflow", "https://stackoverflow.com/story/girisagar46.github.io"),
    ("mastodon", "https://fosstodon.org/@girisagar46"),
)

# Plugins
# See: http://docs.getpelican.com/en/latest/plugins.html
PLUGINS = ["pelican.plugins.sitemap"]

# Sitemap Settings
SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.6,
        "indexes": 0.6,
        "pages": 0.5,
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly",
    },
}

STATIC_PATHS = ["images", "extras/CNAME", "extras/robots.txt", "extras/keybase.txt"]
EXTRA_PATH_METADATA = {
    "extra/custom.css": {"path": "static/custom.css"},
    "extra/CNAME": {"path": "CNAME"},
    "extra/robots.txt": {"path": "robots.txt"},
    "extra/keybase.txt": {"path": "keybase.txt"},
}

CUSTOM_CSS = "static/custom.css"
HOME_HIDE_TAGS = True
USE_LESS = False
FEED_USE_SUMMARY = True

GOOGLE_ANALYTICS = "UA-73000395-1"
GOOGLE_TAG_MANAGER = "GTM-5K6D7ZG"
MICROSOFT_CLARITY = "7cfbr3w8ss"

# Formatting for URLS
ARTICLE_URL = "{slug}"
PAGE_URL = "pages/{slug}"
CATEGORY_URL = "category/{slug}"
TAG_URL = "tag/{slug}"
AUTHOR_SAVE_AS = "author/{slug}.html"
AUTHORS_SAVE_AS = False

FLAIR = True
FLAIR_URL = "https://stackexchange.com/users/5684581/sgiri"
FLAIR_IMAGE_URL = "https://stackexchange.com/users/flair/5684581.png"
FLAIR_USER_NAME = "sgiri"

READERS = {"html": None}

# DEFAULT_CONFIG["MD_EXTENSIONS"] =

# MD_EXTENSIONS = []
# MARKDOWN = [CodeHiliteExtension(css_class="highlight", linenums=True), "extra"]
