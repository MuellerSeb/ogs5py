# -*- coding: utf-8 -*-
"""ogs5py: a python API for OpenGeoSys5"""

import os
from setuptools import setup, find_packages


HERE = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(HERE, "README.md"), encoding="utf-8") as f:
    README = f.read()
with open(os.path.join(HERE, "requirements.txt"), encoding="utf-8") as f:
    REQ = f.read().splitlines()
with open(os.path.join(HERE, "requirements_setup.txt"), encoding="utf-8") as f:
    REQ_SETUP = f.read().splitlines()
with open(os.path.join(HERE, "requirements_test.txt"), encoding="utf-8") as f:
    REQ_TEST = f.read().splitlines()
with open(
    os.path.join(HERE, "docs", "requirements_doc.txt"), encoding="utf-8"
) as f:
    REQ_DOC = f.read().splitlines()

REQ_DEV = REQ_SETUP + REQ_TEST + REQ_DOC

DOCLINE = __doc__.split("\n")[0]
CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Intended Audience :: End Users/Desktop",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Operating System :: MacOS",
    "Operating System :: MacOS :: MacOS X",
    "Operating System :: Microsoft",
    "Operating System :: Microsoft :: Windows",
    "Operating System :: POSIX",
    "Operating System :: Unix",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3 :: Only",
    "Topic :: Scientific/Engineering",
    "Topic :: Software Development",
    "Topic :: Utilities",
]

setup(
    name="ogs5py",
    description=DOCLINE,
    long_description=README,
    long_description_content_type="text/markdown",
    maintainer="Sebastian Mueller",
    maintainer_email="sebastian.mueller@ufz.de",
    author="Sebastian Mueller, Falk Hesse",
    author_email="info@geostat-framework.org",
    url="https://github.com/GeoStat-Framework/ogs5py",
    license="MIT",
    classifiers=CLASSIFIERS,
    platforms=["Windows", "Linux", "Solaris", "Mac OS-X", "Unix"],
    include_package_data=True,
    python_requires=">=3.5",
    use_scm_version={
        "relative_to": __file__,
        "write_to": "ogs5py/_version.py",
        "write_to_template": "__version__ = '{version}'",
        "local_scheme": "no-local-version",
        "fallback_version": "0.0.0.dev0",
    },
    install_requires=REQ,
    setup_requires=REQ_SETUP,
    extras_require={
        "gmsh": ["pygmsh"],  # optional for creating gmesh based meshes
        "show": ["mayavi"],  # optional to view a mesh
        "all": ["pygmsh", "mayavi"],  # everything
        "doc": REQ_DOC,
        "test": REQ_TEST,
        "dev": REQ_DEV,
    },
    packages=find_packages(exclude=["tests*", "docs*"]),
)
