# -*- coding: utf-8 -*-

import re
import time
import MySQLdb
import MySQLdb.cursors
from config.config import Config
from utils.logger import Logger


class Database:

    def __init__(self, product):
        self.product = product
        self.config = Config().mysql(product.lower())
        self.cursor = None
        self.db = None
        self.open()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.close()

    def open(self):

        retry = 0

        while retry <= 3:

            try:
                self.db = MySQLdb.connect(self.config["host"],
                                          self.config["user"],
                                          self.config["pwd"],
                                          self.config["schema"],
                                          port=self.config["port"],
                                          cursorclass=MySQLdb.cursors.DictCursor,
                                          charset="utf8",
                                          connect_timeout=60,
                                          use_unicode=True)
                break

            except MySQLdb.OperationalError as e:
                retry += 1
                time.sleep(1)

    def close(self):
        self.db.close()

    def commit(self):
        if self.db.open:
            self.db.commit()
            # self.close()

    def rollback(self):
        if self.db.open:
            self.db.rollback()
            self.close()

    def last_id(self):
        return self.db.insert_id()

    def execute(self, query, args=tuple(), debug=False):

        if debug:
            Logger().debug({"query": re.sub(' +', ' ', query.replace("\n", "")), "args": args})

        retry = 0

        while retry <= 2:
            try:
                self.cursor = self.db.cursor()
                self.cursor.execute(query, args)
                return self.cursor
            except MySQLdb.OperationalError as e:
                retry += 1
                self.open()

    def get_attributes_from_database(self, table_name):

        query = "SHOW FULL COLUMNS FROM %s" % table_name

        cursor = self.execute(query)

        attributes = []
        for row in cursor.fetchall():
            attributes.append(row["Field"])

        cursor.close
        return attributes


