# !/usr/bin/python3
# -*- coding: utf-8 -*-
# toolbox/logmng.py
"""
Gestion des logs
"""
import logging
import logging.config as log_config

from .cfgmng import CFGBases as toolsconfig


class CReponder(object):
    def __init__(self, status=200, data=None, msg=None):
        """

        :type status: int, default 200
        :app data:
        :app msg:
        """
        self.status = status
        self.data = data
        self.message = msg

    def set(self, status, data=None, msg=None):
        self.status = status
        self.data = data
        self.message = msg

    @property
    def status_ok(self):
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
        :app int status: status code
        :app str message: message d'erreur
        :app str title: titre
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
            log_config.dictConfig(toolsconfig.logs_cfg())
            CTracker.tracker = logging.getLogger(mode)
        except Exception as e:
            tools.print_err(e, ': ', 'Error in Logging Configuration. Using default configs')
            logging.basicConfig(level=logging.NOTSET)

    @staticmethod
    def msg_tracking(msg, title, log_level=logging.INFO, code=''):
        """
        Tracking message
        :app str msg: message à ecrire dans logs
        :app str title: Titre ou référence associé au message
        :app log_level: LOG LEVEL Niveau de l'alert (DEBUG | INFO | WARN | )
        :app code: Code numérique
        """
        CTracker.tracker.log(log_level, msg, extra={'title': title, 'code': code})

    @staticmethod
    def alert_tracking(msg, title, code=''):
        """
            Message d'alerte (WARNING)
            ==============================================================
            :app str msg: message à ecrire dans logs
            :app str title: Titre ou référence associé au message
            :app code: Code numérique
            """
        msg_tracking(msg, title, logging.WARNING, code)

    @staticmethod
    def info_tracking(msg, title, code=''):
        """
        Message d'info (INFO)
        ==============================================================
        :app str msg: message à ecrire dans logs
        :app str title: Titre ou référence associé au message
        :app code: Code numérique
        """
        msg_tracking(msg, title, logging.INFO, code)

    @staticmethod
    def error_tracking(msg, title, code=500):
        """
        Message d'error (ERROR)
        ==============================================================
        :app str msg: message à ecrire dans logs
        :app str title: Titre ou référence associé au message
        :app int code: Code numérique
        """
        msg_tracking(msg, title, logging.ERROR, code)

    @staticmethod
    def critical_tracking(msg, title, code=''):
        """
        Message dcritique (CRITIQUE)
        ==============================================================
        :app str msg: message à ecrire dans logs
        :app str title: Titre ou référence associé au message
        :app code: Code numérique
        """
        msg_tracking(msg, title, logging.CRITICAL, code)

    @staticmethod
    def track_step(trace):
        """
        Last Action for error treatmant
        :param str:trace
        """
        CTracker.LOG_TRACKED = trace

    @staticmethod
    def exception_tracking(ex, title):
        if CTracker.LOG_TRACKED != '':
            msg_tracking(CTracker.LOG_TRACKED, title, logging.INFO)
            CTracker.LOG_TRACKED = ''

        try:
            if isinstance(ex, CError):
                error_tracking(ex.message, ex.title, code=ex.status)
                return ex
            else:
                error_tracking(ex.__str__(), title)
                return CError(ex.__str__(), 500, title)

        except Exception as sex:
            tools.print_err('Erreur d\'origine : ', ex)
            tools.print_err('Erreur intercepte : ', sex)
            return CError(status=500)

    @staticmethod
    def try_fn(callback, action, *args, **kwargs):
        """

        :param callback:
        :param action:
        :param args:
        :param kwargs:
        :return:
        """
        try:
            track_it('{}'.format(action))
            status = kwargs.get('status', 200)

            if kwargs.get('status'): del kwargs['status']
            r = callback(*args, **kwargs)

            return r if isinstance(r, CReponder) else CReponder(status, r)

        except Exception as ex:
            return exception_tracking(ex, action)
