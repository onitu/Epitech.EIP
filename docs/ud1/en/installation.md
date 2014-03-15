# Installation

The Onitu setup relies on *pip*, a command-line interface package manager very well known in the Python world.

*pip* takes care of retrieving the sources and resolving the dependencies of the project. Installing with independent packages avoids you to deal with useless dependencies.

## Setup

To install the project's core:

* `pip install onitu`

Then for each module (*driver*), by replacing `onitu-module_name` by the appropriate name, e.g. `onitu-ssh` or `onitu-dropbox`:

* `pip install onitu-module_name`

## Launch

\begin{figure}[h]
\includegraphics[scale=0.75]{screen_onitu.png}
\caption{Onitu starting}
\end{figure}

When the installation is finished, you can start *Onitu* just by the `onitu` command, at which you can pass a configuration file's path with the `--setup` option (by default, *Onitu* uses the file `.onitu/setup.json` in your user directory).

It allows you to launch, for example, multiple independent instances of *Onitu*, each having a different configuration and using different services.

Other options are also available:

* You can choose the *ZMQ* *socket* for the log by giving your own in `--log-uri` option.
* You can print debug logs with the `--debug` option.
* Finally, `--help` gives you the help of *Onitu* (this list of options).

## Uninstall

If you have to uninstall *Onitu*, you just have to execute the command `pip uninstall onitu`. It will delete *Onitu* along with all its modules (*drivers*) and its local configuration files.
