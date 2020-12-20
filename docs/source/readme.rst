Dreamtools
===========

Dreamtools est un outils d'aide au développement contenant une liste de fonction d'utilisation basique

Installation
------------
.. code-block:: BASH

    $ pip install deamtools
    $ tools-install

Le répertoire de configuration 'cfg' sera créé à la racine du projet.

.. warning::
    Initiliser les données de l'application

Configuration
--------------
.. code-block:: PYTHON3

    import toolbox

    app_name = "AMON_APP"   #nom de votre application
    toolbox.config(app_name, mode='DEBUG')  # par défaut mode ='PROD'

.. warning::
    Le paquet comprend un module de cryptage non supporté par Winddows


Crédits
-------
Conçut par Dreamgeerker