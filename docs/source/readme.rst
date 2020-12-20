Dreamtools
===========

Dreamtools est un outils d'aide au développement contenant une liste de fonction d'utilisation basique

Installation
------------
.. code-block:: BASH

    $ pip install dreamtools
    $ tools-installer
    **************************************************************************
    ** Création architecture
    ** -----------------------------------------------------------------------
    **  Répertoire logs
    **      >> Répertoire créé :  C:\Users\Ohanna\Geekspace\testpack\logs
    **  Répertoire configuration
    **      >> Répertoire créé :  C:\Users\Ohanna\Geekspace\testpack\cfg
    **=======================================================================-


Le répertoire de configuration 'cfg' sera créé à la racine du projet.

.. warning::
    Initiliser les données de l'application

Configuration
--------------
.. code-block:: PYTHON3

    import dreamtools

    app_name = "AMON_APP"   #nom de votre application
    dreamtools.config(app_name, mode='DEBUG')  # par défaut mode ='PROD'

.. warning::
    Le paquet comprend un module de cryptage non supporté par Winddows


Crédits
-------
Conçut par Dreamgeerker