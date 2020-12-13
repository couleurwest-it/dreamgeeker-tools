# !/usr/bin/python3
# -*- coding: utf-8 -*-
# captcha.py

""" Gestion tools/captcha """

from app.captcha import ImageCaptcha
from . import tools

__author__ = "Ketsia LENTIN"
__copyright__ = "Copyright 2019, Les Couleurs de l'ouest"
__credits__ = "Ketsia LENTIN"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "dreamgeeker@couleurwest-it.com"
__email__ = "dreamgeeker@free.fr"
__status__ = "Production"


class CCaptcha(ImageCaptcha):
    __ttf = ['VeraIt.ttf', 'Algerian.ttf', 'Scarlett.ttf', 'TerminalVector.ttf']
    __ttf_path = tools.path_build(tools.STATIC_DIR, 'fonts')

    @staticmethod
    def ttf_path(v):
        return tools.path_build(CCaptcha.__ttf_path, v)

    def __init__(self):
        l = list(map(CCaptcha.ttf_path, CCaptcha.__ttf))
        super().__init__(width=250, height=100, fonts=l)

    def generate_catcha(self, s=6, frm='jpeg'):
        """
        Genere une image en byte d"un code
        =======================================
        :app int s, default 6: taille du captcha (nb car.)
        :app str frm, default jpeg: format de l'image (JPEG, PNG, GIF...), optional
        :return: code, image
        :rtype: str, IOByte
        """
        c = tools.code_maker(s)
        return c, self.generate(c, frm)

    def image_captcha(self, s, fl='out.img', frm='jpg'):
        """
        Genere une image en byte d"un code et l'enregistre

        :app str value: valeur a crypter
        :app str fl: nom du fichier, out.jpg par defaut
        :app str frm: format, default to jpg

        :return: IOByte
        """
        self.write(s, fl, frm)
