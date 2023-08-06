# -*- coding: utf-8 -*-
# flake8: noqa (ignore line length)

"""sktime."""

__version__ = "0.19.0"

__all__ = ["show_versions"]

from textwrap import dedent
from warnings import simplefilter, warn

from sktime.utils._maint._show_versions import show_versions


class PackageDeprecationWarning(DeprecationWarning):
    pass


def generate_deprecation_warning() -> None:
    message = dedent(
        """
        The sktime PyPI package is deprecated.
        The sktime project split into two projects.

        To find out how to install the new packages, please go to:

        * https://github.com/aeon-toolkit/aeon
        * https://github.com/sktime/sktime

        Here is what you can do when installing sktime via pip (e.g. using `pip install ...` or a requirement file like `requirements.txt`, `setup.py`, `setup.cfg`):

        * continue using the package without receiving any updates (ignoring the deprecation warning or avoiding it by pinning the version: `sktime==0.18.0`),
        * replace sktime with one of the new projects,
        * if the sktime package is used by one of your dependencies, it would be great if you take some time to track which package uses sktime and report to their issue tracker that sktime is deprecated.

        More information is available at:
        https://github.com/mloning/sktime-deprecation/discussions/2

        If the previous advice does not support your use case, feel free to report it at:
        https://github.com/mloning/sktime-deprecation/issues/new
    """
    )
    simplefilter("once", category=PackageDeprecationWarning)
    warn(message, category=PackageDeprecationWarning)


generate_deprecation_warning()
