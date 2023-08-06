========
Pcrunner
========

|pypi| |docs| |pre-commit| |workflow-ci| |codecov|

Pcrunner (Passive Checks Runner is a daemon and service that periodically runs
Nagios_ / Icinga_ checks paralell. The results are posted via HTTPS to a
`NSCAweb`_ server.

Features
--------

* Runs as a daemon on Linux.
* Runs as a service on win32.
* Command line interface for single test runs and/or cron use.
* Parallel execution of check commands.
* Posts check results external commands.
* Termniation of check commands if maximum time exceeds.
* Configuration in YAML.
* Command definition in YAML or text format.


Credits
-------

This package was created with Cookiecutter_ and the
`audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _NSCAweb: https://github.com/smetj/nscaweb
.. _Nagios: https://www.nagios.org/
.. _Icinga: https://www.icinga.org/

.. |pypi| image:: https://img.shields.io/pypi/v/pcrunner.svg
    :alt: Pypi
    :target: https://pypi.python.org/pypi/pcrunner

.. |docs| image:: https://readthedocs.org/projects/pcrunner/badge/?version=latest
    :alt: Documentation Status
    :target: https://pcrunner.readthedocs.io/en/latest/

.. |pre-commit| image:: https://results.pre-commit.ci/badge/github/maartenq/pcrunner/main.svg
    :alt: pre-commit.ci status
    :target: https://results.pre-commit.ci/latest/github/maartenq/pcrunner/main

.. |workflow-ci| image:: https://github.com/maartenq/pcrunner/workflows/ci/badge.svg?branch=main
    :alt: CI status
    :target: https://github.com/maartenq/pcrunner/actions?workflow=ci

.. |codecov| image:: https://codecov.io/gh/maartenq/pcrunner/branch/master/graph/badge.svg?token=INVK104RNN
    :alt: Codecov
    :target: https://codecov.io/gh/maartenq/pcrunner
