pytest-goldie: Golden Testing for pytest
========================================

.. image:: https://img.shields.io/pypi/v/pytest-goldie.svg
    :target: https://pypi.org/project/pytest-goldie
    :alt: PyPI version
.. image:: https://img.shields.io/pypi/l/pytest-goldie.svg
    :target: https://pypi.python.org/pypi/pytest-goldie

pytest-goldie is a pytest plugin that enables `golden testing <https://en.wikipedia.org/wiki/Characterization_test>`_ using pytest framework.
Golden testing is a methodology that compares the output of your code with a pre-recorded output. This package provides a fixture called `golden` that can be used to update test results and make test comparisons.

Example
-------

First, install the plugin:

.. code-block:: bash

    $ pip install pytest-goldie

Then, in your test file, use the `golden` fixture:

.. code-block:: python

    def my_function():
        return "Hello, world!"

    def test_my_function(golden):
        output = my_function()
        golden.test(output)

The `golden.test` method takes the output of your function and compares it to the saved output of a previous run. If the `update_goldens` flag is set, pytest-goldie will update the saved output with the new output.

To run the tests and update goldens, use the following command:

.. code-block:: bash

    $ pytest --update_goldens

By default, the golden files are stored in a folder named 'goldens'. You can change the folder name with --goldens_folder flag:

.. code-block:: bash

    $ pytest --goldens_folder my_goldens


This will set the goldens folder to "my_goldens" instead of the default "goldens".

License
-------

This software is licensed under the `MIT License <https://opensource.org/licenses/MIT>`_.

Created by Nick Kartashov and contributors.