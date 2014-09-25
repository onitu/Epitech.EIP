# Configuration

Une fois qu'Onitu et les modules des services que vous désirez utiliser sont correctement installés avec PIP, il reste à configurer leur utilisation au sein du logiciel.

Pour ce faire, la configuration d'Onitu s'effectue par l'édition d'un fichier de configuration au format *JSON*.

Un exemple de configuration sera utilisé tout au long de ce chapitre, que vous pouvez retrouver en figure \ref{json_example}.

Dans ce chapitre, nous allons aborder, point par point, tout ce qu'il y a à savoir pour configurer *Onitu* et ses services.

## Le nom

Premièrement, chaque configuration *JSON* possède un attribut `name` déterminant son nom.

Ce nom est utilisé en interne pour permettre de lancer simultanément plusieurs configurations différentes.


## Les entrées

La section `entries` du document *JSON* vous permet de lister les entrées.

Une entrée est une instance de *driver*, et correspond au paramétrage d'un compte sur un service. Chaque entrée est associée à une clef permettant de l'identifier, dans les règles par exemple.

Une entrée est composée :

* d'un nom permettant de l'identifier de manière unique : "dropbox-bob", "dropbox-alice"...
* d'un champ `driver` contenant le nom du *driver* à instancier, en général le même que celui du service supporté par ce *driver*, comme *dropbox* ou *google_drive*
* d'un champ `options` pour les options de lancement ce *driver*. Ces options sont spécifiques à chaque service, comme les données de connexion, et peuvent varier selon les *drivers*. Dans cette documentation, le symbole\Mandatory{} symbolise qu'il s'agit d'un champ obligatoire.

Dans notre exemple, nous utiliserons deux entrées: une première pour servir des fichiers locaux et une seconde connectée à un compte *Dropbox*.

\newpage


### Fichiers locaux

Ce driver est inclus dans l'installation de base d'*Onitu*. Il permet de transférer et synchroniser des fichiers avec votre système de fichiers local, sur votre disque dur.

Le nom à utiliser pour le *driver* des fichiers locaux est `local_storage`. Ce *driver* ne comporte qu'une option :

* \Mandatory{root} : le répertoire racine à partir duquel il opère.


**Attention**: le nom du répertoire racine est relatif à celui dans lequel est contenu *Onitu*.


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

Le nom du *driver* *Dropbox* est simplement `dropbox`. Il comporte quatre options :

* \Mandatory{root} : le dossier à l'intérieur duquel Onitu placera tous vos fichiers sur Dropbox
* \Mandatory{access\_key} : votre clé d'accès Dropbox
* \Mandatory{access\_secret} : votre clé secrète Dropbox
* **changes_timer** : la fréquence à laquelle Onitu vérifie les changements sur le compte Dropbox, en secondes. La valeur par défaut est **60 secondes**.

Pour obtenir vos clés d'accès, vous devrez vous servir du script d'authentification get_access_token.py fourni à l'installation du driver Dropbox. Vous devez au préalable être connecté-e sur Dropbox.

\begin{figure}[h]
\includegraphics[scale=0.65]{screen_dropbox.png}
\caption{Utilisation du script get\_access\_token.py (sur Ubuntu)}
\end{figure}

Dans l'état actuel du projet, ces informations sont stockés en clair dans le fichier.

\newpage

Un exemple de configuration d'entrée Dropbox réussie :

\begin{figure}[h]
\begin{lstlisting}[language=json,firstnumber=1]
"dropbox-bob": {
  "driver": "dropbox",
  "options": {
    "access_key": "MY_ACCESS_KEY"
    "access_secret": "MY_SECRET_KEY"
  }
}
\end{lstlisting}
\end{figure}

### Amazon S3

Le nom du *driver* Amazon S3 est `amazon_s3`. Il vous permet de connecter un *bucket* Amazon S3 à Onitu.

**Attention**: Amazon S3 est un service payant au nombre de requêtes HTTP effectuées avec lui. L'utilisation d'Onitu ne déroge pas à cette règle, et c'est pourquoi votre activité avec Amazon S3 au travers d'Onitu vous sera facturée par Amazon tout comme des transferts classiques.

L'entrée du *driver* Amazon S3 comporte cinq options :

* \Mandatory{root} : le dossier à l'intérieur duquel Onitu placera tous vos fichiers sur Amazon S3
* \Mandatory{bucket} : le bucket Amazon S3 avec lequel Onitu doit se connecter
* \Mandatory{aws\_access\_key} : votre clé d'accès AWS
* \Mandatory{aws\_access\_secret} : votre clé secrète AWS
* **changes_timer** : la fréquence à laquelle Onitu vérifie les changements sur le bucket Amazon S3, en secondes. La valeur par défaut est **10 secondes**. **Cette action consomme 2 requêtes HTTP GET.**

Si vous ne possédez pas déjà vos clés d'accès Amazon S3, il faut vous connecter à votre compte Amazon et vous rendre à l'adresse \url{https://console.aws.amazon.com/iam/home?#security_credential}.

Pour créer une nouvelle paire de clés, cliquez sur "Create New Access Keys". L'opération devrait être instantanée et générer un ID de clé d'accès et une clé d'accès secrète. Ce sont les clés que vous devez utiliser avec Onitu.

\begin{figure}[h]
\includegraphics[scale=0.5]{create_access_keys_s3}
\caption{Interface pour créer vos clés Amazon S3}
\end{figure}

\begin{figure}[h!]
\includegraphics[scale=0.5]{access_keys_s3}
\caption{Une fois terminé, les clés générées sont celles utilisables avec Onitu}
\end{figure}


\newpage


\newpage


Dans l'état actuel du projet, ces informations sont stockés en clair dans le fichier.

\newpage

Un exemple de configuration d'entrée Amazon S3 réussie :

\begin{figure}[h]
\begin{lstlisting}[language=json,firstnumber=1]
"amazon-s3-alice": {
  "driver": "amazon_s3",
  "options": {
    "root": "onitu/",
    "bucket": "my-bucket",
    "aws_access_key": "MY_ACCESS_KEY",
    "aws_secret_key": "MY_SECRET_KEY",
    "changes_timer" : 300
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
