# manage.py

from flask import app
from flask.app import Flask
from src import api, app
from flask.cli import FlaskGroup


cli = FlaskGroup(app)


if __name__ == '__main__':
    cli()
