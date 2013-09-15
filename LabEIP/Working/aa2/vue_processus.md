# Vue processus

Au lancement d'Onitu, la première étape est le démarrage de *Circus*. *Circus* va nous permettre de lancer et de monitorer des processus de façon simple et optimisée.
*Circus* se charge donc de démarrer, dans deux processus distincts, *Redis* tout d'abord qui nous permettra de stocker toute les métadonnées des fichiers. Puis le *Core* d'Onitu, qui se charge d'analyser le fichier «entries.json» contenant la liste des *drivers* (ainsi que leurs paramètres de configuration) à démarrer. Pour chaque entrée valide, le *Core* demande à *Circus* de lancer le *driver* correspondant. Une fois ceci fait, le *Core* bouclera en attente d'actions à effectuer.\

\

Le *driver* constitue donc un processus à part, lancé et monitoré par *Circus*.
À son lancement, il s'initialise avec les paramètres transmis, puis démarre son *Plug*. Le *Plug* est l'organe communiquant du *driver*, il va donc se connecter à *Redis* pour consulter et transmettre des informations. Il écoutera aussi les requêtes que *Redis* lui transmet et les traitera s'il s'agit de celles qu'il gère, en renvoyant une réponse si necessaire.

\FullHeightFigure{Vue processus}{figures/vue_processus_fig1.png}
\FullHeightRotatedFigure{Vue processus}{figures/vue_processus_fig2.png}
\FullHeightFigure{Vue processus}{figures/vue_processus_fig3.png}
\FullHeightFigure{Vue processus}{figures/vue_processus_fig4.png}
\FullHeightFigure{Vue processus}{figures/vue_processus_fig5.png}
