# -*- coding: utf-8 -*-

import yaml


class Config:

    __monostate = None
    conf = None

    def __init__(self):
        if not Config.__monostate:
            Config.__monostate = self.__dict__
            try:
                self.conf = yaml.load(open("/app/config/config.yml"),  Loader=yaml.FullLoader)
            except:
                self.conf = yaml.load(open("config/config.yml"),  Loader=yaml.FullLoader)

        else:
            self.__dict__ = Config.__monostate

    def mysql(self, product):
        return self.conf["mysql"][product]

    def mongodb(self):
        return self.conf["mongodb"]

    def auth(self):
        return self.conf["auth"]
