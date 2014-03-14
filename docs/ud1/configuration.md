# Règles de configuration

La configuration est pour le moment rudimentaire et se réalise par une édition manuelle du fichier de configuration, rédigé au format *JSON*.

Un exemple de configuration sera utilisé tout au long de ce chapitre, que vous pouvez retrouver en figure \ref{json_example}.


## Le nom

Premièrement, chaque configuration *JSON* possède un attribut `name` déterminant son nom.

Ce nom est utilisé en interne pour le traitement des requêtes, et permettre de faire tourner simultanément plusieurs configurations différentes.


## Les entrées

La section `entries` du document *JSON* vous permet de lister les entrées.

Les entrées sont des instances de *drivers*, et correspondent donc au paramétrage d'un compte sur un service. Chaque entrée est associée à une clef permettant de l'identifier, dans les règles par exemple.

Une entrée contient un champ `driver` contenant le nom du *driver* à instancier, et un champ `options` pour les options spécifiques à chaque *driver*, comme les données de connexion.

Dans notre exemple, nous utiliserons deux entrées: une première pour servir des fichiers locaux et une seconde connectée à un compte *Dropbox*.

\newpage

### Fichiers locaux

Le nom du *driver* à utiliser pour les fichiers locaux est `local_storage`. Ce *driver* n'a besoin en option que du répertoire racine à partir duquel il opérera, `root`.

Une configuration possible est la suivante:

\begin{figure}[h]
\begin{lstlisting}[language=json,firstnumber=1]
"Local": {
  "driver": "local_storage",
  "options": {
    "root": "example/local_driver"
  }
}
\end{lstlisting}
\end{figure}

### *Dropbox*

Le nom du *driver* *Dropbox* est simplement `dropbox`. Il se configure à l'aide de l'adresse *e-mail* et du mot de passe du compte (champs `email` et `password`).

Dans l'état actuel du projet, le mot de passe associé au compte est stocké en clair dans le fichier.

\begin{figure}[h]
\begin{lstlisting}[language=json,firstnumber=1]
"Dropbox": {
  "driver": "dropbox",
  "options": {
    "email": "foo@bar.com"
    "password": "my_password"
  }
}
\end{lstlisting}
\end{figure}

\newpage

## Les règles

Les règles vous permettent de définir quels fichiers doivent être synchronisés vers quelles entrées, et s'insèrent dans la section `rules` du document.

Dans notre exemple, nous souhaitons que toutes les modifications (création, mise à jour ou suppression) de fichiers soient transférées à l'entrée «Local», mais que seules celles opérant sur des images du répertoire `photos/`, et de type *JPG* ou *PNG*, soient relayées à *Dropbox*, comme explicité sur les schémas ci-dessous:

\begin{figure}[h]
\includegraphics[scale=0.75]{rules_schema_1.png}
\caption{Création d'un fichier sur \emph{Dropbox}}
\end{figure}

\begin{figure}[h]
\includegraphics[scale=0.75]{rules_schema_2.png}
\caption{Création d'un fichier sur \emph{Local}}
\end{figure}

Une règle consiste en un ensemble de deux éléments: la condition d'acceptation d'un fichier et l'ensemble de entrées cibles.

La condition liste les différents attributs du fichier que vous voulez tester, sont pour l'instant disponibles le chemin du fichier (`path`), et une liste de types *MIME* (`mime`). La condition s'entre en tant que dictionnaire associé à la clef `match`.

L'ensemble des cibles est une simple liste (nommée `sync`) des noms des entrées affectées par la règle.

Les règles que nous utilisons pour notre exemple s'écrivent de la manière suivante:
\begin{figure}[h]
\begin{lstlisting}[language=json,firstnumber=1]
"rules": [
  {
    "match": {"path": "/"},
    "sync": ["Local"]
  },
  {
    "match": {"path": "/photos/", "mime": ["image/png", "image/jpeg"]},
    "sync": ["Dropbox"]
  }
]
\end{lstlisting}
\end{figure}

Par la suite seront aussi disponibles des conditions sur le nom du fichier ou sur sa taille.



\begin{figure}[p]
\begin{lstlisting}[language=json,firstnumber=1]
{
  "name": "setup_example",

  "entries": {
    "Local": {
      "driver": "local_storage",
      "options": {
        "root": "example/local_driver"
      }
    },
    "Dropbox": {
      "driver": "dropbox",
      "options": {
        "email": "foo@bar.com"
        "password": "my_password"
      }
    }
  },

  "rules": [
    {
      "match": {"path": "/"},
      "sync": ["Local"]
    },
    {
      "match": {"path": "/photos/", "mime": ["image/png", "image/jpeg"]},
      "sync": ["Dropbox"]
    }
  ]

}
\end{lstlisting}
\caption{Fichier \emph{setup.json} d'exemple}
\label{json_example}
\end{figure}