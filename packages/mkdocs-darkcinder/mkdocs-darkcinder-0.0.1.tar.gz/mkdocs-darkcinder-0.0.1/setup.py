from setuptools import setup, find_packages

file = open("README.md", "r")
LONG_DESCRIPTION = file.read()
file.close()

VERSION = "0.0.1"

setup(
    name="mkdocs-darkcinder",
    version=VERSION,
    url="https://github.com/ziroau/darkcinder",
    license="MIT",
    description="A clean, responsive MkDocs theme - Forked from Cinder with ❤",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author="ziroAU",
    packages=find_packages(),
    package_dir={
        "": "."
    },
    include_package_data=True,
    entry_points={
        "mkdocs.themes": [
            "darkcinder = darkcinder",
        ]
    },
    zip_safe=False,
)
