import random
from flask import Flask
from flask import Blueprint
from flask import request
from flasgger.utils import swag_from
from utils.schema import Schema
from utils.request_log import RequestLog
from utils.authorization import Authorization
from service.sms.v1.company import Company
from flasgger.utils import swag_from
from flask import Flask, jsonify, request

base_url = "/api/v1/sms"
application = Flask(__name__)
rpg_blueprint = Blueprint("sms", __name__, url_prefix=base_url)
schema = Schema()


@rpg_blueprint.route('/api/<string:language>/', methods=['GET'])
@swag_from('index.yml')
def index(language):
    language = language.lower().strip()
    features = [
        "awesome", "great", "dynamic",
        "simple", "powerful", "amazing",
        "perfect", "beauty", "lovely"
    ]
    size = int(request.args.get('size', 1))
    if language in ['php', 'vb', 'visualbasic', 'actionscript']:
        return "An error occurred, invalid language for awesomeness", 500
    return jsonify(
        language=language,
        features=random.sample(features, size)
    )
