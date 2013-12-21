# Risques, dépendances, prérequis et contraintes

*Onitu* peut être vu une solution de synchronisation de fichiers entre divers services, et est ainsi sujet à de nombreux disfonctionnements possibles: services ou périphériques inacessibles, lenteurs voire coupures réseaux. Le projet se base de plus sur une architecture permettant l'intégration de *drivers* tiers par tout un chacun, un autre risque est donc un crash de l'un de ces *drivers*.

Ces situations provoqueraient potentiellement une altération des copies en cours, et par conséquent des fichiers stockés sur telle ou telle plateforme. Outre le fait de pouvoir relancer simplement le système en cas de problème, *Onitu* doit fournir des solutions de persistance des données et de reprises sur accident. Un fichier endommagé se doit d'être détecté au plus vite, étiqueté comme tel puis remonté au système hôte, de façon à être réparé au plus vite (correction de la partie corrompue si elle n'est pas trop importante, ou supression et remplacement du fichier).

Ces situations sont toutefois indépendantes de notre volonté, et pour pouvoir s'assurer que notre projet est capable de les gérer, il nous faudra les simuler.

De plus, chaque *driver* est spécifique à un service, et possède donc son lot de risques liés à l'utilisation de ce service. Cependant, un test qui échouerait simplement parce qu'une ressource externe n'est pas accessible ne devrait pas mettre en défaut l'ensemble du système. Dans la mesure du possible, une telle situation ne devrait pas mener à l'échec du test maisjuste indiquer que la ressource n'est pas joignable, et que le test est en conséquence ignoré.
