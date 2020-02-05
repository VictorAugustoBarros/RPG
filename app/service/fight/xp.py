import copy
from flask import jsonify


class Xp:
    def __init__(self, id_player, id_monster):
        self.player = id_player
        self.monster = id_monster

    def gain_xp_monster(self):
        try:
            lvl_player = 1
            xp = 1000
            xp_next = 2000
            xp_porcent = str((xp * 100) / xp_next) + "%"

            return jsonify(
                {"Level": lvl_player, "XP": xp, "XP Next Level": xp_next, "%": xp_porcent})

        except Exception as err:
            return jsonify({"Error": err})
