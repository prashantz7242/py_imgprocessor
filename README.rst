===============
py-imgprocessor
===============


.. image:: https://img.shields.io/pypi/v/py_imgprocessor.svg
        :target: https://pypi.python.org/pypi/py_imgprocessor

.. image:: https://img.shields.io/travis/prashantz7242/py_imgprocessor.svg
        :target: https://travis-ci.com/prashantz7242/py_imgprocessor

.. image:: https://readthedocs.org/projects/py-imgprocessor/badge/?version=latest
        :target: https://py-imgprocessor.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status




opensource low resource usage image processor library written in python.


* Free software: BSD license
* Documentation: https://py-imgprocessor.readthedocs.io.

Scope
--------
1. Image processing with minimal system resourece usage.


Functional Scope
--------
1. Find possible objects from image.
- shapes,
- text
- arbitary patterns.
2. From image identify all the possible contexts & give passage on it.
- <img src="doc/img/photo-sunset.jpeg" alt="photo-sunset.jpeg" width="400" height="450">
- From above image guess about **This is sunset image. picture taken from bay! etc.**
     - Whatever possible info we can catch as passage from it.
3. Reduce image size without quality loss.
4. Append user defined image with current image that should looks & appear real.
5. Restore old images with super quality.
6. Find image fraudlent
-  Is image generated with AI?
-  Is image edited?
7. From the collections of image. Find particular categories images.
- like,
    - Without person.
    - With person
    - With 2 person only
    - With crowded
    - With text 
    - Without text
    - real estate image classifier
    - festive image classifier
    - find a particular 2 persons in images.
    - Find a car models names.

Features
--------

* -

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
