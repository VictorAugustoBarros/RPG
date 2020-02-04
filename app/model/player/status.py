from controller.player.playerController import PlayerController

class StatusPlayer:
    def __init__(self, id_player):
        self.id_player = id_player
        self.basic_status = ''
        self.status = ''

    def get_basic_data(self):
        self.basic_status = {
            "Nome": "Kirito",
            "Idade": 22,
            "Classe": "Espadachim"
        }

    def get_status(self):
        # PlayerController.get_staus_by_id(self.id_player)

        self.status = {
            "Vida": 100,
            "Ataque": 10,
            "Defesa": 15,
            "Ataque Mágico": 2,
            "Skills": {
                "Fireball": {
                    "Dano": 7,
                    "Penetração Armadura": 10,
                    "Penetração Mágica": 10
                }
            }
        }
