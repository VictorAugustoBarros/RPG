from flask import Flask
from flask import Blueprint
from flask import request
from flasgger.utils import swag_from
from utils.schema import Schema
from utils.request_log import RequestLog
from utils.authorization import Authorization
from service.sms.v1.company import Company

base_url = "/api/v1/sms"
application = Flask(__name__)
rpg_blueprint = Blueprint("sms", __name__, url_prefix=base_url)
schema = Schema()


@rpg_blueprint.route("/company/<uid>/range/limit/<start_date>/<end_date>", methods=["GET"])
@RequestLog.register
@Authorization.auth
@swag_from(schema.company_range_limit("SMS"))
def sms_company_range_limit(uid, start_date, end_date):
    return Company.get_time_range_limit(uid, start_date, end_date)
