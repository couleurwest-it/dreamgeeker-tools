#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from . import CTracker

"""
    Networkin manager

    Usage:

    >>> from app import toolbox
    >>> proclamer()
"""
# networkmng.py
"""
Fonctions standards (ré)ultilisables
"""


def test_http_link(p_link):
    """
    Verification url
    =================

    :param p_link:
    :return:
    """

    def fn():
        s = clean_space(p_link)

        if not re.match(r'^https?[:]//', s):
            s = 'http://{}'.format(s)

        ret = requests.head(s)

        if ret.status_code in [301, 302]:
            return test_http_link(ret.headers.get('Location'))

        return s if (ret.status_code == requests.codes.ok) else False

    return CTracker.try_fn(fn, 'URL Checker').data


def get_media_domain(s):
    m = RGX_MEDIA_LINK.search(s)

    if m:
        for s in LIST_MEDIA_LINK.keys():
            if m.group(s): return s
    return None


def whoisit(p_link):
    v = whois.whois(p_link)


def url_join(w, ubase=None):
    if ubase is None:
        ubase = URL_BASE

    return urljoin(ubase, w)
