.. sknrf documentation introduction file

..  figure:: ../_images/PNG/sknrf_logo.png
    :width: 500 pt
    :align: center

Anaconda
========

Conda Build Process
-------------------
conda-build performs the following steps:

    1. Reads the metadata.
    2. Downloads the source into a cache.
    3. Extracts the source into the source directory.
    4. Applies any patches.
    5. Re-evaluates the metadata, if source is necessary to fill any metadata values.
    6. Creates a build environment, and then installs the build dependencies there.
    7. Runs the build script. The current working directory is the source directory with environment variables set. The build script installs into the build environment.
    8. Performs some necessary post-processing steps, such as shebang and rpath.
    9. Creates a conda package containing all the files in the build environment that are new from step 5, along with the necessary conda package metadata.
    10. Tests the new conda package if the recipe includes tests:
    11. Deletes the build environment.
    12. Creates a test environment with the package and its dependencies.
    13. Runs the test scripts.

The conda-recipes repo contains example recipes for many conda packages.

Generate Skeleton for Packages on PyPi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

From the repos folder, run the following commands:

.. code-block:: bash

    >>> conda skeleton pypi jplephem # Dependency located on pypi
    >>> conda skeleton pypi sgp4 # Dependency located on pypi
    >>> conda skeleton pypi skyfield

Read the Metadata
~~~~~~~~~~~~~~~~~

From the repos folder, run the following commands:

.. code-block:: bash

    >>> conda build --python 3.6 --check skyfield


Download the Source Into Cache
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

From the repos folder, run the following commands:

.. code-block:: bash

    >>> conda build --python 3.6 --source skyfield


Creates a build environment and Runs the build script
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

From the repos folder, run the following commands:

.. code-block:: bash

    >>> conda build --python 3.6 --no-test jplephem # Dependency
    >>> conda build --python 3.6 --no-test sgp4 # Dependency
    >>> conda build --python 3.6 --no-test skyfield


Creates a test environment and Runs the test scripts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

From the repos folder, run the following commands:

.. code-block:: bash

    >>> conda build --python 3.6 jplephem # Dependency
    >>> conda build --python 3.6 sgp4 # Dependency
    >>> conda build --python 3.6 skyfield

Conda Install
-------------

Install Local Build
~~~~~~~~~~~~~~~~~~~

From the repos folder, run the following commands:

.. code-block:: bash

    >>> conda install --use-local skyfield

Test the installation from the terminal:

.. code-block:: bash

    >>> python
    >>> import skyfield



