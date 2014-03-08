# Taille et performance

Dans un premier temps, Onitu ne vise pas à être déployé sur de très grosses structures, mais plutôt sur des réseaux domestiques ou au sein de petites et moyennes entreprises. Plus tard, si la capacité à monter en charge est satisfaisante et que la demande est présente, de plus gros réseaux seront envisagés.\

\

Onitu doit pouvoir être utilisé au sein d'un réseau amateur, et donc avec peu de moyens. Un matériel tel que le Raspberry Pi doit par exemple être suffisant pour faire fonctionner le serveur, avec une dizaine de *drivers*, quelques milliers de fichiers et plusieurs centaines de requêtes par heure.
Même si nous ne cherchons pour le moment pas à nous adapter à de très grosses structures, nous devons à tous prix éviter d'augmenter de manière exponentielle selon un facteur.\

\

Pour le moment, les deux goulots d'étranglement sont la synchronisation d'un fichier, et le traitement des règles par le *Referee*. Pour le premier, plusieurs algorithmes devront être essayés, mais la qualité du réseau reste l'élément discriminant, sur lequel nous n'avons aucun contrôle. Pour le traitement des règles par le *Referee*, d'autres instances de ce dernier pourront être lancées en cas de ralentissement, permettant une concurrence et un parallélisme.\

\

L'optimisation de l'utilisation du réseau est au cœur de l'architecture d'Onitu, et des adaptations en profondeur devront être effectuées si nous ne répondons pas à des critères satisfaisants.
De part la nature très hétéroclite des différentes solutions avec lesquelles nous communiquons (fichiers locaux, *Dropbox*, serveur SSH…), il est très dur de s'adapter à toutes les vitesses. En effet, un échange entre deux fichiers locaux de plusieurs giga-octets pourra prendre quelques millisecondes sur un *SSD*, alors que le téléchargement d'un fichier de quelques octets pourra prendre plusieurs heures sur *Amazon Glacier*. Parfois, le temps de réponse est le facteur discriminant, parfois c'est la taille de la requête.
Nous travaillons encore à améliorer l'algorithme d'échange de fichiers afin de mieux nous adapter. Nous pensons notament utiliser un système de crédits, ainsi que des tailles de découpage variables, qui seront contrôlés par les *drivers* eux-même.\

\

Onitu utilise la base de données *Redis* afin de stocker les métadonnées. Cette base de données monte extrêmement bien en charge et peut supporter facilement des milliers de requêtes par seconde sur de petits systèmes. Mais pour cela, elle conserve toutes les données dans la mémoire vive. Une attention particulière doit donc être apportée quant à la constitution de ces métadonnées, afin de ne pas utiliser trop de mémoire. Pour le moment, nous essayons de nous en tenir à moins de 100 méga-octets utilisés pour stocker un million de fichiers, soit 100 octets par fichier. Bien entendu, cela reste une moyenne et dépend notamment de la longueur du nom du fichier.
