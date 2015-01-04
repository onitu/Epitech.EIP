# Configuration

La force d'Onitu réside dans ses capacités de configuration, allant des simples options au lancement du programme jusqu'à une gestion fine des transferts de fichiers, en permettant de réguler les échanges via les règles de configuration.

## Options de lancement

Quelques options existent pour déterminer le comportement d'Onitu au lancement, elles sont les suivantes:

#### `--setup`

Cette option permet de spécifier le fichier de configuration à utiliser par l'instance d'Onitu. Par défaut, le fichier `.config/onitu/setup.yml` de votre répertoire utilisateur (*HOME*) est utilisé.

#### `--no-dispatcher`

Utilisez cette option si vous souhaitez désactiver la journalisation des événements.

#### `--debug`

Lance Onitu en mode débogage. Cela aura pour effet d'être bien plus verbeux dans la journalisation des événements.

## Fichier de configuration

Le fichier de configuration permet de paramètrer les éléments plus durables de la configuration, qui seront conservés d'un lancement à l'autre.

Ce fichier est rédigé en syntaxe [*YAML*](http://fr.wikipedia.org/wiki/YAML).

Un exemple est disponible en figure \ref{config_example} qui servira de support aux explications.

\begin{figure}
\begin{lstlisting}[language=yaml,firstnumber=1]
name: "exemple"

folders:
  documents:
    mode: rw
  media:
    type:
      - image/
      - audio/
      - video/

services:

  Local:
    driver: local_storage
    root: files/

    folders:
      documents: Docs/
        blacklist:
          - "*~"
      media: Media/

  Backup:
    driver: ssh
    uri: "onitu@monserveur.net:onitu/"

    folders:
      media:
        mode: w
\end{lstlisting}
\caption{\label{config_example}Exemple de fichier de configuration}
\end{figure}

### Nom

Un premier paramètre de configuration est le nom de la configuration (paramètre `name`). En effet, plusieurs configurations peuvent cohabiter, et Onitu saura repérer les données relatives à l'une ou l'autre de ces configurations à l'aide de ce nom. Dans notre exemple, le nom est `exemple`.

### Dossiers

Onitu regroupe les fichiers en dossiers (ou *folders*). Un dossier ne représente pas seulement un répertoire sur le système de fichiers, mais associe des règles de synchronisation aux fichiers contenus.

Les paramètres présents dans la définition de chaque dossier sont les paramètres par défaut, et peuvent être surchargés pour chaque service.

Dans notre exemple, nous avons deux dossiers: `documents` et `pictures`. Le premier est paramétré pour synchroniser tous les fichiers qu'il contient, tandis que le second ne gère que les fichiers dont le type *MIME* commence par `image/`, `audio/` ou `video/`, c'est à dire les documents multimédia.

Les options de paramétrage des dossiers sont les suivantes:

#### mode

Indique le mode dans lequel le dossier doit considérer ses fichiers: `r` (lecture seule), `w` (écriture seule), ou `rw` (lecture/écriture).

En lecture seule, Onitu détectera les notifications des fichiers, mais ne procèdera jamais à des modifications sur ces fichiers.

En écriture seule, ce sera le comportement inverse, Onitu pourra modifier les fichiers, et les notifications seront ignorées.

Si aucun mode n'est précisé, `rw` est sélectionné par défaut.

#### type

Ce paramètre permet de filter les fichiers par types *MIME*. Les fichiers dont le type ne correspond pas à ceux énoncés seront ignorés.

Les types *MIME* n'ont pas besoin d'être écrits en totalité, la vérification se fera en testant si le type du fichier commence comme l'un des types listés. C'est à dire qu'il suffit d'utiliser `image/` pour reconnaître tous les types d'images.

#### file_size

Ce paramètre précise les tailles minimales et maximales des fichiers à gérer. Leur valeur est par défaut en octets, mais il existe de nombreux suffixes pour modifier l'unité:

* `o`, `b`: octets
* `k`, `ko`, `kb`: kilooctets ($10^3$)
* `m`, `mo`, `mb`: mégaoctets ($10^6$)
* `g`, `go`, `gb`: gigaoctets ($10^9$)
* `t`, `to`, `tb`: téraoctets ($10^{12}$)
* `p`, `po`, `pb`: pétaoctets ($10^{15}$)
* `ki`: kibioctets ($2^{10}$)
* `mi`: mébioctets ($2^{20}$)
* `gi`: gibioctets ($2^{30}$)
* `ti`: tébioctets ($2^{40}$)
* `pi`: pébioctets ($2^{50}$)

Ces unités sont insensibles à la casse.

Le paramètre se compose de deux sous-paramètres `min` et `max`, et s'utilise donc ainsi:

\begin{figure}[h]
\begin{lstlisting}[language=yaml,firstnumber=1]
file_size:
  min: 1k
  max: 2Go
\end{lstlisting}
\end{figure}

#### blacklist, whitelist

Ces deux paramètres définissent des listes de filtrage sur les chemins et noms de fichiers. Les valeurs peuvent être des chemins (dans ce cas, seront affectés les fichiers descendant de ce chemin), ou des expressions rationnelles utilisant la syntaxe *shell*.

Sont exclus tous les fichiers non reconnus par une des règles de `whitelist`, ou reconnus par un règle de `blacklist`.

### Services

Viennent ensuite les déclarations de services. Chaque service est défini avec un nom (la clef), le *driver* à instancier (`driver`), les dossiers à utiliser (`folders`), et les options propres à chaque *driver* (`options`).

La liste de dossiers permet aussi, comme précisé plus haut, de surcharger les configurations, et ainsi restreindre ou étendre l'utilisation d'un dossier pour un service particulier. Les noms de dossier peuvent aussi être directement suivis d'un chemin, qui sera le point de montage du dossier dans le service cible (par défaut, le nom du dossier est utilisé).

Les options du *driver* sont assez diverses, elles permettent de configurer les paramètres d'authentification, le point de montage sur le service (`root`), la fréquence de rafraîchissement des événements (`changes_timer`). Chaque *driver* définit les options par lequel il peut être configuré.
