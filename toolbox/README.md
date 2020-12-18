#Librairies de fonctions aide au développement

##Modules Assistants

###Module tools : Librairie de fonctions standard

* **Ensemble d'expression reguliere standard** 
  * lettres accentuées (RGX_ACCENTS)
  * adresse mail (RGX_EMAIL)
  * Mot de passe sécurisé de 8 a dix caractères avec au moins une majuscule/minucule/car.Spec (RGX_PWD)
  * Numéro de Téléphone (RGX_PHONE)
  * Punctuation autorisée (RGX_PUNC)
  * Url (RGX_URL)
    
* **Fonctions d'utilisation stadard** 
  * print_err : Ecriture sur le flux erreur de la console
  * string_me: Convertion d'une valeur en chaine
  * clean_space : Nettoyage des espaces "superflus"
  * clean_allspace : Nettoyage de tous les espaces 
  * clean_coma : Supprime les accents/caractères spéciaux du texte source en respectant la casse 
  * clean_master : Supprime les accents, caractères spéciaux et espace du texte source
  * inttohex : Conversion d'un entier en hexadécimal
  * addhex : Addition hexadécimal
  * plain_hex : Complète un chiffre hexadecimal en préfixant une valeur de zéro
  * plain_zero : Complete une valeur chaine de zéro

  * check_password(s) : Vérifie que la syntaxe d'une chaine répond au critère d'un mot de passe
  * comphex : Compare hexadécimales

  * pwd_maker : Passeword maker
  * code_maker : Génération d'une chaine aléatoire composé de lettre et de chiffres 
  * def aleatoire : Génération d'un nombre aléatoire entre

* Fonction sur fichier
  * get_dir_path : renvoie du repertoire de travail en cours 
  * path_build : Construiction d'un pathfile
  * get_extension : Retrourne l'extension d'un fichier
  * def file_exists : Search for a file
  * makedirs : Création d'un répertoire avec verification 
  * get_parent_dir : Renvoie du repertoire parent
  * get_my_path : retour du repertoire pour le fichier en cours 
  * def remove_file : Suppression d'un fichier si existant 
  * def clean_dir(directory, pattern='*'): Supprimes tous les fichier d'un repertoire
    
* **Fonctions sur objet** 
  * add_list : Ajout d'un item dans une liste avec gestion des doublons
  * def dictlist : Ajout d'un valeur dans une liste d'un dictionnaire
  * str_dic : Convertion d'une chaine en distionnaire
  * pop_dic : Suppression d'une liste d'items d'un 
  * paser_directory : parcours de repertoire
    

###Module dtemng
Librairie de fonction de gestion de date

###Module cfgmng
Module de chargmenent de fichier de configuration au format YAML

###Module logmng
Module de gestion de LOGS

###Module krypt
Module de cryptage

###Module networkmng.py
Module de gestion Network

###Module pymaging
de gestion de l'image

##Module de configuration

config.py