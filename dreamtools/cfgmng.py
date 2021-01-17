# -*- coding: utf-8 -*-
# cfgmng.py

"""
Gestion fichiers de configurations (YAML)

pathfile : dreamtools/cfgmng.py

Repertoires par défaut
----------------------
.. note::
    * DIRPROJECT/cfg/DIRPROJECT/cfg/.log.yml : Fichier de configuration des logs
    * DIRPROJECT/cfg/.app.yml : Fichier de configuration de l'application
    * DIRPROJECT/cfg/categorie.yml : Fichier de liste définie par un code et un libelle
    * DIRPROJECT/cfg/mailing.yml : Fichier de mails préparés
    * DIRPROJECT/cfg/validators.yml : Fichier de validation(cf CERBERUS)
    * DIRPROJECT/cfg/normalizor.yml : Fichier de normalization(cf CERBERUS)

Class CFBases
-------------
"""

import yaml

try:
    from yaml import CLoader as Loader, CDumper as Dumper, CSafeLoader as SafeLoader
except ImportError:
    from yaml import Loader, Dumper, SafeLoader

from . import tools


class CFGEngine(object):
    """
    cfg engine
    """
    __dirpath = None

    @staticmethod
    def initial(baz_dir='cfg'):
        """

        :param str baz_dir:
        :return:
        """
        CFGEngine.__dirpath = tools.path_build(tools.DIRPROJECT, baz_dir)

    @staticmethod
    def working_directory(sub_dir):
        CFGEngine.initial()
        return tools.path_build(CFGEngine.__dirpath, sub_dir)

    @staticmethod
    def loading(p, ref=None, m='r'):
        """
        Récupération des parametres de configuration du fichier <p> section <r>

        :param str p: Fichier de configuration
        :param str ref: référence parametres à récupérer, optionnel
        :param str m: bytes par defaut
        :return: configuration | None

        """
        config = None

        try:
            if tools.file_exists(p):
                with open(p, mode=m) if 'b' in m else open(p, mode=m, encoding='utf-8') as cfg:
                    cfg = yaml.load(cfg, Loader=SafeLoader)
                    if type(cfg).__name__ == "dict":
                        cfg = dict(cfg)
                    elif type(cfg).__name__ == "list":
                        cfg = list(cfg)

                    config = cfg.get(ref) if ref else cfg
        except Exception as ex:
            print(f'[Chargement du fichier {p}:\n', ex)
        finally:
            return config

    @staticmethod
    def saving(d, f, m="w"):
        """
        Enregistrement d' un fichier
        ========================================

        :param dict(str, list(str)) d: données à enregistrer
        :param str f: nom du fichier
        :param str m: default (write): mode "w|a", optional
        :return:
        """
        tools.makedirs(tools.dirparent(f))

        with open(f, m) if 'b' in m else open(f, mode=m, encoding='utf-8') as f_yml:
            yaml.dump(d, stream=f_yml, allow_unicode=True)

        return f


class CFGBases(CFGEngine):
    """
    Cette class permet de gere des fichiers de configuration disponibles dans le repertoire <PROJET_DIR>/cfg
    """
    __directory__ = CFGEngine.working_directory('')  # databases parameters
    _logs = tools.path_build(__directory__, 'log.yml')
    _app = tools.path_build(__directory__, 'app.yml')
    _categories = tools.path_build(__directory__, 'categorie.yml')
    _mail = tools.path_build(__directory__, 'mailing.yml')
    _validator = tools.path_build(__directory__, 'validators.yml')  # databases parameters
    _normalisator = tools.path_build(__directory__, 'normalizor.yml')  # databases parameters

    @staticmethod
    def loadingbyref(filename, *args, **kwargs):
        """
        Récupération des parametres de configuration du fichier <filepath> section <r>

        :param str filename: Nom fichier sans extension
        :return: configuration | None
        """
        filepath = tools.path_build(CFGBases.__directory__, f'{filename}.yml')
        return CFGEngine.loading(filepath, *args, **kwargs)

    @staticmethod
    def savingbyref(datas, filename, *args, **kwargs):
        """
        Récupération des parametres de configuration du fichier <filepath> section <r>

        :param str filename: Fichier de configuration
        """
        filepath = tools.path_build(CFGBases.__directory__, f'{filename}.yml')
        return CFGEngine.saving(datas, filepath, *args, **kwargs)


    @staticmethod
    def loadcfglogs():
        """ Configuration des logs

        :Exemple:
            >>> import import logging.config as log_config
            >>> import logging
            >>> log_config.dictConfig(CFGBases.loadcfglogs())
            >>> tracker = logging.getLogger('PROD|TEST')
            >>> tracker.info("Exemple dun message d'information")

        """

        return CFGBases.loading(CFGBases._logs)

    @staticmethod
    def loadcfgapp(code=None):
        """ Parametres application

        :param str code: clé a retourner (filtre)
        :return: Configuration
        """
        return CFGBases.loading(CFGBases._app, code)

    @staticmethod
    def loadcfgvalidator():
        """ Parametres de validation de formulaire
        """
        return CFGBases.loading(CFGBases._validator)

    @staticmethod
    def lloadcfgnormalizor():
        """ Parametres de normalisation de formulaire
        :return: parametres de normaisation
        :rtype: dict
        """
        return CFGBases.loading(CFGBases._normalisator)

    @staticmethod
    def loadcfgmailing(code):
        """ Mail préparé

        :param str code: référence du mail à envoyer
        :return: mail

        """
        return CFGBases.loading(CFGBases._mail, code)

    @staticmethod
    def loadcategories(code=None):
        """ Liste de definition

        :param str code: référence du de la liste
        :return: liste(s) de categories
        :rtype: dict
        """
        return CFGBases.loading(CFGBases._categories, code)


_all_ = ['CFGBases']
