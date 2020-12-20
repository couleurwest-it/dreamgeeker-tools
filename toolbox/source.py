source = {'.app.yml': "{'SALT': 'ungraindesel', 'SECRET_KEY': 'Unepetitecledeseurite', 'TIMEZONE_FR': 'Europe/paris', 'TIMEZONE_GF': 'America/Cayenne'}", '.log.yml': "{'formatters': {'complet': {'datefmt': '%Y%m%d%H%M%S', 'format': '%(asctime)s.%(msecs)d|[%(levelname)s %(code)s]|[%(title)s] %(message)s'}, 'default': {'datefmt': '%Y%m%d%H%M%S', 'format': '%(asctime)s|%(levelname)s|[%(name)s.%(module)s] %(message)s'}, 'server': {'datefmt': '%Y%m%d%H%M%S', 'format': '%(asctime)s|%(levelname)s| %(status)d - %(request)s'}}, 'handlers': {'console': {'class': 'logging.StreamHandler', 'formatter': 'default', 'level': 'DEBUG', 'stream': 'ext://sys.stdout'}, 'default': {'class': 'logging.StreamHandler', 'formatter': 'default', 'level': 'DEBUG', 'stream': 'ext://sys.stdout'}, 'file': {'backupCount': 30, 'class': 'logging.handlers.TimedRotatingFileHandler', 'encoding': 'utf8', 'filename': 'logs/traces.log', 'formatter': 'complet', 'interval': 1, 'level': 'INFO', 'when': 'midnight'}}, 'loggers': {'PROD': {'handlers': ['console', 'file'], 'level': 'INFO', 'propagate': False}, 'TEST': {'handlers': ['console'], 'level': 'DEBUG', 'propagate': False}}, 'root': {'handlers': ['console'], 'level': 'NOTSET', 'propogate': True}, 'version': 1}", 'categorie.yml': "{'categories': {'key': 'value'}}", 'mailing.yml': '{\'footer\': {\'html\': \'<footer>\\n <table>\\n  <tbody style="font-size: 11px;">\\n  <tr>\\n  <td rowspan="6"><img src="http://couleurwest-it.com/logo" alt="CW Logo" /></td>\\n  <td style="font-size: 20px; font-weight: bold; color: #dc0000; font-variant: small-caps;">Couleur West IT</td>\\n  </tr>\\n  <tr>\\n  <td style="font-size: 12px; font-variant: small-caps;">Conception &amp; R&eacute;alisation de solutions num&eacute;riques adapt&eacute;es<br />Accompagment au Changement</td>\\n  </tr>\\n  <tr>\\n  <td style="font-size: 11px; text-align: center;" colspan="2"><span style="font-weight: bold; font-variant: small-caps;">mail :</span> <a href="mailto:contact@couleurwest-it.com">contact@couleurwest-it.com</a> | <span style="font-size: 11px; font-weight: bold; font-variant: small-caps;"> Telegram :</span> <a href="https://t.me/dreamgeeker">dreamgeeker</a></td>\\n  </tr>\\n  <tr>\\n  <td style="text-decoration: none; font-size: 11px; width: 526px; text-align: center;" colspan="2"><em><strong>Telephone</strong> :</em>&nbsp;+594 (0) 694 949 842</td>\\n  </tr>\\n  </tbody>\\n  </table>\\n  <p><cite style="float: right; text-align: right; font-size: 10px;"> Le monde est vieux, mais l\\\'avenir sort du pass&eacute;.<br /> (Djibril Tamsir Niane)</cite></p>\\n  <p>&nbsp;</p>\\n  <article>\\n  <p>Cet email vous est envoy&eacute; de mani&egrave;re automatique, ne pas y r&eacute;pondre car votre demande ne sera pas trait&eacute;e.</p>\\n  <em>Pour votre s&eacute;curit&eacute; :</em>\\n  <ul>\\n  <li><em>Nous ne vous demanderons jamais par mail aucunes informations d\\\'ordre priv&eacute;es</em></li>\\n  <li><em>Nous ne partageons ni ne diffusons aucune de vos donn&eacute;es</em></li>\\n  <li><em>Votre adresse mail n\\\'est utilis&eacute;e que pour vous identifier et &eacute;changer avec vous.</em></li>\\n  <li><em>Nous n\\\'envoyons aucunes publicit&eacute;</em></li>\\n  </ul>\\n  <em>N\\\'h&eacute;sitez pas &agrave; supprimer tous mail vous paraissant suspicieux.</em><em>Bon &agrave; savoir : Selon L&rsquo;ADEME un mail d\\\'1 Mo envoy&eacute; correspont &agrave; environ &agrave; 15 grammes de CO2 ! Ainsi, l\\\'envoie de 30 mails par jour &agrave; diff&eacute;rents destinataires pendant un an correspond &agrave; presque 330 kg de CO2, soit plusieurs milliers de km d&rsquo;essence utilis&eacute;s en voiture. Le stockage des mails et des pi&egrave;ces jointes sur un serveur est aussi un enjeu important : plus le courriel est conserv&eacute; longtemps, plus son impact sur le changement climatique sera fort. </em><br /><em> R&eacute;duisez l\\\'impact environnemental :</em>\\n  <ul>\\n  <li><em>classez vos mails d&egrave;s leur arriv&eacute;e, nettoyez r&eacute;guli&egrave;rement vos spams et tous vos mails obsol&egrave;tes</em></li>\\n  <li><em>archivez (de pr&eacute;f&eacute;rence de mani&egrave;re locale) vos mail "important"</em></li>\\n  <li><em>stockez vos documents administratifs dans des espaces cloud telque Digipost et partagez vos documents par lien.</em></li>\\n  <li><em>supprimez les pi&egrave;ces jointes des messages auxquels vous r&eacute;pondez, ciblez et ne multipliez pas les destinataires lors de vos envois de mails.</em></li>\\n  <li><em>d&eacute;sabonnez vous des newsletter inutiles</em></li>\\n  </ul>\\n  <em>Vous souhaitez savoir plus ? Quoi faire ? Comment faire ? =&gt; <a href="contact@couleurwest-it.com">contact@couleurwest-it.com</a></em></article>\\n</footer>\\n\', \'txt\': \'Cordialement --- Le monde est vieux, mais l\\\'avenir sort du passÃ©.  (Djibril Tamsir Niane)\\n\\n    -----\\n ---    .   Couleur\\n--       .       . West IT --        .  .  .   https://couleurwest-it.com\\n ---       .   .\\n    -----+\\n    ------------------------------------------\\nConception et rÃ©alisation de solutions numÃ©riques Accompagnement au chamgement\\ncontacts : contact@couleurwest-it.com | https://t.me/dreamgeeker\\n\\n ----\\n Cet email vous est envoyÃ© de maniÃ¨re automatique. Merci de ne pas y rÃ©pondre.\\n En cas de rÃ©clamation envoyer un mail Ã\\xa0 reclamation@lescouleursdelouest.fr\\n\\n Pour votre sÃ©curitÃ© :\\n   - Nous ne vous demanderons jamais aucunes informations d\\\'ordre privÃ©e par mail\\n   - Nous ne partageons ni ne diffusons aucune de vos donnÃ©es\\n   - Votre adresse mail n\\\'est utilisÃ©e que pour vous identifier et Ã©changer avec vous\\n   - Nous n\\\'envoyons aucune publicitÃ©\\n\\n N\\\'hÃ©sitez pas Ã\\xa0 supprimer tous mail vous paraissant suspicieux\\n\\n Bon Ã\\xa0 savoir : Selon Lâ€™ADEME un mail d\\\'1 Mo envoyÃ© correspont Ã\\xa0 environ Ã\\xa0 15 grammes de CO2 ! Ainsi, l\\\'envoie de 30 mails par jour Ã\\xa0 diffÃ©rents destinataires pendant un an correspond Ã\\xa0 presque 330 kg de CO2, soit plusieurs milliers de km dâ€™essence utilisÃ©s en voiture.\\n Le stockage des mails et des piÃ¨ces jointes sur un serveur est aussi un enjeu important : plus le courriel est conservÃ© longtemps, plus son impact sur le changement climatique sera fort.\\n RÃ©diusez l\\\'impact environnemental :\\n   - classez vos mails dÃ¨s leur arrivÃ©e et nettoyez vos spams et vos mails obsolÃ¨tes\\n   - archivez (de prÃ©fÃ©rence de maniÃ¨re locale) vos mails "importants"\\n   - stockez vos documents administratifs dans des espaces cloud telque Digipost et partagez vos documents par lien.\\n   - supprimez les piÃ¨ces jointes des messages auxquels vous rÃ©pondez, ciblez et ne multipliez pas les destinataires lors de vos envois de mails.\\n   - dÃ©sabonnez-vous des newsletters inutiles (vous trouverez les lien en bas de mail)\\n Vous souhaitez des informations ou des conseil sur le numÃ©rique : contact@couleurwest-it.com\\n\'}, \'ref_message\': {\'html\': \'<h4>Bienvenu {nom} {prenom}</h4><br />\\n<p>Exemple du mÃªme message au format html</p>\\n\', \'object\': \'Exemple gestion mail\', \'txt\': "Bienvenu {nom} {prenom} Example d\'un message au format texte\\n"}}', 'normalizor.yml': '{\'email\': {\'rename\': \'adresse mail\'}, \'link\': {\'rename\': \'url\'}, \'paf\': {\'rename\': "prix d\'entrÃ©e"}, \'password\': {\'rename\': \'mot de passe\'}, \'pseudo\': {\'rename\': \'pseudo\'}, \'title\': {\'rename\': \'titre\'}}', 'regex.yml': "{'accents': 'Ã\\xa0Ã¢Ã¤Ã£Ã©Ã¨ÃªÃ«Ã®Ã¯Ã¬Ã´Ã¶Ã²ÃµÃ¹Ã¼Ã»Ã¿Ã±Ã§', 'email': '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\\\.[a-zA-Z0-9-.]+$', 'password': '/.*(?=.{8,12})(?=.*[Ã\\xa0Ã¢Ã¤Ã£Ã©Ã¨ÃªÃ«Ã®Ã¯Ã¬Ã´Ã¶Ã²ÃµÃ¹Ã¼Ã»Ã¿Ã±Ã§a-z])(?=.*[A-Z])(?=.*\\\\d)(?=.*[!#$%&?]).*/', 'phone': '^0[1-9]\\\\d{8}$', 'punctuation': '@#!?$&-_', 'url': 'https?:\\\\/\\\\/(www\\\\.)?[-a-zA-Z0-9@:%._\\\\+~#=]{1,256}\\\\.[a-zA-Z0-9()]{1,6}\\\\b([-a-zA-Z0-9()@:%_\\\\+.~#?&//=]*)'}", 'validators.yml': "{'check_mail': {'required': False, 'schema': 'email scheme'}, 'form_example': {'categorie': {'coerce': 'clean_string', 'required': True, 'type': 'string'}, 'commune': {'coerce': 'clean_string', 'required': True, 'type': 'string'}, 'email': {'check_with': 'email'}, 'info': {'coerce': 'clean_string', 'required': True, 'type': 'string'}, 'link': {'check_with': 'url', 'required': False}, 'phone': {'required': False, 'schema': 'gf phone'}, 'title': {'coerce': 'clean_string', 'required': True, 'type': 'string'}}, 'link': {'check_with': 'url', 'required': False}, 'media_link': {'check_with': 'medialink', 'coerce': 'medialink', 'required': False}, 'txt_optional': {'coerce': 'clean_string', 'required': False, 'type': 'string'}, 'txt_required': {'coerce': 'clean_string', 'required': True, 'type': 'string'}, 'valid_mail': {'check_with': 'email', 'required': True}, 'valid_pwd': {'schema': 'sch_password'}}"}