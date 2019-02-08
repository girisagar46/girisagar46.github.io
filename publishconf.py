#!/usr/bin/env python

import os
import sys

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.
sys.path.append(os.curdir)

SITEURL = 'https://girisagar46.github.io'
RELATIVE_URLS = False

FEED_DOMAIN = SITEURL
# FEED_ALL_ATOM = SITEURL+'feeds/all.atom.xml'
# CATEGORY_FEED_ATOM = SITEURL+'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
