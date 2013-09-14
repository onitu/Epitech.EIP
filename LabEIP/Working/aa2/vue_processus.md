# Vue processus

Au lancement d'Onitu, la première étape est de lancer Circus. Circus va nous permettre de lancer et de monitorer des processus de façon simple et optimisé.
Circus se charge donc de lancer dans deux processus distinct, Redis tout d'abord qui nous permettra de stocker toute les méta-données des fichiers. Puis le Core d'Onitu qui se charge d'analyser le fichier "entries.json" contenant la liste des drivers (ainsi que leurs paramètres) à démarrer. Pour chaque entrée valide le Core demande à Circus de lancer le Driver correspondant. Une fois ceci fait le Core bouclera en attente d'action à effectuer.

Le driver est donc un processus à part, lancé et monitoré par Circus.
A son lancement il va d'initialiser avec les paramètres transmits, puis lancer le "Plug". Le Plug est l'élément communiquant du driver, il va donc se connecter à redis pour consulter et transmettre des informations. Il va donc écouter les requêtes que Redis lui transmet et les traiter si c'est a lui de le faire, en renvoyant une réponse si necessaire.

\FullHeightFigure{Vue processus}{figures/vue_processus_fig1.png}
\FullHeightRotatedFigure{Vue processus}{figures/vue_processus_fig2.png}
\FullHeightFigure{Vue processus}{figures/vue_processus_fig3.png}
\FullHeightFigure{Vue processus}{figures/vue_processus_fig4.png}
\FullHeightFigure{Vue processus}{figures/vue_processus_fig5.png}
