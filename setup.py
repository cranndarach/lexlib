from setuptools import setup
from os import path

# Load the README.
wd = path.abspath(path.dirname(__file__))
with open(path.join(wd, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

ver = "2.2.1"
repo = "https://github.com/cranndarach/lexlib"
setup(name="lexlib",
      version=ver,
      description="Utilities for research involving words.",
      long_description=long_description,
      long_description_content_type="text/x-rst",
      keywords="psycholinguistics research words language linguistics \
                psychology cognitive science cogsci",
      url=repo,
      download_url="{}/tarball/{}".format(repo, ver),
      author="R. J. Steiner",
      author_email="r.steiner@uconn.edu",
      license="MIT",
      packages=["lexlib"],
      classifiers=[
          "Development Status :: 4 - Beta",
          "Intended Audience :: Science/Research",
          "License :: OSI Approved :: MIT License"
          ]
      )
