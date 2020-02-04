# -*- coding: utf-8 -*-
from utils.database import Database
from utils.custom_exceptions import InvalidCompanyIdException


class PlayerController:

    @staticmethod
    def get_staus_by_id(id_player):
        """
        Retorna objeto Empresa do ID informado
        :param id_player: Id do Jogador
        :return: Status jogador
        """

        with Database("email") as db:
            query = "SELECT * FROM EMPRESA_MAIL WHERE ID_EMPRESA_EPML = %s AND ID_EMPRESA_PAI_EPML = 1"

            result = db.execute(query, (id_player,))

            if result.rowcount <= 0:
                raise InvalidCompanyIdException({"msg": "Invalid player ID.", "code": 400})

            return result.fetchone()
