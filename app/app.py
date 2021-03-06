from flask import Blueprint, render_template

from . import db

main = Blueprint('main', __name__)


@main.route('/')
def index():
    """Serve client-side application."""
    return render_template('index.html')
