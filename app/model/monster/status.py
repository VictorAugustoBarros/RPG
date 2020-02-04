class StatusMonster:
    def __init__(self, id_monster):
        self.id_monster = id_monster
        self.basic_status = ''
        self.status = ''

    def get_basic_data(self):
        self.basic_status = {
            "Nome": "Maou",
            "Idade": 2000,
            "Classe": "Demon Lord"
        }

    def get_status(self):
        self.status = {
            "Vida": 200,
            "Ataque": 10,
            "Defesa": 15,
            "Ataque Mágico": 2,
            "Skills": {
                "Dark Spear": {
                    "Dano": 7,
                    "Penetração Armadura": 30,
                    "Penetração Mágica": 30
                }
            }
        }
