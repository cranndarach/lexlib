from setuptools import setup

ver = "1.1.1"
setup(name="lexlib",
      version=ver,
      description="Utilities for research involving words.",
      keywords=[
            "psycholinguistics",\
            "research",\
            "words",\
            "language",\
            "linguistics",\
            "psychology",\
            "cognitive",\
            "cognitive science",\
            "cogsci"\
            ],
      url="https://github.com/cranndarach/lexlib",
      download_url="https://github.com/cranndarach/lexlib/tarball/{}".format(
            ver),
      author="R. J. Steiner",
      author_email="r.steiner@uconn.edu",
      license="MIT",
      packages=["lexlib"],
      classifiers=[
          "Development Status :: 4 - Beta",
          "Intended Audience :: Science/Research",
          "License :: OSI Approved :: MIT License"
          ],
      install_requires=["pandas"]
      )
