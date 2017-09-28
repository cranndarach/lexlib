from setuptools import setup

ver = "2.0.0"
repo = "https://github.com/cranndarach/lexlib"
setup(name="lexlib",
      version=ver,
      description="Utilities for research involving words.",
      keywords="psycholinguistics research words language linguistics \
                psychology cognitive science cogsci",
      url=repo,
      download_url="{}/tarball/{}".format(repo, ver),
      author="R. J. Steiner",
      author_email="r.steiner@uconn.edu",
      license="MIT",
      classifiers=[
          "Development Status :: 4 - Beta",
          "Intended Audience :: Science/Research",
          "License :: OSI Approved :: MIT License"
          ]
      )
