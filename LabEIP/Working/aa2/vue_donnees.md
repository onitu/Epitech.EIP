# Vue données

Les principales données gérées par Onitu sont des fichiers. Afin de manipuler ces fichiers avec une grande précision et de manière performante, des méta-données sont stockées.

Ces méta-données sont stockées dans une base de données clé-valeur en mémoire, Redis. Les données sont préservées entre chaque lancement du serveur grâce à un 'dump' régulier de la base.

Chaque nom de fichier correspond à une clé dans Redis, à laquelle est associée un tableau associatif (hash) contenant les méta-données du fichier, sous la forme suivante :

\begin{lstlisting}[language=json,firstnumber=1]
{
    checksum: '6d96270004515a0486bb7f76196a72b40c55a47f',
    size: 1798585,
    type: 'file',
    content-type: 'image/png',
    created-at: 'Thu Jun 20 2013 20:31:34 GMT+0200',
    updated-at: 'Mon Jun 24 2013 18:27:04 GMT+0200',
    routes : "2a 81 b6",
}
\end{lstlisting}

Lorsqu'ils détectent un changement dans un fichier, les drivers doivent publier le changement sur les routes correspondantes. Les drivers écoutant ces routes seront alors informés du changement. Le Referee décide quelles sont les routes, qui les écoutes et de quels fichiers elles sont constituées. Il faut donc savoir facilement à quelles routes appartient un fichier, mais aussi quels sont les fichiers appartenant à une route. Redis ne gérant pas les relations, comme une base de donnée SQL, le schéma doit simuler une relation plusieurs-à-plusieurs.
Pour cela, la liste des routes d'un fichier sont inscrites dans ses méta-données, et un 'set' Redis est utilisé pour stocker l'ensemble des fichiers d'une route.

Ce model implique que la taille de la base de données augmente avec le nombre de fichiers, le nombre de routes, et la taille du nom des fichiers. Or, le fait que Redis soit en mémoire limite la taille de la base. D'autres solutions seront donc envisagées si la capacité à monter en charge n'est pas suffisante. Il est notament envisagé de ne pas identifier les fichiers par leur chemin absolu, mais simplement par entier représentant un identifiant unique.

\FullWidthFigure{Vue données}{figures/vue_donnees_fig1.png}
