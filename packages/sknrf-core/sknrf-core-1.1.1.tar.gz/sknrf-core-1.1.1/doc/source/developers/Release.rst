.. sknrf documentation introduction file

..  figure:: ../_images/PNG/sknrf_logo.png
    :width: 500 pt
    :align: center

Release Process
===============

Generate a release as follows:
    * Increment version in module and submodules:
        * Increment Version number in: cmake/root.cmake
        * Update the download_url in: setup.py
    * Update submodules: git pull origin master ; git submodule sync ; git submodule update --init --recursive --remote
    * Run Unit Tests: nosetests --config=nose.cfg --with-coverage
    * Run the Build: python setup.py clean ; python setup.py config ; python setup.py build ; python setup.py install ; python setup.py upload_doc
    * Create the Package: python setup.py sdist bdist_wheel
    * Submit code: git add . ; git commit -m "Release vX.X.X" ; git push origin master
    *

Increment the Version number in the module and submodules:

.. code-block:: bash

    vim cmake/root.cmake                                                        # Update the SKNRF_VERSION_{MAJOR | MINOR | PATCH}
    vim setup.py                                                                # Update the download_url

Build and test the release as follows:

.. code-block:: bash

    git pull origin master                                                      # Update module
    git submodule sync                                                          # Sync submodule state
    git submodule update --init --recursive --remote                            # Update submodules
    python setup.py clean                                                       # make clean
    python setup.py config                                                      # cmake ..
    python setup.py build                                                       # make
    python setup.py install                                                     # make install
    nosetests --config=nose.cfg --with-coverage                                 # Run Unit Tests

Deploy the release as follows:

.. code-block:: bash

    git add .                                                                   # Add
    git commit -m "vX.X.X Release"                                              # Commit
    git push origin master                                                      # Push
    git tag vX.X.X                                                              # Tag
    git push origin --tags                                                      # Push Tag
    python setup.py sdist bdist_wheel                                           # Build source, binary package
    python setup.py upload_doc                                                  # Upload doc to homepage
    twine upload dist/*                                                         # Upload to PyPI
    mv dist/sknrf_core-1.0.1-cp37-abi3-linux_x86_64.whl dist/sknrf_core-1.0.1-cp37-abi3-manylinux2014_x86_64.whl

Create the release on gitlab.



