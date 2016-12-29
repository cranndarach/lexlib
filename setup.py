from setuptools import setup

setup(name="lexlib",
      version="1.0.0",
      description="Utilities for research involving words.",
      keywords=[
            "psycholinguistics",
            "research",
            "words",
            "language",
            "linguistics",
            "psychology",
            "cognitive",
            "cognitive science",
            "cogsci"
            ],
      url="https://github.com/cranndarach/lexlib",
      download_url="https://github.com/cranndarach/lexlib/tarball/0.1.0",
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
