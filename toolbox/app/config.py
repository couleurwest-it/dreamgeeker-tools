from app import tools
from app.logmng import CTracker


class CConfig():

    def __init__(self, app):
        print ('\n==============================')
        tools.APP_NAME = app

        tools.PROJECT_DIR = tools.get_dir_path()
        tools.APP_DIR = tools.path_build(tools.PROJECT_DIR, tools.APP_NAME)
        tools.TMP_DIR = tools.path_build(tools.PROJECT_DIR, 'tmp')

        CTracker.config('PROD')
