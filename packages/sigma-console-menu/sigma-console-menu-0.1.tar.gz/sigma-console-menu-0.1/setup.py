from setuptools import setup, find_packages

VERSION = "0.1"
DESCRIPTION = "Sigma console menu"

with open("README.md") as readme_file:
    README = readme_file.read()

with open("HISTORY.md") as history_file:
    HISTORY = history_file.read()

setup(
    name="sigma-console-menu",
    version=VERSION,
    author="Karol Angrys",
    author_email="karol.angrys@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=README + "\n\n" + HISTORY,
    license="MIT",
    packages=find_packages(),
    install_requires=["keyboard"],
)
