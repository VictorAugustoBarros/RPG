# -*- coding: utf-8 -*-

from utils.database import Database


class ClassAttr:
    """
    Classe utilizando Borg Pattern, semelhante a um Singleton.
    Armazena todos os atributos necessários para a criação das classes dinamicas.
    """
    __monostate = None

    def __init__(self):
        if not ClassAttr.__monostate:
            self.dict_attr = {
                                "SMS": {"EMPRESA_ESMS": {}, "LIMITE_FINALIZACAO_CAMPANHA_ESMS": {}},
                                "EMAIL": {"EMPRESA_MAIL": {}, "LIMITE_FINALIZACAO_CAMPANHA_MAIL": {}}
                             }

            ClassAttr.__monostate = self.__dict__

            with Database('sms') as query:

                for table in self.dict_attr["SMS"]:

                    attributes = query.get_attributes_from_database(table)

                    for attribute in attributes:
                        self.dict_attr["SMS"][table][attribute] = attribute.lower()

            with Database('email') as query:

                for table in self.dict_attr["EMAIL"]:

                    attributes = query.get_attributes_from_database(table)

                    for attribute in attributes:
                        self.dict_attr["EMAIL"][table][attribute] = attribute.lower()
        else:
            self.__dict__ = ClassAttr.__monostate

