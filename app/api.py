from flask import Blueprint

from . import db


api = Blueprint('api', __name__)


@api.route('/version', methods=['GET'])
def get_version():
    """
    Return string of the current web application version.
    This endpoint is publicly available.
    """
    return '0.0.1'
