# Configuration rules

Configuration is currently basic and is done by manually editing the configuration file, written in *JSON* format.

An example configuration will be used through this chapter, which you'll be able to find in Figure \ref{json_example}.

## Name

First of all, each *JSON* configuration has a `name` attribute, defining its name.

This name is used internally for request treatment and to permit the simultaneous execution of multiple different configurations.

## Entries

The `entries` section of the *JSON* document permits to list the entries.

Entries are *drivers* instances, and thus reflect the configuration of an account on a given service. Each entry is associated with a key used to identify it, for example in the configuration rules.

An entry contains a `driver` field that contains the name of the *driver* to be instantiated, and an `options` field for *driver-specific* options, like login informations.

We use two entries in our example: the first manages local files, and the second one is logged on to a *Dropbox* account.

\newpage

### Local storage

The name of the *driver* to use for local files is `local_storage`. This driver only needs the root directory from which it will work, `root`, as an option.

Here is a possible configuration:

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

The name of the *Dropbox driver* simply is `dropbox`. It is configured with the Dropbox account's *e-mail* address and password (`email` and `password` fields).

In the project's current state, the account password is stored in plain text in the file.

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

## Rules

Rules permit to define which files must be synchronized on which entries, and are placed in the document's `rules` section.

In our example, we wish to transfer all files modifications (creation, update or removal) to the «Local» entry, but only those dealing with images in the `photos/` directory, with *JPG* or *PNG* types, to *Dropbox*, like shown in the following figures:

\begin{figure}[h]
\includegraphics[scale=0.75]{rules_schema_1.png}
\caption{File creation on \emph{Dropbox}}
\end{figure}

\begin{figure}[h]
\includegraphics[scale=0.75]{rules_schema_2.png}
\caption{File creation on \emph{Local}}
\end{figure}

A rule is made of a set of two elements: the acceptation condition of a file and the list of target entries.

The condition lists the file attributes you want to test, currently available conditions are file path (`path`), and a *MIME* (`mime`) file types list. The condition is provided as a dictionnary associated to the `match` key.

The list of target entries (named `sync`) contains the names of entries concerned by the rule.

\newpage

The rules used in our example are written this way:

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

In the future, conditions on the file name or its size will also be available.


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
\caption{Example \emph{setup.json} file}
\label{json_example}
\end{figure}