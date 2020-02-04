# -*- coding: utf-8 -*-

from utils.model import Model


class Empresa(Model):

    def __init__(self, mysql_data=None):
        super(Empresa, self).__init__("EMPRESA_MAIL", "ID_EMPRESA_EPML", "EMAIL")

        if mysql_data:
            self.set_attributes(mysql_data)
