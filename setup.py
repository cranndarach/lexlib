from setuptools import setup

setup(name="wordutils",
      version="1.0.0",
      description="Utilities for research involving words.",
      url="https://github.com/cranndarach/wordutils",
      author="R. J. Steiner",
      author_email="r.steiner@uconn.edu",
      license="MIT",
      packages=["wordutils"],
      classifiers=[
          "Development Status :: 4 - Beta",
          "Intended Audience :: Science/Research",
          "License :: OSI Approved :: MIT License",
          "Programming Langauge :: Python :: 3"
      ],
      install_requires=["pandas"]
      )
