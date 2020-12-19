#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# networkmng.py

import re
import requests
from urllib.parse import urljoin

import whois

from . import tracker, tools

"""
    Networkin manager

    Usage:

    >>> from toolbox import toolbox
    >>> proclamer()
"""

def test_http_link(p_link):
    """
    Verification url
    =================

    :param p_link:
    :return:
    """

    def fn():
        s = tools.clean_space(p_link)

        if not re.match(r'^https?[:]//', s):
            s = 'http://{}'.format(s)

        ret = requests.head(s)

        if ret.status_code in [301, 302]:
            return test_http_link(ret.headers.get('Location'))

        return s if (ret.status_code == requests.codes.ok) else False

    return tracker.fntracker(fn, 'URL Checker').data

def check_mail(mail_certified):
    """
    Verification legere domaine/mot de passe
    :app str mail_certified: mail a check
    :return: True / False
    """
    # Step 1: Getting MX record from domaine
    return tools.check_mail(mail_certified) is not None

def whoisit(p_link):
    v = whois.whois(p_link)


def url_join(domaine, page):

    return urljoin(domaine, page)
