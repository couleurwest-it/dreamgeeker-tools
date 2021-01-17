from . import tools
from . import tracker


class CConfig:

    def __init__(self, app, mode="PROD"):
        """
        Configuration des parametres d'accès relatif au projet en cours
        ==============================================================

        Parametres
        -----------
        :param str app: Nom de l'application
        :param str[PROD|DEV] mode: PRDO ou DEV

        """

        tools.APPNAME = app
        tools.DIRPROJECT = tools.dirproject()
        tools.DIRAPP = tools.path_build(tools.DIRPROJECT, tools.APPNAME)
        tools.DIRTMP = tools.path_build(tools.DIRPROJECT, 'tmp')

        tracker.config(mode)
