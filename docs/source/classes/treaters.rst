Module de validation
=====================

Validation de formulaire.

.. note::
    Les shémas de validation sont sauvegarder dans le dossier de configuration validators
    Les schéma de normalization dans normalizator


.. automodule:: dreamtools.validata
    :members:


Gestion de mailing
========================

.. automodule:: dreamtools.mailbot
    :members:

.. autoclass:: dreamtools.mailbot.CMailer
    :members:


Traitement d'image
========================

.. automodule:: dreamtools.imagine
    :members:

.. autoclass:: dreamtools.imagine.CImagine
    :members:


Module de cryptage
=========================================

pathfile : dreamtools/tools

.. important::
    Module utilisable uniquement sous Linux. Pas de prise en charge du module crypt par Windows

.. note::
    Une clé privé et un grain de sel doivent être défini dans le fichier "de parapetre d'application"

    * **PROJECT_DIR/cfg/.app.yml**

    * SECRET_KEY

    * SALT_EXT

    *Méthode* : sha-512`*

:Exemple:
    >>> from krypt import CKrypting
    >>> pwd = CKrypting.encrypt("Mon mon de passe en clair")
    >>> if CKrypting.compare(pwd, 'Mon mot de passe en claire'):
    >>>     print ('Saisie invalide')
    >>> else:
    >>>     print ('Bienvenue')


