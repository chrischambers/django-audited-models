======================
Django Audited Models:
======================

:author: Chris Chambers
:date: 2012/05/08

Django Audited Models provides a simple abstract base class (and factory
function) for tracking database record creation and modification times, as
well as the creator of the record and the last user to edit it. It leverages
two pluggable applications to achieve this:

1. `Django Extensions`_, which provides (amongst many other things) a
   ``CreationDateTimeField`` and ``ModificationDateTimeField``.
2. `Django Threaded Multihost`_, originally developed for Satchmo_, which
   provides a ``threadlocals`` mechanism that works reliably for Django
   installations powering multiple sites via the ``sites`` framework.


.. _`Django Extensions`: https://github.com/django-extensions/django-extensions
.. _`Django Threaded Multihost`: https://bitbucket.org/bkroeze/django-threaded-multihost
.. _Satchmo: http://www.satchmoproject.com/

Requirements
============

* Python 2.5+
* Django 1.2+
* Applications listed in ``requirements.txt``

You will also need to install the applications listed in
``requirements-dev.txt`` in order to run the test suite.
