# !/usr/bin/python3
# -*- coding: utf-8 -*-
# app_tools.py

from source import source
from toolbox import cfgloader
from toolbox import tools

base = tools.get_dir_path()

print('[toolbox-install] Création architecture')

print('\t Répertoire configuration')
tools.makedirs(tools.path_build(base, 'cfg'))

print('\tRépertoire logs')
tools.makedirs(tools.path_build(base, 'logs'))

print('[toolbox-install] Export configuration de base')
src = tools.path_build(base,'cfg')

for files, data in source.items():
    cfgloader.save_cfg(eval(data),tools.path_build(src, files))