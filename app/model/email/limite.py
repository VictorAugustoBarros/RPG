# -*- coding: utf-8 -*-

from utils.model import Model


class Limite(Model):

    def __init__(self, mysql_data=None):
        super(Limite, self).__init__("LIMITE_FINALIZACAO_CAMPANHA_MAIL", "ID_LIMITE_FINALIZACAO_CAMPANHA_LFCML", "EMAIL")

        if mysql_data:
            self.set_attributes(mysql_data)

    def pretify(self):

        return {
                "company": self.id_empresa_lfcml,
                "week": self.id_semana_lfcml,
                "limit": self.qt_hora_limite_lfcml
               }
