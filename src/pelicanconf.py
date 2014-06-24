#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'\u041f\u0430\u0432\u0435\u043b \u0421\u0443\u0442\u044b\u0440\u0438\u043d'
SITENAME = u'\u041f\u0430\u0432\u0435\u043b \u0421\u0443\u0442\u044b\u0440\u0438\u043d'
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'ru'
DEFAULT_DATE = 'fs'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

THEME = "themes/pelican-bootstrap3"

DISPLAY_PAGES_ON_MENU = True
DISPLAY_TAGS_ON_SIDEBAR = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_CONTACTS_ON_SIDEBAR = True

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
