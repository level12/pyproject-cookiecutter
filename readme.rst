PyProject CookieCutter
######################

This cookiecutter is a template for starting a python project.

Preparation
===========

You will need to do the following before you use this cookiecutter:

* Create a repo for the project on GitHub
* CircleCI

  * Projects -> Add Project
  * Project Settings -> API Permissions -> Create Status Token
  * Add token as `circle_badge_token` in `cookicutter.json`

* Codecov

  * Add new repository
  * Add "Upload Token" as `codecov_api_token` in `cookicutter.json`
  * Settings -> Badge -> copy token to `codecov_badge_token` in `cookicutter.json`

* Update all values in `cookiecutter.json`

Usage
=====

It's recommended that you install the latest version of cookiecutter at the user level::

    pip install -U cookiecutter --user

Once cookiecutter is installed, you can use this cookiecutter like::

    cookiecutter <PYPROJ-CC-DIR> --no-input --overwrite-if-exists -o <CREATE-PROJ-IN-DIR>
