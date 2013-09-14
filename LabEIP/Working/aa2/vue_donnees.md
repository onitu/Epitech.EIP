# Vue données

Les principales données gérées par Onitu sont des fichiers. Afin de manipuler ces fichiers avec une grande précision et de manière performante, des méta-données sont stockées.

Ces méta-données sont stockées dans une base de données clé-valeur en mémoire, Redis. Les données sont préservées entre chaque lancement du serveur grâce à un 'dump' régulier de la base.\\

Chaque nom de fichier correspond à une clé dans Redis, à laquelle est associée un tableau associatif (hash) contenant les méta-données du fichier, sous la forme suivante :

\begin{lstlisting}[language=json,firstnumber=1]
{
    checksum: '6d96270004515a0486bb7f76196a72b40c55a47f',
    size: 1798585,
    type: 'file',
    content-type: 'image/png',
    created-at: 'Thu Jun 20 2013 20:31:34 GMT+0200',
    updated-at: 'Mon Jun 24 2013 18:27:04 GMT+0200',
}
\end{lstlisting}

Redis sert aussi à partager diverses informations, comme les options de configuration des drivers, ou les ports correspondants aux sockets ZeroMQ.
