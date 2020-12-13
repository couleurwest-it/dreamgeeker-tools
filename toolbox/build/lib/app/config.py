from app import tools
from app.logmng import CTracker


def CConfig():

    tools.PROJECT_DIR = tools.get_my_path()


    APP_NAME = 'app'
    APP_DIR = tools.path_build(tools.PROJECT_DIR, APP_NAME)
    TMP_DIR = tools.path_build(tools.PROJECT_DIR, 'tmp')


    CTracker.config('PROD')

    def __init__():
        print (tools.get_dir_path())
        print(tools.get_my_path())