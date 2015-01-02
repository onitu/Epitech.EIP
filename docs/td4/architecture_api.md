## *API REST*

L'[*API REST*](https://fr.wikipedia.org/wiki/Representational_State_Transfer) d'Onitu permet à des logiciels externes d'intéragir avec Onitu. Cela offre la possibilité de développer une interface web pour visualiser les photos, surveiller le bon fonctionnement d'Onitu et être averti d'une défaillance ou encore intégrer Onitu à un autre logiciel.

L'*API* expose des routes *HTTP* pour contrôler plusieurs parties d'Onitu : les
fichiers, les *drivers* et les règles de configuration.

Dans les exemples qui suivront, toutes les routes sont à préfixer de `/api/v1.0`, ce préfixe étant omis pour des raisons de lisibilité.

### Les fichiers

Plusieurs routes sont exposées pour manipuler les fichiers gérés par Onitu. Ce
sont les routes qui commencent par `/files`.

Pour le moment, ces routes permettent uniquement de la consultation et non
d'envoyer des fichiers sur Onitu. C'est pour cela qu'elles n'acceptent que des
requêtes *HTTP GET*.

Les routes actuellement en place lisent les fichiers stockés sur Onitu. Elles
permettent de consuler les métadonnées de ces fichiers, pour en déterminer le
propriétaire, la taille ou les *drivers* qui en possèdent une version à jour.

#### GET `/files`

Liste les fichiers actuellement gérés par Onitu.

\begin{figure}[h]
\begin{lstlisting}[language=json,firstnumber=1]
GET /api/v1.0/files HTTP/1.1
Host: 127.0.0.1
Accept: application/json
\end{lstlisting}
\caption{Exemple de requête}
\end{figure}

\begin{figure}[h]
\begin{lstlisting}[language=json,firstnumber=1]
HTTP/1.1 200 OK
Vary: Accept
Content-Type: application/json

{
    "files": [
        {
            "mimetype": "text/plain", 
            "filename": "file.txt", 
            "uptodate": [
                "B", 
                "A"
            ], 
            "folder_name": "test", 
            "fid": "4d079fe9-e65e-5330-9734-6fbd327adc95", 
            "size": 5
        }, 
        {
            "mimetype": "image/jpeg", 
            "filename": "picture.jpg", 
            "uptodate": [
                "A", 
                "B"
            ], 
            "folder_name": "test", 
            "fid": "51dfe21c-7962-5b34-a983-98636c9b0249", 
            "size": 130499
        }
    ]
}
\end{lstlisting}
\caption{Exemple de réponse}
\end{figure}

\clearpage

#### GET `/files/id/(folder: string)/(name: string)`

Récupère l'identifiant (`fid`) du fichier de nom `name` dans `folder`.

\begin{figure}[h]
\begin{lstlisting}[language=json,firstnumber=1]
GET /api/v1.0/files/id/A/picture.jpg HTTP/1.1
Host: 127.0.0.1
Accept: application/json
\end{lstlisting}
\caption{Exemple de requête}
\end{figure}

\begin{figure}[h]
\begin{lstlisting}[language=json,firstnumber=1]
HTTP/1.1 200 OK
Vary: Accept
Content-Type: application/json

{
    "picture.jpg": "51dfe21c-7962-5b34-a983-98636c9b0249"
}
\end{lstlisting}
\caption{Exemple de réponse}
\end{figure}

\clearpage

#### GET `/files/(fid: string)/metadata`

Récupère les métadonnées du fichier d'identifiant `fid` (nom de fichier, type *MIME*, taille, etc.).

\begin{figure}[h]
\begin{lstlisting}[language=json,firstnumber=1]
GET /api/v1.0/files/51dfe21c-7962-5b34-a983-98636c9b0249/metadata HTTP/1.1
Host: 127.0.0.1
Accept: application/json
\end{lstlisting}
\caption{Exemple de requête}
\end{figure}

\begin{figure}[h]
\begin{lstlisting}[language=json,firstnumber=1]
HTTP/1.1 200 OK
Vary: Accept
Content-Type: application/json

{
    "mimetype": "image/jpeg", 
    "filename": "picture.jpg", 
    "uptodate": [
        "A", 
        "B"
    ], 
    "folder_name": "test", 
    "fid": "51dfe21c-7962-5b34-a983-98636c9b0249", 
    "size": 130499
}
\end{lstlisting}
\caption{Exemple de réponse}
\end{figure}

\clearpage

### Les services

Une partie importante de l'API est la manipulation des *drivers* et services. Il est possible de démarrer et stopper un service, de voir son statut et d'obtenir des statistiques à son sujet.

L'arrêt et le démarrage des services est notamment utile si vous souhaitez en mettre en pause, pour par exemple faire une sauvegarde de ses données sans risquer d'avoir des modifications pendant cette sauvegarde.

Le statut consiste à déterminer l'état de fonctionnement du service, s'il est en route, à l'arrêt ou en train de changer d'état.

Les statistiques permettent de surveiller qu'un service n'a pas de problème, ne consomme pas trop de CPU ou de RAM. Mais aussi de savoir depuis combien de temps il est en route.

Selon les services, il est aussi possible d'avoir des statistiques supplémentaires comme l'espace disponible, le nombre de requêtes effectuées, etc.

#### GET `/services`

Liste l'ensemble des services de l'instance courante d'Onitu.

\begin{figure}[h]
\begin{lstlisting}[language=json,firstnumber=1]
GET /api/v1.0/services HTTP/1.1
Host: 127.0.0.1
Accept: application/json
\end{lstlisting}
\caption{Exemple de requête}
\end{figure}

\begin{figure}[h]
\begin{lstlisting}[language=json,firstnumber=1]
HTTP/1.1 200 OK
Vary: Accept
Content-Type: application/json

{
    "services": [
        {
            "driver": "local_storage", 
            "name": "A", 
            "options": null
        }, 
        {
            "driver": "local_storage", 
            "name": "B", 
            "options": null
        }
    ]
}
\end{lstlisting}
\caption{Exemple de réponse}
\end{figure}

\clearpage

#### GET `/services/(name: string)`

Récupère les métadonnées du service `name` (nom, *driver*, options).

\begin{figure}[h]
\begin{lstlisting}[language=json,firstnumber=1]
GET /api/v1.0/services/A HTTP/1.1
Host: 127.0.0.1
Accept: application/json
\end{lstlisting}
\caption{Exemple de requête}
\end{figure}

\begin{figure}[h]
\begin{lstlisting}[language=json,firstnumber=1]
HTTP/1.1 200 OK
Vary: Accept
Content-Type: application/json

{
    "driver": "local_storage", 
    "name": "A", 
    "options": null
}
\end{lstlisting}
\caption{Exemple de réponse}
\end{figure}

\clearpage

#### GET `/services/(name: string)/stats`

Statistiques d'utilisation du service `name` (consommation mémoire et *CPU*, temps d'exécution).

\begin{figure}[h]
\begin{lstlisting}[language=json,firstnumber=1]
GET /api/v1.0/services/A/stats HTTP/1.1
Host: 127.0.0.1
Accept: application/json
\end{lstlisting}
\caption{Exemple de requête}
\end{figure}

\begin{figure}[h]
\begin{lstlisting}[language=json,firstnumber=1]
HTTP/1.1 200 OK
Vary: Accept
Content-Type: application/json

{
    "info": {
        "ctime": "0:00.54", 
        "started": 1420206477.527315, 
        "mem_info2": "1G", 
        "age": 95.96143507957458, 
        "cpu": 0.0, 
        "mem": 0.6, 
        "create_time": 1420206476.65, 
        "mem_info1": "23M"
    }, 
    "status": "ok", 
    "name": "A", 
    "time": 1420206573.518441
}
\end{lstlisting}
\caption{Exemple de réponse}
\end{figure}

\clearpage

#### GET `/services/(name: string)/status`

Statut du service `name` (actif, inactif).

\begin{figure}[h]
\begin{lstlisting}[language=json,firstnumber=1]
GET /api/v1.0/services/A/status HTTP/1.1
Host: 127.0.0.1
Accept: application/json
\end{lstlisting}
\caption{Exemple de requête}
\end{figure}

\begin{figure}[h]
\begin{lstlisting}[language=json,firstnumber=1]
HTTP/1.1 200 OK
Vary: Accept
Content-Type: application/json

{
    "status": "active", 
    "name": "A", 
    "time": 1420206603.0177
}
\end{lstlisting}
\caption{Exemple de réponse}
\end{figure}

\clearpage

#### PUT `/services/(name: string)/start`

Démarre le service `name`.

\begin{figure}[h]
\begin{lstlisting}[language=json,firstnumber=1]
PUT /api/v1.0/services/A/start HTTP/1.1
Host: 127.0.0.1
Accept: application/json
\end{lstlisting}
\caption{Exemple de requête}
\end{figure}

\begin{figure}[h]
\begin{lstlisting}[language=json,firstnumber=1]
HTTP/1.1 200 OK
Vary: Accept
Content-Type: application/json

{
    "status": "ok", 
    "name": "A", 
    "time": 1420206648.256163
}
\end{lstlisting}
\caption{Exemple de réponse}
\end{figure}

\clearpage

#### PUT `/services/(name: string)/stop`

Stoppe le service `name`.

\begin{figure}[h]
\begin{lstlisting}[language=json,firstnumber=1]
PUT /api/v1.0/services/A/stop HTTP/1.1
Host: 127.0.0.1
Accept: application/json
\end{lstlisting}
\caption{Exemple de requête}
\end{figure}

\begin{figure}[h]
\begin{lstlisting}[language=json,firstnumber=1]
HTTP/1.1 200 OK
Vary: Accept
Content-Type: application/json

{
    "status": "ok", 
    "name": "A", 
    "time": 1420206631.014166
}
\end{lstlisting}
\caption{Exemple de réponse}
\end{figure}

\clearpage

#### PUT `/services/(name: string)/restart`

Redémarre le service `name`.

\begin{figure}[h]
\begin{lstlisting}[language=json,firstnumber=1]
PUT /api/v1.0/services/A/restart HTTP/1.1
Host: 127.0.0.1
Accept: application/json
\end{lstlisting}
\caption{Exemple de requête}
\end{figure}

\begin{figure}[h]
\begin{lstlisting}[language=json,firstnumber=1]
HTTP/1.1 200 OK
Vary: Accept
Content-Type: application/json

{
    "status": "ok", 
    "name": "A", 
    "time": 1420206663.207203
}
\end{lstlisting}
\caption{Exemple de réponse}
\end{figure}

\clearpage
