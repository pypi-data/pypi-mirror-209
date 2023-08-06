=======
idem-ai
=======

.. image:: https://img.shields.io/badge/made%20with-pop-teal
   :alt: Made with pop, a Python implementation of Plugin Oriented Programming
   :target: https://pop.readthedocs.io/

.. image:: https://img.shields.io/badge/made%20with-idem-teal
   :alt: Made with idem, a Python implementation of Plugin Oriented Programming
   :target: https://www.idemproject.io/

.. image:: https://img.shields.io/badge/docs%20on-docs.idemproject.io-blue
   :alt: Documentation is published with Sphinx on docs.idemproject.io
   :target: https://docs.idemproject.io/idem-ai/en/latest/index.html

.. image:: https://img.shields.io/badge/made%20with-python-yellow
   :alt: Made with Python
   :target: https://www.python.org/


``idem-ai`` extends idem with translation capabilities from the `pop-ml <https://gitlab.com/vmware/pop/pop-ml>`__ plugin,
enabling multilingual support in infrastructure management workflows.

* `idem-ai source code <https://gitlab.com/vmware/idem/idem-ai>`__
* `idem-ai documentation <https://docs.idemproject.io/idem-ai/en/latest/index.html>`__

About
=====

``idem-ai`` extends idem, a powerful infrastructure and configuration management tool,
by adding translation capabilities from the pop-ml plugin.
With idem-ai, you can enable multilingual support in your infrastructure management workflows.

By integrating idem-ai into your idem environment,
you gain access to additional contracts and features that enable translation in various aspects of idem.
The added contracts from ``idem-ai`` provide translation capabilities for logs, state comments, and rend output.
This means you can translate log messages,
comments within your states,
and the rendered output of commands to facilitate communication in multiple languages.

idem-ai also introduces an `ml.translate` exec module,
which allows you to perform on-the-fly translations using pop-ml.
This module can be used within Jinja in SLS or invoked directly on the command line,
giving you flexibility in translating text in your idem environment.

With idem-ai, you can effortlessly manage multilingual environments,
ensuring clear and consistent communication across language barriers in your infrastructure management workflows.

What is POP?
------------

This project is built with `pop <https://pop.readthedocs.io/>`__, a Python-based
implementation of *Plugin Oriented Programming (POP)*. POP seeks to bring
together concepts and wisdom from the history of computing in new ways to solve
modern computing problems.

For more information:

* `Intro to Plugin Oriented Programming (POP) <https://pop-book.readthedocs.io/en/latest/>`__
* `pop-awesome <https://gitlab.com/vmware/pop/pop-awesome>`__
* `pop-create <https://gitlab.com/vmware/pop/pop-create/>`__

Getting Started
===============

Prerequisites
-------------

* Python 3.8+
* git *(if installing from source, or contributing to the project)*

Installation
------------

.. note::

   If wanting to contribute to the project, and setup your local development
   environment, see the ``CONTRIBUTING.rst`` document in the source repository
   for this project.

If wanting to use ``idem-ai``, you can do so by either
installing from PyPI or from source.

Install from PyPI
+++++++++++++++++

.. code-block:: bash

   pip install idem-ai

Install from source
+++++++++++++++++++

.. code-block:: bash

   # clone repo
   git clone git@gitlab.com/vmware/idem/idem-ai.git
   cd idem-ai

   # Setup venv
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -e .

Usage
=====

To use ``idem-ai``, you need to create a YAML configuration file that defines the behavior of the translation.

Here's an example YAML configuration file:

.. code-block:: yaml

    idem:
      translate_output: False
      translate_comments: False
      translate_docs: False
      translate_logs: False
    pop_ml:
      source_lang: en
      dest_lang: es

This configuration file contains various options that control the translation behavior:

- ``translate_output``: If set to True, the output of the execution will be translated. Default is False.
- ``translate_comments``: If set to True, the comments of states  and exec moduleswill be translated. Default is False.
- ``translate_logs``: If set to True, the log messages will be translated. Default is False.
- ``dest_lang``: The destination language for translation. Default is "es".
- ``source_lang``: The source language for translation. Default is "en".

The ``dest_lang`` parameter is required for the translation to work. It should be a two-letter language code.

You can modify these options based on your requirements.

Examples
--------

Here are some example commands that demonstrate the usage of idem-ai:

Translate a text using the ml.translate exec module:

.. code-block:: bash

    idem exec ml.translate "Hello World!" dest_lang=es

.. note::

    Make sure to replace config.yaml with the path to your actual YAML configuration file.

Translate logs using the `--translate-logs` option:

.. code-block:: bash

    idem -c my_config.cfg exec test.ping --translate-logs --log-level=debug

In this example, the --translate-logs option enables the translation of logs with pop-ml.
This will translate the log messages into the specified destination language.

Translate state comments using the --translate-state-comments option:

.. code-block:: bash

    idem -c my_config.cfg state my_state.sls --translate-state-comments

In this example, the --translate-state-comments option enables the translation of state comments.
This will translate the comments from state output from the run into the specified destination language.

Translate rend output using the --translate-output option:

.. code-block:: bash

    idem -c my_config.cfg exec test.ping --translate-output

In this example, the --translate-output option enables the translation of rend output for a doc subcommand.
However, please note that enabling this option may cause unpredictable behavior for CLI programs.
It is recommended to use it with caution.

Translate docstrings from ``idem doc`` using the --translate-docs option:

.. code-block:: bash

    idem -c my_config.cfg doc exec.test.ping --translate-docs

In this example, the --translate-docs option enables the translation of docs for the exec.test.ping command.
This will translate the documentation associated with the specified command into the specified destination language
without translating keys, paths, refs, and other values unrelated to docs.

.. note::

    idem's CLI options take precedence over the options specified in the configuration file.
    This means that if you specify an option both in the configuration file and as a command-line argument,
    the command-line argument will take precedence.

Roadmap
=======

Reference the `open issues <https://gitlab.com/vmware/idem/idem-ai/-/issues>`__ for a list of
proposed features (and known issues).

Acknowledgements
================

* `Img Shields <https://shields.io>`__ for making repository badges easy.
