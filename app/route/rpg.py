import random
from flask import Flask
from flask import Blueprint
from utils.schema import Schema
from flasgger.utils import swag_from

from model.player.status import StatusPlayer
from model.monster.status import StatusMonster

from service.fight.batalha import Fight
from service.fight.xp import Xp

base_url = ""
application = Flask(__name__)
rpg_blueprint = Blueprint("sms", __name__, url_prefix=base_url)
schema = Schema()


@rpg_blueprint.route('/status/', methods=['GET'])
@swag_from('details/status.yml')
def index():
    return {"success": True}


@rpg_blueprint.route('/player_attack/<id_player>/<id_monster>/', methods=['GET'])
@swag_from('details/player_attack.yml')
def player_attack(id_player, id_monster):
    status_player = StatusPlayer(id_player)
    status_player.get_status()
    status_player.get_basic_data()

    status_monster = StatusMonster(id_monster)
    status_monster.get_status()
    status_monster.get_basic_data()

    batalha = Fight(status_player, status_monster)

    return batalha.player_attack()


@rpg_blueprint.route('/gain_xp_monster/<id_player>/<id_monster>/', methods=['GET'])
@swag_from('details/gain_xp_monster.yml')
def gain_xp_monster(id_player, id_monster):
    xp = Xp(id_player, id_monster)

    return xp.gain_xp_monster()
