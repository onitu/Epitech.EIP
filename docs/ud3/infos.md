\newpage

# Informations complémentaires

## Bogues connus

Onitu étant actuellement en développement, de nouveaux bogues apparaissent ou sont détectés régulièrement dans les versions de test du projet.

La liste des bogues peut être consultée dans la section *Issues* de la page *Github* du projet, à cette adresse: <https://github.com/onitu/onitu/issues>.

Le report des bogues rencontrés se fait sur cette même page, en créant une nouvelle *issue*.

### Problèmes de casse avec Dropbox

Dropbox utilise un système de fichiers **insensible à la casse**, c'est-à-dire que tous les noms de fichiers sont en minuscules pour Dropbox. Le service ne fait alors pas la différence entre, par exemple, des fichiers nommés **test.doc**, **Test.doc**, **test.DOC**...

Cela pose bien entendu un problème lors d'une utilisation de Dropbox à travers Onitu, les autres services connectés à Onitu ne partageant pas de telles spécifications. Cela constitue un problème connu : une asymétrie de synchronisation des fichiers entre Onitu et Dropbox, c'est-à-dire que là où Onitu voit plusieurs fichiers différents dont seule la casse du nom change, Dropbox n'en voit qu'un seul. Si vous apportez des modifications à un fichier **test.doc**, puis à un autre fichier **TEST.DOC**, et que vous les synchronisez avec Dropbox, vous perdrez les modifications effectuées sur **test.doc** sur Dropbox, car il les remplacera par les données du fichier **TEST.DOC**.

L'utilisateur est donc encouragé à utiliser des fichiers dont le nom diffère autrement que par la seule casse lorsqu'il connecte Onitu à son compte Dropbox, sous peine d'encourir une possible perte de données et des comportements inattendus et non-souhaités.


## Évolutions

L'administration d'*Onitu* n'est actuellement possible que par une édition manuelle du fichier de configuration. Nous travaillons activement à l'intégration d'une interface Web d'administration, depuis laquelle vous pourrez administrer vos fichiers, les services utilisés ainsi que les règles de transfert de vos fichiers (voir **[Interface Web]**).

Le nombre de *drivers* actuellement proposés est plutôt limité, mais augmentera progressivement par la suite, à mesure que nous agrégerons les protocoles de nouveaux services.

## Foire aux questions (FAQ)

* **Pourquoi choisir *Onitu* ?**  
  *Onitu* se démarque sur le marché par deux atouts majeurs: en choisissant *Onitu*, vous bénéficiez d'un contrôle total de vos données, tout en vous appuyant sur des services reconnus.
  Vous rendez également compatibles des services indépendants, tels que *Dropbox* et *Google Drive* par exemple.
* **Qui êtes-vous ?**  
  Nous sommes un groupe de 10 étudiants d'Epitech, et développons *Onitu* dans le cadre de notre projet de fin d'études (ou *EIP* pour *Epitech Innovative Project*).
* **Où télécharger *Onitu* ?**  
  Les sources du projet sont disponibles sur le *Github* officiel: <https://github.com/onitu/onitu>

* **Comment installer *Onitu* ?**
  Référez-vous au Chapitre 1 de ce document : **[Installation]**.
* **Sur quelles machines puis-je installer *Onitu* ?**  
  *Onitu* peut s'installer sur toute machine disposant de Python, versions *2.7* ou supérieures.
  Seuls certains drivers de gestion des fichiers locaux peuvent être spécifiques à certaines architectures.
* **Que faire en cas de dysfonctionnement ?**  
  Dans le cas où vous rencontreriez un bogue lié à l'installation ou l'utilisation d'*Onitu*, nous vous invitons à le reporter dans les *issues* du projet sur *Github*: <https://github.com/onitu/onitu/issues>
* **Comment puis-je contribuer au projet ?**  
  Un premier conseil si vous souhaitez contribuer au projet est d'en suivre l'évolution notamment en consultant les *issues*: <https://github.com/onitu/onitu/issues>  
  Nous vous conseillons ensuite de prendre contact avec l'équipe (cf **Comment puis-je vous contacter ?**).
  Enfin, nous vous invitons à consulter la documentation technique pour mettre cela en pratique: <http://onitu.readthedocs.org>
* **Comment puis-je vous contacter ?**  
  Vous pouvez nous contacter à l'aide de l'adresse *e-mail* `onitu_2015@labeip.epitech.eu`,
  ou venir nous retrouver sur *IRC*: canal `#onitu` sur *FreeNode* (`irc.freenode.net`).
* **Où trouver la documentation du projet ?**  
  La documentation technique est disponible en ligne à l'adresse suivante: <http://onitu.readthedocs.org>

## Liens utiles

Voici une série de liens vous permettant de vous tenir informé de l'état du projet et de son avancement.

* Site vitrine : <http://onitu.github.io>
* Twitter : <https://twitter.com/OnituProject>
* Canal *IRC* : `#onitu` sur le serveur *FreeNode* (`irc.freenode.net`)
* *Github* du projet : <https://github.com/onitu/onitu>
* Documentation technique en ligne : <http://onitu.readthedocs.org>
* Rapports d'exécution des tests : <https://travis-ci.org/onitu/onitu>
* Tests de performance : <http://onitu.khady.info>
