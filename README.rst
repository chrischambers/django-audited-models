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

Installation
============

1. Install pip_.
2. Run ``pip install django-audited-models``.
3. Add ``threaded_multihost.middleware.ThreadLocalMiddleware`` to your list of
   ``MIDDLEWARE_CLASSES``.
4. Inherit from ``AuditedModel`` instead of ``models.Model`` in your django
   applications.
5. Profit!

.. _pip: http://www.pip-installer.org/en/latest/index.html
.. _setuptools: http://pypi.python.org/pypi/setuptools

Explanation
===========

Django-audited-models fulfils several needs:

1. This kind of metadata is almost always useful, and inexpensive to capture -
   most of your clients will just presume this information is logged and will
   be frustrated if they can't get at it ("What do you mean we can't see who
   created this record?")
2. Django's admin logging functionality provides some of this detail, but is
   flawed in that it only captures events which take place within the admin
   itself.
3. This app provides a consistent, logical naming convention and interface for
   the metadata.
4. This app makes use of several other applications to capture this
   information automatically. No need to pollute your views with unrelated
   logic or override ``ModelAdmin`` methods to store the user who created the
   record.
5. It's pluggable - simply drop it in, install its requirements, inherit from
   ``AuditedModel``, and you'll have your creation/modification dates and the
   users responsible for them, respectively. Similarly, replace your
   ``ModelAdmin`` with the ``AuditedAdmin`` subclass and you'll have some
   sensible defaults for the admin UI (readonly metadata fields, etc.).
6. As a bonus, ensures that ``MyModel.objects.latest()`` does something
   sensible by default - very handy when working with the interpreter,
   especially.

Some might question the verbosity of the time entry fields
(``datetime_created`` and ``datetime_modified``). Consider the following::

    >>> from datetime import date
    >>> latest_user = User.objects.latest('date_joined')
    >>> if latest_user.date_joined < date.today():
    >>>     print "Nobody has joined the site today."

    # Intuitively, this looks like it will work, but...
    TypeError: can't compare datetime.datetime to datetime.date

Python treats ``datetime`` objects very differently to ``dates``, and the
explicit fieldnames remind the developer of this difference and help prevent
errors due to incorrect assumptions.

Requirements
============

* Python 2.5+
* Django 1.2+
* Applications listed in ``requirements.txt``

You will also need to install the applications listed in
``requirements-dev.txt`` in order to run the test suite.
