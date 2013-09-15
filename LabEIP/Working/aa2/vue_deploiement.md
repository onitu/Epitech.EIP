# Vue déploiement

Onitu est principalement destiné à être utilisé par des particuliers, dans un cadre privé. Le parc de machines sur lequel il sera amené à être installé est donc particulièrement hétéroclite: machines diverses, de gammes différentes (de l'entrée de gamme au serveur professionnel), possédant chacune un environnement et une configuration leur étant propre. Pour éviter que cela ne constitue un frein au déploiement de notre solution, l'installation de l'outil devra donc être des plus aisées.\

\

Le déploiement de la solution, une fois les sources récupérées depuis un dépôt *Git* par exemple, se fera à l'aide d'une procédure d'installation détaillée, voire d'un script.
Celle-ci commencera bien sûr par la mise en place de l'interpréteur *CPython*, sur lequel s'appuient le code et les bibliothèques du projet.

Par la suite, à l'aide du gestionnaire de modules python *PIP*, les dépendances à Onitu seront installées sur la machine hôte, telles que *Circus*, *ZeroMQ* ou encore *Redis*.
La solution est alors prête à l'emploi. Seule persiste pour l'administrateur la configuration de celle-ci, passant notamment par la mise en place de l'arborescence de fichiers.\

\

Les contraintes géographiques du système seront dépendantes des hôtes sur lequel il sera installé: ceux-ci régiront en effet les performances et la bande passante. En fonction de l'activité des utilisateurs du système (fréquence des requêtes) et de la taille des fichiers stockés, la consommation en bande passante pourra s'avérer importante. Il sera donc de la responsabilité de l'administrateur de veiller à ce que cette utilisation ne soit pas excessive suivant les caractéristiques de son installation.

À terme, l'architecture permettra aux différents composants du serveur de fonctionner de façon décorrélée sur différentes machines, néanmoins reliées entre-elles. Ce traffic supplémentaire sera semblable à celui nécessaire pour la communication avec les organes distants, tels que *DropBox*, et ne constituera donc pas une charge supplémentaire.

\FullHeightRotatedFigure{Vue déploiement}{figures/vue_deploiement_fig1.png}
