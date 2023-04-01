import os

import flask as f

import toml

from .usermanager import UserManager
from .linkmanager import LinkManager
from .page import page_bp
from .search import search_bp
from .add import add_bp
from .users import users_bp
from .vote import vote_bp


def create_app(config_dict=None):
    app = f.Flask("owdex")

    for file in ("../../owdex.toml", "/owdex.toml"):
        try:
            app.config.from_file(file, load=toml.load)
        except FileNotFoundError:
            pass

    if config_dict:
        app.config = app.config | config_dict

    app.um = UserManager(app.config["ADMIN_USERNAME"],
                         app.config["ADMIN_PASSWORD"])

    app.lm = LinkManager(["stable", "unstable", "archive"])

    with app.app_context():
        app.register_blueprint(page_bp)
        app.register_blueprint(search_bp)
        app.register_blueprint(add_bp)
        app.register_blueprint(users_bp)
        app.register_blueprint(vote_bp)

    return app
