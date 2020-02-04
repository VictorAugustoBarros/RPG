# -*- coding: utf-8 -*-


class Schema:

    def __init__(self):
        self.header = {
            "name": "authorization",
            "in": "header",
            "required": True,
            "default": "gc4Eew5L4wJloAvTAJoit56mnh0lso23"
        }

        self.company = {
            "name": "uid",
            "in": "path",
            "type": "integer"
        }

    def company_range_limit(self, product):
        start_date = {
            "name": "start_date",
            "type": "string",
            "in": "path",
            "pattern": r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}"
        }
        end_date = {
            "name": "end_date",
            "type": "string",
            "in": "path",
            "pattern": r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}"
        }

        s = {
            "tags": ["Company", product],
            "required": ["start_date", "end_date", "company"],
            "parameters": [self.header, start_date, end_date, self.company],
            "responses": {
                "200": {
                    'description': '',
                },
                "404": {
                    'description': ''
                }
            }
        }

        return s
