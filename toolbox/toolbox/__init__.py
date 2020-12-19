#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Fonctions standards (ré)ultilisables
"""

__author__ = "Ketsia LENTIN"
__copyright__ = "Copyright 2020, Couleur West IT"
__credits__ = "Ketsia LENTIN"
__license__ = "MIT"
__version__ = "1.0.1"
__email__ = "contact@couleurwest-it"
__status__ = "Production"
__docformat__ = 'reStructuredText'

from toolbox import tools
from toolbox.cfgmng import CFGBases as cfgloader
from toolbox.logmng import CTracker as tracker

if __name__ == "__main__":
    import doctest
    doctest.testmod()