# !/usr/bin/python3
# -*- coding: utf-8 -*-
# toolbox/krypt.py

"""Gestion  kryptage"""

import crypt, random, string, getpass
import hashlib

from . import toolsconfig


class Krypting:
    """
    Gestion kryptage des données
    """
    PREFIX = "$5$"
    SALT = toolsconfig.app_cfg('SECRET_KEY', mode='r')
    SALT_EXT = toolsconfig.app_cfg('EXTERN_SECRET_KEY', mode='r')

    @staticmethod
    def __encrypt(password, prefix):
        """This is used in place of `mkpasswd --sha-512`"""
        if isinstance(password, bytes):
            orig = password
            try:
                password = password.decode("utf-8")
            except UnicodeDecodeError:
                return None
            assert password.encode("utf-8") == orig, "utf-8 spec says this can't happen!"

        return crypt.crypt(password, prefix)

    @staticmethod
    def encrypt(password):
        """This is used in place of `mkpasswd --sha-512`"""
        return Krypting.__encrypt(password, Krypting.PREFIX + Krypting.SALT)

    @staticmethod
    def extern_encrypt(password):
        '''
        Cryptage chaine pour utilisation extrene (suppression prefix)
        :param str password:
        :return: mot de passe crypté
        '''
        """This is used in place of `mkpasswd --sha-512`"""
        s = Krypting.__encrypt(password, Krypting.PREFIX + Krypting.SALT_EXT)
        i = len(Krypting.SALT_EXT)

        return s[i:]

    @staticmethod
    def compare(enc, s):
        """Comparaison d'un chaine (mot de passe) en clair à un mot de passe crypté

        :Parametres:
        :param str enc: Mot de passe crypté
        :para str s: chaine à tester
        """
        return crypt.crypt(s, enc) == enc
