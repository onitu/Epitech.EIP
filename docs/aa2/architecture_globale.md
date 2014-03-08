# Représentation de l'architecture globale

Onitu doit répondre à des contraintes de latences très fortes. De nombreux événements peuvent survenir en très peu de temps, mais avec des temps de traitement extrêmement variés (de quelques millisecondes à plusieurs heures). Afin de répondre à cette contrainte, l'architecture globale se doit d'être décentralisée, et de pouvoir monter en charge facilement.\

\

Les différents éléments sont donc isolés dans des processus systèmes, qui sont lancés et surveillés par le logiciel *Circus*. Les processus partagent les informations dont ils ont besoin via la base de données en mémoire *Redis*, et échangent des données via des sockets *ZeroMQ*.\

\

Le schéma suivant présente les différents éléments constituant Onitu, avec pour exemple deux *drivers*, un premier pour Ubuntu One et un second pour Dropbox.
Les flèches pointillées représentent la parenté (quel processus lance quel processus), et les flèches avec des tirets représentent la communication via *ZeroMQ*.

\FullWidthFigure{Architecture globale}{figures/architecture_globale_fig1.png}
