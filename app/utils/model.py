
from utils.class_attr import ClassAttr


class Model:

    def __init__(self, table_name, primary_key, product):

        self.table_name = table_name
        self.primary_key = primary_key
        self.product = product.upper()

        for attribute in ClassAttr().dict_attr[self.product][self.table_name]:
            setattr(self, ClassAttr().dict_attr[self.product][self.table_name][attribute], None)

    def set_attributes(self, mysql_data):

        for attribute in ClassAttr().dict_attr[self.product][self.table_name]:
            try:
                setattr(self, ClassAttr().dict_attr[self.product][self.table_name][attribute], mysql_data[attribute])
            except:
                try:
                    setattr(self, ClassAttr().dict_attr[self.product][self.table_name][attribute], mysql_data[attribute.lower()])
                except:
                    pass
