# !/usr/bin/python3
# -*- coding: utf-8 -*-
# tools/app_tools.py

"""Fonctions standard application"""

import yaml

try:
    from yaml import CLoader as Loader, CDumper as Dumper, CSafeLoader as SafeLoader
except ImportError:
    from yaml import Loader, Dumper, SafeLoader



__all__ = ['CFGBases']

from app import tools


class CFGEngine(object):
    """
    cfg engine
    """
    __dir_path = None

    @staticmethod
    def initial(baz_dir='cfg'):
        """

        :param str baz_dir:
        :return:
        """
        CFGEngine.__dir_path = tools.path_build(tools.PROJECT_DIR, baz_dir)


    @staticmethod
    def working_directory(sub_dir):
        CFGEngine.initial()
        print ('3', CFGEngine.__dir_path)
        return  tools.path_build(CFGEngine.__dir_path, sub_dir)

    @staticmethod
    def load_cfg(filepath, r=None, mode='rb'):
        """
        Récupération des parametres de configuration du fichier <filepath> section <r>

        :param str filepath: Fichier de configuration
        :param str r: référence parametres à récupérer, optionnel
        :param str mode: bytes par defaut
        :return: configuration | None

        """
        config = None

        try:
            if tools.file_exists(filepath):
                with open(filepath, mode) as cfg:
                    cfg = yaml.load(cfg, Loader=SafeLoader)
                    if type(cfg).__name__ == "dict":
                        cfg = dict(cfg)
                    elif type(cfg).__name__ == "list":
                        cfg = list(cfg)

                    config = cfg.get(r) if r else cfg
        except Exception as ex:
            print("err", ex)
        finally:
            return config

    @staticmethod
    def save_cfg(d, f, m="w"):
        """Enregistre un fichier
        :app d: données à enregistrer
        :app str f: nom du fichier
        :app str m, default (write): mode "w|a", optional
        :return:
        """
        tools.makedirs(tools.get_parent_dir(f))

        with open(f, m) as f_yml:
            yaml.dump(d, stream=f_yml, allow_unicode=True)

        return f


class CFGBases(CFGEngine):
    """
    Parametres de configuraiton
    """
    CFG_DIR = CFGEngine.working_directory('')  # databases parameters
    __cfg_db = tools.path_build(CFG_DIR, '.db.yml')  # databases parameters
    __cfg_log = tools.path_build(CFG_DIR, '.log.yml')
    __app_log = tools.path_build(CFG_DIR, '.app.yml')
    categories = tools.path_build(CFG_DIR, 'categorie.yml')
    mail_sender = tools.path_build(CFG_DIR, 'mailing.yml')
    cfg_validator = tools.path_build(CFG_DIR, 'validators.yml')  # databases parameters
    cfg_normalizor = tools.path_build(CFG_DIR, 'normalizor.yml')  # databases parameters

    @staticmethod
    def logs_cfg():
        """
        Configuration des logs
        :return:
        """
        print (CFGBases.__cfg_log)
        return CFGBases.load_cfg(CFGBases.__cfg_log)

    @staticmethod
    def app_cfg(code=None):
        """
        Parametres application
        ======================

        :param str code: clé a retourner (filtre)
        :return:
        """
        return CFGBases.load_cfg(CFGBases.__app_log, r, mode=mode)

    @staticmethod
    def smtp_cfg():
        """
        Parametres SMTP
        :return:
        """
        return CFGBases.load_cfg(CFGBases.__app_log, 'smtp_data')

    @staticmethod
    def validator(code=None):
        """
        Parametres de validation de formulaire de données

        :app str ref: référence du formulaire

        :return: parametres de configuration
        :rtype: dict
        """
        return CFGLib.load_cfg(CFGLib.cfg_validator, code)

    @staticmethod
    def normalizor():
        """
        Parametres de normaisation de données de formulaire
        :return: parametres de normaisation
        :rtype: dict
        """
        return CFGLib.load_cfg(CFGLib.cfg_normalizor)

    @staticmethod
    def mailing_lib(ref=None):
        """
            Mail standard

            :app str ref: référence du mail

            :return: mail
            :rtype: dict
            """
        return CFGLib.load_cfg(CFGLib.mail_sender, ref)

    @staticmethod
    def categorie_lib():
        """
            Mail standard

            :app str ref: référence du mail

            :return: mail
            :rtype: dict
            """
        return CFGLib.load_cfg(CFGLib.categories)
