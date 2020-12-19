# !/usr/bin/python3
# -*- coding: utf-8 -*-
# toolbox/logmng.py
"""
Gestion des logs
"""
import logging
import logging.config as log_config

from . import cfgloader
from . import tools


class CReponder(object):
    def __init__(self, status=200, data=None, msg=None):
        """

        :type status: int, default 200
        :param data:
        :param msg:
        """
        self.status = status
        self.data = data
        self.message = msg

    def __call__(self, status, data=None, msg=None):
        self.status = status
        self.data = data
        self.message = msg

    @property
    def ok(self):
        return 200 <= self._status < 300

    @property
    def response(self):
        return {"message": self.message, "data": self.data, 'status_code': self._status}

    @property
    def status(self):
        return self._status

    @property
    def data(self):
        return self._data

    @property
    def message(self):
        return self._msg

    @status.setter
    def status(self, v):
        self._status = v

    @message.setter
    def message(self, v):
        self._msg = v

    @data.setter
    def data(self, v):
        self._data = v


class CError(Exception, CReponder):
    """    Custum Error Generator    """

    def __init__(self, message, status, title='ERRCustom'):
        """
        Erreur personnalisée
        :param int status: status code
        :param str message: message d'erreur
        :param str title: titre
        """
        Exception.__init__(self, message)
        CReponder.__init__(self, status, msg=message)

        self.__setattr__('title', title)

    def error_json(self):
        """
        erreur au format json
        :return:
        """
        return {'error': self.message, 'info': self.errors}


class CTracker:
    LOG_TRACKED = ''

    @staticmethod
    def config(mode='PROD'):
        try:
            tools.makedirs(tools.path_build(tools.PROJECT_DIR, 'logs'))
            log_config.dictConfig(cfgloader.logs_cfg())
            CTracker.tracker = logging.getLogger(mode)
        except Exception as e:
            tools.print_err(e, ': ', 'Error in Logging Configuration. Using default configs')
            logging.basicConfig(level=logging.NOTSET)

    @staticmethod
    def msg_tracking(msg, title, log_level=logging.INFO, code=0):
        """
        Tracking message
        :param str msg: message à ecrire dans logs
        :param str title: Titre ou référence associé au message
        :param int log_level: LOG LEVEL Niveau de l'alert (DEBUG | INFO | WARN | )
        :param int code: Code numérique
        """
        logging.log(log_level, msg, extra={'title': title, 'code': code})

    @staticmethod
    def alert_tracking(msg, title, code=''):
        """
            Message d'alerte (WARNING)
            ==============================================================
            :param str msg: message à ecrire dans logs
            :param str title: Titre ou référence associé au message
            :param code: Code numérique
            """
        CTracker.msg_tracking(msg, title, logging.WARNING, code)

    @staticmethod
    def info_tracking(msg, title, code=''):
        """
        Message d'info (INFO)
        ==============================================================
        :param str msg: message à ecrire dans logs
        :param str title: Titre ou référence associé au message
        :param code: Code numérique
        """
        CTracker.msg_tracking(msg, title, logging.INFO, code)

    @staticmethod
    def error_tracking(msg, title, code=500):
        """
        Message d'error (ERROR)
        ==============================================================
        :param str msg: message à ecrire dans logs
        :param str title: Titre ou référence associé au message
        :param int code: Code numérique
        """
        CTracker.msg_tracking(msg, title, logging.ERROR, code)

    @staticmethod
    def critical_tracking(msg, title, code=''):
        """
        Message dcritique (CRITIQUE)
        ==============================================================
        :param str msg: message à ecrire dans logs
        :param str title: Titre ou référence associé au message
        :param code: Code numérique
        """
        CTracker.msg_tracking(msg, title, logging.CRITICAL, code)

    @staticmethod
    def flag(trace):
        """
        Last Action for error treatmant
        :param str:trace
        """
        CTracker.LOG_TRACKED = trace

    @staticmethod
    def exception_tracking(ex, title):
        if CTracker.LOG_TRACKED != '':
            CTracker.msg_tracking(CTracker.LOG_TRACKED, title, logging.INFO)
            CTracker.LOG_TRACKED = ''

        try:
            if isinstance(ex, CError):
                CTracker.error_tracking(ex.message, ex.title, code=ex.status)
                return ex
            else:
                CTracker.error_tracking(ex.__str__(), title)
                return CError(ex.__str__(), 500, title)
        except Exception as sex:
            tools.print_err('Erreur intercepté : ', ex)
            tools.print_err('Erreur module logmng : ', sex)
            return CError(status=500)

    @staticmethod
    def fntracker(fn, action, *args, **kwargs):
        """
        Execution d'une fonctoion avec gestions des erreurs 
        
        :param fn: fonction a executer
        :param action: Titre de l'execution pour tracabilité
        :param args: argument de la fonction
        :param kwargs: parametres supplementaire (status par defaut en cas de reussite)
        :rtype: CReponder

        :Example:
        >>> from toolbox.logmng import CTracker
        >>> def fn(param)::
        >>>     return int(param)

        >>> r = CTracker.fntracker(fn, 'Test de convertion int', 'j')
        >>> r.response
        {'message': "invalid literal for int() with base 10: 'j'", 'data': None, 'status_code': 500}

        >>> r = CTracker.fntracker(fn, 'Test de convertion int', '589321')
        >>> r.response
        {'message': None, 'data': 589321, 'status_code': 200}
        """
        try:
            CTracker.flag('{}'.format(action))
            status = kwargs.get('status', 200)

            if kwargs.get('status'): del kwargs['status']
            r = fn(*args, **kwargs)

            return r if isinstance(r, CReponder) else CReponder(status, r)

        except Exception as ex:
            return CTracker.exception_tracking(ex, action)
