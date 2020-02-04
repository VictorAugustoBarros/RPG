import copy
from flask import jsonify


class Fight:
    def __init__(self, status_player, status_monster):
        self.player = status_player
        self.monster = status_monster

    def player_attack(self):
        try:
            status_old = self.monster.status

            status_new = copy.deepcopy(self.monster.status)
            status_new["Vida"] = status_new["Vida"] - self.player.status["Ataque"]

            return jsonify(
                {"Player": self.player.status, "Monster": status_old, "Monster After Damage": status_new})

        except Exception as err:
            return jsonify({"Error": err})
