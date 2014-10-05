## Client

Le client est le programme permettant de déployer facilement Onitu sur plusieurs machines en conservant une configuration commune. Le serveur sera lancé avec sa configuration et les clients viendront s'y connecter, ils communiqueront ainsi au sein d'un même réseau Onitu.

L'architecture du client est copiée sur celle du serveur, les *drivers* sont placés dans le même répertoire et le *Plug* simule celui du serveur par des appels réseaux.

### Authentification

Chaque client est identifié par un couple de clefs publique/privée automatiquement générées. La clef publique du client doit être connue du serveur pour que celui-ci puisse s'y connecter (elle doit être présente dans le dossier `authorized_keys/` du serveur).

De la même manière, pour des raisons de sécurité, le client doit être capable de vérifier l'identité du serveur, et donc pour cela avoir le fichier de clef publique `server.key` dans son répertoire `keys`/.

Une fois ces étapes respectées, il suffit de lancer le client pour que celui-ci se connecte auprès du serveur. Un *driver* de type *remote-driver* (pilote distant) sera alors instancié du côté du serveur.

### *Plug*

Le *Plug* dans le client agit comme un *proxy*, fonctionnant dans les deux sens. Toute requête faite auprès du *remote-driver* sera relayée au client via le *Majordomo*. Et toute requête faite sur le *Plug* du client sera de la même manière transmise à celui du *remote-driver* à l'aide du *Majordomo*.

Ces opérations sont totalement transparentes et le *driver* tournant sur le client n'a pas à se soucier de savoir s'il tourne avec un réel *Plug* ou à l'aide d'un *proxy*.
