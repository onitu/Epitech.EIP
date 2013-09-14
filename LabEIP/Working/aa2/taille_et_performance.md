# Taille et performance

Onitu est une solution visant à être installée au plus près de l'utilisateur. Elle ne sera ainsi déployée que sur des réseaux de taille modeste, tels que des réseaux domestiques ou de petites entreprises. C'est pourquoi le nombre d'utilisateurs du système n'excédera jamais quelques dizaines d'utilisateur.

Conséquence de nombre restreint d'utilisateurs, celui des requêtes simultanés ne sera pas non plus très important. Nous estimons la charge à une centaine de requêtes par heure, ponctuées occasionnellement de quelques pics à deux ou trois fois plus. Ces chiffres restent largement raisonnables pour une machine moderne, et donc ne consituent pas un problème.
La taille des données ainsi échangées est par contre corrélée avec la taille des fichiers stockés, pouvant facilement s'élever à plusieurs méga ou giga-octets. Cependant, ces fichiers ne sont pas transmis en un seul bloc, mais découpés en différentes sections (*chunks*), de façon à ce que la taille des requêtes ne soit pas trop conséquente, et ne pèse ainsi pas trop lourd sur la charge réseau.

La taille des données stockées est bien plus variable d'une installation à l'autre. Seul invariant, la taille du programme et de ses fichiers de configuration, probablement quelques kilo-octets, négligeable face aux fichiers de l'utilisateur.

En effet, les fichiers concernés constituent tous ceux que l'utilisateur veut voir synchronisés avec d'autre service, et représentent donc une taille non quantifiable, limitée par les capacités et ressources en stockage de la machine hôte.

Pour un bon déroulement du processus, il est promordial que les requêtes s'effectuent rapidement et ne bloquent pas l'ensemble du système. De façon à ce que différentes actions, telles que la mise à jour des drivers ou la redistribution des fichiers entre services à charge et vitesse variables (fonctions de la plateforme d'accueil), puissent être effectuées simultanément, celles-ci devront se faire de manière asynchrone.
