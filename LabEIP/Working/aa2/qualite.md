# Qualité

Les contraintes purement fonctionnelles, évoquées tout au long de ce document ne représentent pas l'ensemble dex exigences auxquelles notre architecture devra répondre.

Premièrement, Onitu, afin d'être au plus proche des besoins de ses utilisateurs, devra permettre d'agréger un grand nombre de services externes de stockage. Ne pouvant prétendre à l'intégration des présentes solutions, et encore moins des futures, l'architecture permettra d'étendre facilement ses fonctionnalités en y greffant des modules complémentaires.

La fiabilité du système est sans aucun doute le point le plus important de la solution. S'occupant de la synchronisation, et donc de la sauvegarde des fichiers utilisateurs, il n'est en effet pas tolérable que de telles données se perdent ou soient corrompues. Ce point est comblé par une conception modulaire et un isolement des drivers: si l'un d'entre-eux rencontre un problème, le reste de l'application ne sera pas affecté. Des outils de contrôle de somme des données seront aussi implémentés afin de s'assurer à tout moment de la fiabilité de celles-ci.

La sécurité des échanges, bien que cruciale, ne relève pas de notre architecture, car étant relative au protocole de chacun des services externes. Nous ne pourrons à ce sujet n'agir qu'en tant que conseillers, en aidant l'utilisateur au niveau d'une configuration qui correspond à ses besoins de confidentialité, d'intégrité, etc. En lui présentant de manière concise les différents choix qui s'offrent à lui, et l'orientant vers ceux qui répondent le mieux à ses attentes, tels que des services à protocoles chiffrés pour l'échange des données.

La confidentialité des données devra aussi être assurée, par des méthodes d'authentification. Nous nous appuyerons à cet effet sur des protocoles reconnus, tels OAuth.

Enfin, l'application étant développée en python, elle sera facilement déployable et interopérable. Présent sur les principaux systèmes d'exploitation du marché, toute personne devrait être en mesure de faire tourner notre solution. Nous veillons aussi, dans nos choix techniques sur les bibliothèques utilisées, à ce que celles-ci soient de même portables et faciles à mettre en place.
