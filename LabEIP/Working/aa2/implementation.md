# Implémentation


## Vue globale

Par nature onitu doit gerer beaucoup d'operations en paralelle, pour cela il existe plusieurs solutions clasique. Principalement utiliser un systeme evenementiel, utiliser plusieurs threads ou utiliser plusieurs process.

Le systeme evenementiel nous parais plus compliquer a mettre en place car il laisse moins de liberetes au differentes parties qui devront obligatoirement respecter une api commune relativement stricte. Elle est aussi moins tolerante avec des composants qui bloquent alors qu' ils ne devraient pas et peu entrainer rapidement une perte de performance ou un arret du systeme dans son ensemble. Dans onitu nous voulons a terme une possibilitee poru des developpeur externe d' ajouter des drivers, donc un systeme centralaiser ou tout doit obligatoirement fonctionner parfaitement en suivant les regles nous semble peu adapter.

Il nous reste donc le choix entre l'utilisation de threads ou de different process, pour l'instant nous avons choisis d'utiliser des threads car l'avantage principal d' avoir plusieurs process est de pouvoir etendre facilement le systeme sur plusieurs machines. Cela ne nous interesse que moyenement a ce niveau car nous pouront deja le faire en aillant sinmplement plusieurs instances d' onitu. L' autre avantage d'avoir plsuieeurs process est de contourner la Global-Interpreter-Lock (GIL) de python qui n' authorise en fait qu' une seule operation en paralelle meme dans le cadre du multithread. Cependant bnous estimons que notre application sera IO-bound, c' est a dire qu' elle esera principalement limitee par les operation d' entree sortie sur le disque et sur le reseaux qui sont toutes les deux implementee a  un niveau plus bas que python ce qui ne causera pas de blockage sur la GIL.

\FullWidthFigure{Vue globale}{figures/implementation_vue_globale_fig1.png}
\clearpage

La programation paralelle, multi-thread dans notre cas, apporte souvent des problemes. La plus part du temps il s' agit d' erreurs de gestion des ressources qui sont partagees entre differentes unitees d' execution. Ces ressources partager ce retrouvent utilisee par plusieurs unitees en meme temps ce qui cause des conflict et entraine souvent une corupton des donnees. Il est trres compliquer de reussir a avoir une architecture qui elimine ces problemes. C' est pourquoi nous avons decider de limiter au maximum les donnees partagees entre diferent thread. (Ce qui devrais aussi facilitee un changement eventuel en faveur du multi-process)

Pour limiter les donnes comune nous utilisont une archtecture de type messaging. Il n'y as aps de ressources comune entre les differentes unitees d' execution. Les diferentes parties du programent vont neamoins comuniquer au travers de messages en utilisant la librairie 0mq. Un thread va etre notififiee des evenements propre a son backend par une implementation de son choix qui depend grandement de la nature du backend. (hooks sur le filesystem, thread-jumaux qui surveuille une API de backend en ligne, etc) Quand il a des evenements il va notifier les autres parties du programe qui en ont besoin en envoyant des message. DE la mememe facon il va recevoir des message qui seront pour lui des ordres et proviendront principalement du referee.

Cette architecture particuliere fait que nos diagrame de classe et les relations entre les diferents elements d' onitu sont tres imple et il y' as peut de relations d' agregation car les differents elements sont au meme niveau et comuniquent avec des messages au lieu de se modifier directement.


## Couches applicatives

Onitu etant un serveur relativement generique gerant des drivers pour les differents backends, son architecture centrale est relativement simple. D'autant plus que l' architecture est base sur du messaging ce qui diminue grandement le besoin de nombreuse methodes et attributs.

\FullHeightRotatedFigure{Couches applicatives}{figures/implementation_couches_applicatives_fig1.png}
\FullHeightRotatedFigure{Couches applicatives}{figures/implementation_couches_applicatives_fig2.png}
