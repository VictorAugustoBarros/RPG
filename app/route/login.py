import random
from flask import Flask
from flask import Blueprint
from utils.schema import Schema
from flasgger.utils import swag_from

base_url = ""
application = Flask(__name__)
login_blueprint = Blueprint("login", __name__, url_prefix=base_url)
schema = Schema()


@login_blueprint.route('/new_account/<email>/<login>/<senha>/<nick>/', methods=['POST'])
@swag_from('details_user/new_user.yml')
def new_account(email, login, senha, nick):
    return {"success": True}


@login_blueprint.route('/delete_account/<email>/<login>/<senha>/', methods=['DELETE'])
@swag_from('details_user/new_user.yml')
def delete_account(email, login, senha):
    return {"success": True}
