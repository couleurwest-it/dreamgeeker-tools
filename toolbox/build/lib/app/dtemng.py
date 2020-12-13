#!/usr/bin/env python
# -*- coding: utf-8 -*-
# toolbox/dtemng.py

"""Gestionnaire standard de dates"""

import locale
import time

import pytz
from datetime import datetime, timedelta, date

locale.setlocale(locale.LC_TIME, 'fr_FR.utf8')
TZ_GF = pytz.timezone('America/Cayenne')
TZ_FR = pytz.timezone('Europe/paris')

ISO_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'
FR_FORMAT = '%d/%m%/%Y'

I_MONDAY, I_TUESDAY, I_WEDNESDAY, I_THURSDAY, I_FRIDAY, I_SATURDAY, I_SUNDAY = 0, 1, 2, 3, 4, 5, 6
FRM_ISO, FRM_TIMESTAMP = 'iso', 'ts'


def set_timezone(dt, tz=pytz.utc):
    """
    Applique la timezone indiquée à la date passé en parametre

    """
    return dt.replace(tzinfo=tz)


def datetime_from_utc_to_local(utc_datetime):
    """
    :param utc_datetime:
    :return:
    """
    return pytz.utc.localize(utc_datetime, is_dst=None).astimezone()


def datetime_from_gf_to_local(utc_datetime):
    """
    Convertit une date gf en date utc
    :app datetime utc_datetime: date gf
    :return: date utc
    """
    return TZ_GF.localize(utc_datetime, is_dst=None).astimezone()


def datetime_from_utc_to_gf(utc_datetime):
    """
    Convertit une date utc en date gf
    :app datetime utc_datetime: date utc
    :return: date gf
    """
    return pytz.utc.localize(utc_datetime, is_dst=None).astimezone(TZ_GF)


def datetime_from_local_to_utc(utc_datetime):
    """

    :param utc_datetime:
    :return:
    """
    return utc_datetime.astimezone(pytz.utc)


def datetime_from_local_to_gf(local_datetime):
    """

    :param local_datetime:
    :return:
    """
    return local_datetime.astimezone(TZ_GF)


def datetime_from_gf_to_utc(utc_datetime):
    """

    :param utc_datetime:
    :return:
    """
    return TZ_GF.localize(utc_datetime, is_dst=None).astimezone(pytz.utc)


def timestamper(p_dt):
    """
        Conversion de la date  au format timestamp

        :app p_dt: date à convertir
        :return: date en miliseconde (sans les ms)
    """
    return int(p_dt.timestamp())  # int => sans les ms


# getters function
def dte_now(utc=False, fm=None, tz=None):
    """dte_now module
        ==============
        Date et heure du jour

        :app bool p_iso: renvoie de la date du jour au format iso or not
        :rtype: datetime | string

        :Example:
        ---------

        >>> dte_now ()
        datetime.datetime (2019, 06, 02, 17, 30, 43, 248622)

        >>> dte_now (True)
        '2019-06-02T17:30:43.248622'
    """
    d = datetime.utcnow()
    if not utc:
        d = pytz.utc.localize(d, is_dst=None).astimezone(tz)

    if fm == FRM_ISO:
        return d.isoformat()
    elif fm == FRM_TIMESTAMP:
        return timestamper(d)
    else:
        return d


def gf_now(fm=None):
    """
    GF Now
    ======================

    Renvoie la date du jour de Guyane FR

    :app p_iso: Format iso or not

    :rtype: datetime.datetime
    """

    return dte_now(fm=fm, tz=TZ_GF)


def utcnow_iso():
    """
    Date et heure actuelle utc au format iso
    :return: date utc
    """
    return dte_now(True, FRM_ISO)


def utcnow_ts():
    """
    Date et heure actuelle utc au format timestamp
    :return: timestamp
    """
    return dte_now(True, FRM_TIMESTAMP)


def gfnow_iso():
    """

    :return:
    """
    return gf_now(FRM_ISO)


def gfnow_ts():
    """

    :return:
    """
    return gf_now(FRM_TIMESTAMP)


def dttoday(fm='%Y-%m-%d'):
    """
        dttoday module
        ==============
        Renvoie la date actuelle

        :rtype: str

        :Example:
        ---------

        >>> dttoday ()
        '02/06/2019'

        >>> dttoday('%d.%m.%Y')
        '02.06.2019'
        """
    return dtetostr(dte_now(), fm)


def gf_today(fm='%Y-%m-%d'):
    """
        dttoday module
        ==============
        Renvoie la date actuelle

        :rtype: str

        :Example:
        ---------

        >>> dttoday ()
        '02/06/2019'

        >>> dttoday('%d.%m.%Y')
        '02.06.2019'
        """
    return dtetostr(gf_now(), fm)


def date_dayed(dte=None, b=True):
    """
    REnvoie debut ou fin de journée
    :app datetime.datetime dte:     date à timestamper
    :app bool b: Date debut de jour (00:00:00.000) ou date de fin de journee (23:59:59.999) soit lendemin à 00
    :return:
    """
    if dte is None:
        dte = dte_now()

    if b:
        return dte.replace(hour=0, minute=0, second=0, microsecond=0)
    else:
        return dte.replace(hour=23, minute=59, second=59, microsecond=0)


def day_stamped(dte=None):
    """
    Transformation d'un date en un timestamp
    :app datetime.datetime dte:     date à timestamper
    :app bool b: Date debut de jour (00:00:00.000) ou date de fin de journee (23:59:59.999)
    :return:
    """
    if dte is None:
        dte = dte_now()

    return timestamper(dte)


def dttime(pdte):
    """

    :param pdte:
    :return:
    """
    return pdte.time()


def get_date(p_year, p_month, p_day):
    """

    :param p_year:
    :param p_month:
    :param p_day:
    :return:
    """
    return date(p_year, p_month, p_day)


""" 
---- Convert function
"""


def tsdatser(v):
    return dtetostr(tstodte(v), '%Y.%m.%d-%H:%M (%a)')


def tstodte(p_timestamp):
    """
        Conversion de la date  partir d'un timestamp

        :app p_timestamp: temps en milliseconde depuis 1970
        :return: date
    """
    return datetime.fromtimestamp(int(p_timestamp))  # => renvoie datetime


def dtetostr(pdte, fm='%Y-%m-%dT%H:%M:%S'):
    """dtetostr module

    Convertit une date en chaine selon un format donnée

    :app pdte: date à convertir
    :type pdte: date

    :app fm: format désirée, defaults to  '%d/%m/%Y'
    :type fm: str, optional

    :return: Renvoie un chaine correspondant au format date passé en parametre
    :rtype: str

    :example:
    ---------

    >>> d = dte_now ()
    >>> dtetostr (d, '%d.%m.%Y')
    02.06.2019
    """
    try:
        return pdte.strftime(fm)
    except:
        return None


def strtodate(dt, pt='%d-%m-%Y %H:%M:%S'):
    """
    Conversion d'une chaine en format date

    :app str ds: date au format chaine
    :app str pt, default '%d-%m-%Y %H:%M:%S': patterne, optional

    :return: Renvoie la date convertit ou None en cas d'invalidité (date non conform)
    :rtype: datetime

    :Exemple:

    >>> s = '24-O2-1976 16:45'
    >>> strtodate (s, '%d-%m-%Y %H:%m')
    datetime.datetime(1976,02,24,16,45)
    """
    return datetime.strptime(dt, pt)


def get_hours(dte):
    """

    :param dte:
    :return:
    """
    return dtetostr(dte, fm='%H:%M')


def isotodate(s_iso):
    """
        Conversion d'une chaine date au format iso en date

        Format ISO : YYYY-MM-DDTHH:MN
        :app p_dte:

        :return:
    """
    return strtodate(s_iso, pt='%Y-%m-%dT%H:%M:%S')


def isostamper(s_iso):
    """

    :param s_iso:
    :return:
    """
    return timestamper(isotodate(s_iso))


""" 
   features function
"""


def is_workday(dte):
    """
    Determine si la date est un jour ouvré ou vaqué (week-end / fériés)

    :app dte: date à évaluer
    :return: renvoie le statut jour ouvré (true=ouvré)
    """
    feries = jours_feries(dte.year)
    return not (dte in feries or dte.weekday() > I_FRIDAY)


def dateadd(p_dt, nb_days):
    """
        Ajoute un nombre de jours données à une date

        :app p_dt: date de départ
        :type p_dt: datetime
        :app nb_days: nombre de jour à additionner (valeur négative/positive)
        :type nb_days: entier

        :return: date de depat + nombre de jours

    """

    return p_dt + timedelta(days=int(nb_days))


def timeadd(p_dt, nb_hours):
    """
        Ajoute un nombre de jours données à une date

        :app date p_dt: date de départ
        :app int nb_hours: nombre de jour à additionner (valeur négative/positive)

        :return: date de depat + nombre de jours

    """
    return p_dt + timedelta(hours=nb_hours)


def dtediff(p_date1, p_date2):
    """
        Calcul du nombre de jours entre deux dates

        :app p_date1: date à comparer
        :app p_date2: date à comparer

    """
    t = p_date2 - p_date1

    return abs(t.days)


# jours féries
def datepaques(an):
    """
        Calcule des dates de Pâques d'une année donnée

        * Lundi de paque : lundi suivant le dimanche de paque (La Pâque)
        * Jeudi de l'ascension : 3 jour après paques
        * pentecote : 49 jours après le lundi de paques

         :app: année de référence
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
        Référencie tous les jours fériés de France

        :app pi_year: Année de référence (optionnel)

        :Exemple:
        ==========
        >>> jours_feries ()		#Jours fériés année en cours
        >>> jours_feries (2018)	# jours fériés année 2018

        :return: un tableau de date de jours fériés
    """

    an = dte_now().year if pi_year is None else pi_year

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


def date_add_workday(dte_start, nb_days):
    """
        Ajoute un nombre de jours ouvrés donnés à une date

        :app: date de départ
        :app: nombre de jour à additionner (valeur négative/positive)
        :return: date de depat + nombre de jours
    """
    while nb_days > 0:
        dte_start = dateadd(dte_start, 1)

        if is_workday(dte_start): nb_days -= 1
    return dte_start


def get_weeks_num(dte=None):
    """Renvoie le numéro de la date indiqué (now par deafut)"""
    if dte is None:
        dte = dte_now()

    return dte.isocalendar()[1]


def get_fullmonth(dte):
    """

    :param dte:
    :return:
    """
    return dtetostr(dte, "%B %Y")


def pub_date(dte=None):
    ctime = time if dte is None else time.mktime(dte.timetuple())
    return ctime.strftime('%a, %d %b %Y %H:%M:%S %z')
