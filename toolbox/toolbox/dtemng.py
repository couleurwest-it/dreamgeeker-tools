#!/usr/bin/env python
# -*- coding: utf-8 -*-
# toolbox/dtemng.py

"""Gestionnaire standard de dates"""

import locale
import time
from datetime import datetime, timedelta, date

import pytz

I_MON, I_TUES, I_WED,I_THU, I_FRI, I_SAT, I_SUN = 1, 2, 3, 4,5,6,7

locale.setlocale(locale.LC_TIME, 'fr_FR.utf8')

ISO_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'
FR_FORMAT = '%d/%m%/%Y'

FRM_ISO, FRM_TIMESTAMP = 'iso', 'ts'


def set_timezone(dt, tz=pytz.UTC):
    """
    Applique la timezone indiquée à la date passé en parametre
    =========================================================

    :param date dt: date
    :param timezone tz: timezone
    """
    return dt.replace(tzinfo=tz)


def datetime_from_utc_to_local(utc_datetime):
    """
    :param utc_datetime:
    :return:
    """
    return pytz.utc.localize(utc_datetime, is_dst=None).astimezone()


def datetime_from_local_to_utc(utc_datetime):
    """

    :param utc_datetime:
    :return:
    """
    return utc_datetime.astimezone(pytz.utc)

def maintenant(utc=False, fm=None, tz=None):
    """maintenant module
        ==============
        Date et heure du jour

        :param bool p_iso: renvoie de la date du jour au format iso or not
        :rtype: datetime | string

        :Example:
        ---------

        >>> maintenant ()
        datetime.datetime (2019, 06, 02, 17, 30, 43, 248622)
        >>> maintenant (True)
        '2019-06-02T17:30:43.248622'
    """
    d = datetime.utcnow()
    if not utc:
        d = pytz.utc.localize(d, is_dst=None).astimezone(tz)

    if fm == FRM_ISO:
        return d.isoformat()
    elif fm == FRM_TIMESTAMP:
        return dtets(d)
    else:
        return d

def utcnow_iso():
    """
    Date et heure actuelle utc au format iso
    :return: date utc
    """
    return maintenant(True, FRM_ISO)

def utcnow_ts():
    """
    Date et heure actuelle utc au format timestamp
    :return: timestamp
    """
    return maintenant(True, FRM_TIMESTAMP)

def datestr(dte=None, fm='%Y-%m-%dT%H:%M:%S'):
    """datestr module

    Convertit une date en chaine selon un format donnée

    :param date dte: date à convertir

    :param str fm: format désirée, defaults to  '%d/%m/%Y'

    :return: Renvoie un chaine correspondant au format date passé en parametre
    :rtype: str

    :example:
    ---------

    >>> d = maintenant ()
    >>> datestr (d, '%d.%m.%Y')
    02.06.2019
    """
    try:
        if datestr() is None:
            dte=maintenant()
        return dte.strftime(fm)
    except:
        return None

def today(fm='%d/%m/%Y'):
    """
        dttoday module
        ==============
        Renvoie la date actuelle

        :rtype: str

        :Example:
        ---------

        >>> today ()
        '02/06/2019'

        >>> today('%d.%m.%Y')
        '02.06.2019'
        """
    return datestr(fm)

def date_dayed(dte=None, b=True):
    """
    REnvoie debut ou fin de journée
    :param datetime.datetime dte:     date à dtets
    :param bool b: Date debut de jour (00:00:00.000) ou date de fin de journee date du jour + 1 (minuit) soit lendemin à 00
    :return:
    """
    if dte is None:
        dte = maintenant()

    dte = dte.replace(hour=0, minute=0, second=0, microsecond=0)

    return dte if b  else dateadd(dte, 1)

def get_time(dte):
    """
    Renvoie d'une date au format time
    :param date dte:
    :rtinme: int
    """
    return dte.time()

def get_date(p_year, p_month, p_day):
    """
    Generationd'une date a partir des valeur numerique
    :param int p_year:
    :param int p_month:
    :param int p_day:
    :rtype: date
    """
    return date(p_year, p_month, p_day)

""" 
Convert function
"""
def tsdate(ts):
    """
    Conversion timestamp - date
    ==============================================

        :param ts: temps en milliseconde depuis 1970
        :return: date
    """
    return datetime.fromtimestamp(int(ts))  # => renvoie datetime

def tstring(v, fm='%Y.%m.%d-%H:%M (%a)'):
    """
     Conversion timestamp - chaine(str)
     ==============================================
    """
    return datestr(tsdate(v), fm)

def dtets(dte=None):
    """
    Conversion date - timestamp
    ==============================================*
    
    Parametres
    ------------
    :param date dt: date à convertir
    :return int: date en miliseconde (sans les ms)
    """
    if dte is None:
        dte = maintenant()

    return int(dte.timestamp())  # int => sans les ms

def strdate(dt, pt='%d-%m-%Y %H:%M:%S'):
    """
    Conversion string - date
    ==============================================
    :param str dt: date
    :param str pt, default '%d-%m-%Y %H:%M:%S': patterne, optional

    :return: Renvoie la date convertit ou None en cas d'invalidité (date non conform)
    :rtype: datetime

    :Exemple:

    >>> s = '24-O2-1976 16:45'
    >>> strdate (s, '%d-%m-%Y %H:%m')
    datetime.datetime(1976,02,24,16,45)
    """
    return datetime.strptime(dt, pt)

def isotodate(s_iso):
    """
    Conversion str_iso - date
    ==============================================

    Format ISO : YYYY-MM-DDTHH:MN
    :param p_dte:

    :return:
    """
    return strdate(s_iso, pt='%Y-%m-%dT%H:%M:%S')

""" 
   features function
"""

def datepaques(an):
    """
    Calcul Pâques d'une année donnée
    ===================================================

    * Lundi de paque : lundi suivant le dimanche de paque (La Pâque)
    * Jeudi de l'ascension : 3 jour après paques
    * pentecote : 49 jours après le lundi de paques

    :param: année de référence
    :return: un tableau contenant (date du lundi de paque, jeudi de l'ascension, lundi de pentecote)
    """

    a = an // 100
    b = an % 100

    c = (3 * (a + 25)) // 4
    d = (3 * (a + 25)) % 4
    e = (8 * (a + 11)) // 25

    f = (5 * a + b) % 19
    g = (19 * f + c - e) % 30
    h = (f + 11 * g) // 319

    j = (60 * (5 - d) + b) // 4
    k = (60 * (5 - d) + b) % 4

    m = (2 * j - k - g + h) % 7
    n = (g - h + m + 114) // 31
    p = (g - h + m + 114) % 31

    jour = p + 1

    mois = n

    dte_paques = date(an, mois, jour)
    lundi_pak = dte_paques + timedelta(days=1)
    jeudi_ascension = dte_paques + timedelta(days=39)
    pentecote = lundi_pak + timedelta(days=49)

    return [dte_paques, lundi_pak, jeudi_ascension, pentecote]

def jours_feries(pi_year=None):
    """
    Jour fériés pour une date donnée
    =================================

    :param int pi_year: Année de référence (optionnel)

    :Exemple:
    ----------------------------------------------------
    >>> jours_feries ()		#Jours fériés année en cours
    >>> jours_feries (2018)	# jours fériés année 2018

    :return: un tableau de date de jours fériés
    """

    an = maintenant().year if pi_year is None else pi_year

    dt_feries = datepaques(an)

    dt_feries.append(date(an, 1, 1))  # jour de l'an
    dt_feries.append(date(an, 5, 1))  # fete du travail
    dt_feries.append(date(an, 5, 8))  # jour victoire
    dt_feries.append(date(an, 7, 14))  # fete national
    dt_feries.append(date(an, 8, 15))  # assomption
    dt_feries.append(date(an, 11, 1))  # toussain
    dt_feries.append(date(an, 11, 1))  # armistice
    dt_feries.append(date(an, 12, 25))  # noel

    return dt_feries

def is_workday(dte):
    """
    Determine si la date est un jour ouvré ou vaqué (week-end / fériés)

    :param dte: date à évaluer
    :return: renvoie le statut jour ouvré (true=ouvré)
    """
    feries = jours_feries(dte.year)
    return not (dte in feries or dte.weekday() > I_FRI)

def dateadd(dte, nb, fm='d'):
    """
    Ajoute un nombre de jours données à une date
    =============================================

    :param date dte: date de départ
    :param int nb: nombre de jour à additionner (valeur négative/positive)
    :param str fm: days (default), h (hours), m (minutes) 
    
    :return: date de depat + nombre de jours

    """
    if fm == 'h':
        return dte + timedelta(hours= nb)
    elif fm == 'm':
        return dte + timedelta(minutes=nb)
    else:
        return dte + timedelta(days=nb)

def timeadd(dte, nb):
    """
    Ajoute un nombre de jours données à une date
    ===================================================

    Parametres
    ----------

    :param date dte: date de départ
    :param int nb: nombre de jour à additionner (valeur négative/positive)

    :return: date de depat + nombre de jours

    """
    return dateadd(dte, nb, 'h')

def date_add_workday(dte, nb):
    """
        Ajoute un nombre de jours ouvrés donnés à une date
        ===================================================

        Parametres
        ----------
        :param: date dte: date de référence
        :param int nb: nombre de jour à additionner (valeur négative/positive)
        :return: date de depat + nombre de jours
    """
    while nb > 0:
        dte = dateadd(dte, 1)
        if is_workday(dte): nb -= 1

    return dte

def dtediff(p_date1, p_date2):
    """
    Calcul du nombre de jours entre deux dates
    =============================================

    Parametres
    --------------------------------
    :param p_date1: date à comparer
    :param p_date2: date à comparer
    """
    t = p_date2 - p_date1
    return abs(t.days)

def get_weeks_num(dte=None):
    """Renvoie le numéro de la date indiqué (now par deafut)"""
    if dte is None:
        dte = maintenant()

    return dte.isocalendar()[1]

def fullmonth(dte):
    """
    Renvoie la date du jour au format MOIS YYYY
    :param date dte:
    :rtype: str
    """
    return datestr(dte, "%B %Y")

def date_rss(dte=None):
    ctime = time if dte is None else time.mktime(dte.timetuple())
    return ctime.strftime('%a, %d %b %Y %H:%M:%S %z')


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