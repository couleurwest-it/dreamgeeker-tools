#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# toolbox.py

"""
   Bibliotheque de fonctions
"""

import ast
import fnmatch
import os
import re
import sys
from random import choice, randint
from string import punctuation, ascii_letters, digits

import requests

""""constantes"""
LOGS_CODE_INFO, LOGS_CODE_WRN, LOGS_CODE_ERR, LOGS_CODE_HARD = 20, 30, 40, 50
STR_ACCENT = 'àâäãéèêëîïìôöòõùüûÿñç'
STR_ENABLED_PUNC = r'@#!?$&-_'
RGX_PASSWORD = r'^.*(?=.{8,12})(?=.*[' + STR_ACCENT + 'a-z])(?=.*[A-Z])(?=.*\d)(?=.*[' + STR_ENABLED_PUNC + ']).*'
RGX_GF_PHONE = r'^0([679]\d{8}|594\d{6})$'
RGX_PHONE = r'^0[1-9]\d{8}$'
RGX_EMAIL = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
RGX_URL = r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)'
LIST_MEDIA_LINK = {
    "dailymotion": "https://www.dailymotion.com/video/{}",
    "youtube": "https://www.youtube.com/watch?v={}",
    "soundcloud": "https://api.soundcloud.com/tracks/{}"
}
RGX_MEDIA_LINK = re.compile(
    '((?P<dailymotion>dai.ly|dailymotion)|(?P<youtube>youtu.be|youtube)|(?P<soundcloud>soundcloud))')
RGX_MEDIA_DOMAIN = r'domaim=[.]((?P=domain)youtube|dailymotion|soundcloud).com'
PROJECT_DIR = ''
"""fonctions"""


def print_err(*args, **kwargs):
    """
    Ecriture sur le flux erreur de la console

    :app args: arguments 1
    :app kwargs: arguemnts2
    """
    print(*args, file=sys.stderr, **kwargs)


def string_me(ch):
    """
    Convertion d'une valeur en chaine
    :param chaine:
    :rtype: str
    """

    try:
        return str(ch)
    except:
        return None


def clean_space(chaine):
    """
        clean_space module :
        ====================

        Nettoyage des espaces "superflus"

        :Exemple:
        --------

        >>> chaine = 'Se  réveiller au matin        (ou pas) de sa destiné !'
        >>> clean_space (chaine)
        'Se réveiller au matin (ou pas) de sa destiné !'


        >>> clean_space (s, True)
        'Se reveiller au matin ou pas de sa destine'
    """
    s = string_me(chaine)
    return re.sub(r'[ ][ ]+', ' ', s.strip())


def clean_allspace(chaine):
    """
        clean_allspace module :
        ====================

        Nettoyage de tous les espaces

        :Exemple:
        --------

        >>> chaine = 'Se  réveiller au matin        (ou pas) de sa destiné !'
        >>> clean_allspace (chaine)
        'Seréveilleraumatin(oupas)desadestiné!
        '
    """

    s = string_me(chaine)
    return re.sub(r'\s', '', s.strip())


def clean_coma(chaine, pb_punk=False):
    """
        clean_coma module
        ==================

        Supprime les accents/caractères spéciaux du texte source en respectant la casse

        :app chaine: Chaine de caractere à "nettoyer"
        :app pb_punk: indique si la punctuation est à nettoyer ou pas (suppression)

        :Exemple:
        --------

        >>> s = 'Se  réveiller au matin  (ou pas) de sa destiné !'
        >>> clean_coma (s)
        'Se seveiller au matin (ou pas) de sa destine !''

        >>> clean_coma (s, True)
        'Se reveiller au matin ou pas de sa destine'
    """

    if pb_punk:
        # Nettoyage caractere spéciaux (espace...)
        o_rules = str.maketrans(STR_ACCENT, 'aaaaeeeeiiioooouuuync', punctuation)
    else:
        o_rules = str.maketrans(STR_ACCENT, 'aaaaeeeeiiioooouuuync')

    return clean_space(chaine).translate(o_rules).swapcase().translate(o_rules).swapcase()


def clean_master(chaine):
    """
        clean_master module
        ==================

        Supprime les accents, caractères spéciaux et espace du texte source

        :app chaine: Chaine de caractere à "nettoyer"

        :Exemple:
        --------

        >>> s = 'Se  réveiller au matin  (ou pas) de sa destiné !'
        >>> clean_master (s)
        'Sereveilleraumatinoupasdesadestine

    """
    return clean_allspace(clean_coma(chaine, True)).lower()


def inttohex(v):
    """
    STRING TO HEXADECIMAL
   ============================================
    Conversion d'un entier en hexadécimal

    **Parameters**
    ----------------------------------------------
    :app int v: nombre à convertir

    :return : valeur en hexadécimal
    :rtype: srt
    """
    return hex(int(v))


def addhex(h, v):
    """
    ADD HEXADECIMAL
    ============================================

    :app str h: valeur hexadécimal
    :app str v: valeur entière à ajouter

    :return: valeur additionné en hexedécimal
    """
    v += int(h, 16)
    return hex(v)


def plain_hex(hx, s=3):
    """
    COMPLETE HEx
    ============================================
    Complète un chiffre hexadecimal en préfixant une valeur de zéro

    **Parameter**
    ------------------------------------------
    :app str hx: valeur hexadécimal
    :app int v: longeur chaine attendu

    :rtype: str:

    :Examples:
    ------------------------------------------
    :app str hx: valeur hexadécimal
    :app int v: longeur chaine attendu

    :rtype: str
    """
    return plain_zero(hx[2:], s)


def plain_zero(v, s):
    """Complete une valeur chaine de zéro

    :param v: valeur à completer
    :param s: taille chaine attendu préfixé de zerom

    Example
    >>> d = 5
    >>> plain_zero(5,3)
    >>> '005'
    """
    s = '{:0>' + str(s) + '}'
    return s.format(v)


# =========================================Analyse chaine
def check_password(s):
    """
    Vérifie que la syntaxe d'une chaine répond au critère d'un mot de passe
    :param str s: chaine à vérifier

    :PARAMATRES:
     :
        * Une majuscule
        * Une minuscule
        * Un chiffre
        * Un carectère spécial (@#!?$&-_ autorisé )

        :app str s: chaine de caractère

        :return bool: True si la chaine est valide
    """
    r = re.compile(RGX_PASSWORD)
    return r.match(s)


def check_mail(s):
    """
    CHECK MAIL
    ====================================
    Vérifie que la syntaxe d'une chaine correspond à la syntaxe d'une addresse mail :

    **Parameters**
    -----------------------------
    :app str s: chaine à évaluer
    :app bool b: avec ou sans vérifiaction de validité

    :rtype: bool
    """
    s = clean_space(s).lower()

    return re.match(RGX_EMAIL, s)


def comphex(hx_a, hx_b):
    """
    Compare hexadécimales
    ===========================================
    Compare deux valeur hexadécimal :
        * 0 : hx_a == hx_b
        * 1 : hx_a > hx_b
        * -1 : hx_a < hx_b

    **Parameters**
    --------------
    :app str hx_a:
    :app str hx_b:

    :rtype: int
    """
    v = int(hx_a, 16) - int(hx_b, 16)

    if v == 0:
        return 0
    else:
        return -1 if v < 0 else 1


# ========================================= Generation
def pwd_maker(i_size=8):
    """
    Passeword maker
    =================
    Génération d'un password respectant les regles de password
    """

    t = list(ascii_letters + digits + STR_ENABLED_PUNC)

    while True:
        s_chaine = ''
        for i in range(0, i_size):
            s = choice(t)
            s_chaine += s
            t.remove(s)
        if check_password(s_chaine):
            break

    return s_chaine


def code_maker(c=4):
    """
    Code maker
    =================

    Génération d'une chaine aléatoire composé de lettre et de chiffres

    :param int c: taille du code
    :rtype str:
    """
    ll = list(ascii_letters + digits)
    s = ''

    for i in range(0, c):
        s += choice(ll)

    return s


def aleatoire(end, s=1):
    """
    Aléatoire
    =================
    Génération d'un nombre aléatoire entre [1-end] => end caractère

    **Parameters**
    --------------
    :param int end: valeur maximal (paut indiquer la taille si s=1)
    :param s: valeur de départ, default to 1
    :rtype s: int, optional

    :return: Un chiffre aléatoire
"""
    return randint(s, end)


# Files function ###############################
def get_dir_path():
    """
    renvoie du repertoire de rtavail en cours
    :return:
    """
    return os.getcwd()


def path_build(ps_dir, ps_complement):
    """
    Construiction d'un pathfile
    :param ps_dir:
    :param ps_complement:
    :return:
    """
    return os.path.abspath(os.path.join(ps_dir, ps_complement))


def get_extension(ps_file):
    """
    Retrourne l'extension d'un fichier
    :param ps_file:
    :return:
    """
    return os.path.splitext(ps_file)[1]


def file_exists(fp):
    """
    Search for a file
    :param str fp: filepath
    :return:
    """
    return os.path.exists(fp)


def makedirs(path):
    """

    :param path:
    """
    if not file_exists(path):
        os.makedirs(path)


def get_parent_dir(path):
    """
    Renvoie du repertoire parent
    :param str path: repertoire
    :rtype: str
    """
    return os.path.dirname(os.path.realpath(path))


def get_my_path():
    """
    retour du repertoire pour le fichier en cours
    ============================================

    :rtype: str
    """
    return get_parent_dir(__file__)


def remove_file(p):
    """
    Suppression d'un fichier si existant
    ====================================

    :param str p: chemin complet du fichier à supprimer
    """
    if file_exists(p):
        os.remove(p)


def clean_dir(directory, pattern='*'):
    """
    Supprimes tous les fichier d'un repertoire
    =========================================

    :param str directory: chemin du repertoire
    :param string pattern: patter des fichier à supprimer (filtre)
    :return int: nombre de fichier supprimer
    """
    i_count = 0

    for root, dirs, files in os.walk(directory):
        for filename in files:
            if fnmatch.fnmatch(filename, pattern):
                f = path_build(root, filename)
                remove_file(f)
                i_count += 1
    return i_count


# datas function ###############################
def add_list(v, ll):
    """
    Ajout d'un item dans une liste avec gestion des doublons
    ==============================================================
    :app str v: valeur à ajouter
    :app list l: liste
    """
    if v not in ll:
        ll.append(v)


def dictlist(k, v, d):
    """
    Ajout d'un valeur dans une liste d'un dictionnaire
    =======================================================

    :app str k: clé dictionnaire
    :app v: valeur à ajouter
    :app dict[str, list[]] p_dic: dictionnaire
    :return:
    """
    if k is None or v is None: return

    if k not in d: d[k] = []

    add_list(v, d.get(k))


def str_dic(chaine):
    """
    Convertion d'une chaine en distionnaire
    ========================================

    :param str chaine: chaine au format "dict'
    :rtype: dic

    :Example:
    ----------
    >>> s_dic = "{'key':value}"
    >>> str_dic(chaine)
    """
    return ast.literal_eval(chaine)


def pop_dic(l_id, dic):
    """
        Suppression d'une liste d'items d'un dictionnaire
        ==================================================

        :app list[str] l_ids : liste de clé à suppriemr
        :app dict[str:object] dic: dictionaire à nettoyer

        :Example:
        ----------
        >>>
    """
    if dic:
        for s in l_id:
            if s in dic: del dic[s]


def day_in_sec(dy, ml=False):
    """
    Convertion d'un nombre de jours en secondes ou milisecondes
    :param int dy: nombre de jours
    :param bool ml: en millisecondes si True sinon en secondes, dafault False
    :return: (milli) secondes
    """

    nb = int(dy)
    # 1 jour = 24h=> heures / 1h = 60mn => nb min / 1mn = 60 sc => en secondes
    nb = nb * 24 * 60 * 60

    return nb * 1000 if ml else nb


def day_in_hour(dy):
    """
    Convertion d'un nombre de jours en secondes ou milisecondes
    :param int dy: nombre de jours
    :rtype: int
    """

    nb = int(dy)
    return nb * 24
