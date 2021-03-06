from distutils.core import setup

setup(
    name="django-audited-models",
    version="0.4.alpha",
    author="Chris Chambers",
    author_email="magma.chambers@gmail.com",
    description=(
        "An abstract base class providing automatic creator/editor/"
        "datetime_created/datetime_modified fields."
    ),
    long_description=open("README.rst").read(),
    license="BSD",
    url="https://github.com/chrischambers/django-audited-models",
    keywords=['django', 'auditing', 'automatic', 'abstract'],
    packages=[
        'audited_models',
        'test_project',
        'test_project.test_app',
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ],
    install_requires=[
        "Django >= 1.3",
        "django-extensions == 0.8",
        "django-threaded-multihost == 1.4-1",
    ],
)
