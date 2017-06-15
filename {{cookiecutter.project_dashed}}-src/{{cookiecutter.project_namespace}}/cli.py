from __future__ import print_function

import click

from {{cookiecutter.project_namespace}}.version import VERSION


@click.group()
@click.pass_context
def {{cookiecutter.project_namespace}}(ctx):
    pass


@{{cookiecutter.project_namespace}}.command()
def version():
    click.echo('version: {}'.format(VERSION))


@{{cookiecutter.project_namespace}}.command()
@click.argument('name', default='World')
def hello(name):
    click.echo('Hello {}!'.format(name))


def cli_entry():
    {{cookiecutter.project_namespace}}()
