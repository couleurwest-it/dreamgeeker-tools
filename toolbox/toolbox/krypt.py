# !/usr/bin/python3
# -*- coding: utf-8 -*-
# krypt.py

"""
Module de cryptage
"""

import crypt

from . import cfgloader


class CKrypting:
    """
    Gestion kryptage des données
    """
    PREFIX = "$5$"
    SALT = cfgloader.app_cfg('SECRET_KEY')
    SALT_EXT = cfgloader.app_cfg('SALT')

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
        return CKrypting.__encrypt(password, CKrypting.PREFIX + CKrypting.SALT)

    @staticmethod
    def extern_encrypt(password):
        '''
        Cryptage chaine pour utilisation extrene (suppression prefix)

        :param str password:
        :return: mot de passe crypté
        '''
        """This is used in place of `mkpasswd --sha-512`"""
        s = CKrypting.__encrypt(password, CKrypting.PREFIX + CKrypting.SALT_EXT)
        i = len(CKrypting.SALT_EXT)

        return s[i:]

    @staticmethod
    def compare(enc, s):
        """Comparaison d'un chaine (mot de passe) en clair à un mot de passe crypté

        :Parametres:
        :param str enc: Mot de passe crypté
        :para str s: chaine à tester
        """
        return crypt.crypt(s, enc) == enc
