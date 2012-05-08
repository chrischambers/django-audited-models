from distutils2.core import setup, find_packages

setup(
    name="django-audited-models",
    version="0.1.alpha",
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
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
        "Topic :: Auditing",
    ]
)
