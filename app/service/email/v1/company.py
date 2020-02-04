from datetime import datetime
from flask import jsonify
from utils.custom_exceptions import ExceptionHandler
from utils.custom_exceptions import InvalidDateFormatException
from controller.email.empresa_controller import EmpresaController


class Company:

    @staticmethod
    def get_time_range_limit(company, start_date, end_date):
        """
        Retorna se é possível ou não criar uma campanha dentro das datas informadas
        :param company: Id da empresa
        :param start_date: Data inicio da campanha
        :param end_date: Data fim da campanha
        :return: dict
        """

        try:
            # Valida formato da data
            try:
                s_date = datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S')
                e_date = datetime.strptime(end_date, '%Y-%m-%d %H:%M:%S')

            except ValueError:
                raise InvalidDateFormatException(({"msg": "Invalid date format, should be Y-m-d H:M:S", "code": 400}))

            week = (s_date.weekday() + 1) % 7  # Transforma dia da semana para ser (0 Domingo - 6 Sabado)

            limit = EmpresaController.get_time_range_limit(company, start_date, week)

            valid = e_date < limit

            return {"valid": valid,
                    "start_date": start_date,
                    "end_date": end_date,
                    "limit_date": limit.strftime('%Y-%m-%d %H:%M:%S')}

        except Exception as e:
            return ExceptionHandler.handler(e)

    @staticmethod
    def get_company_range_limit_config(company):
        """
        Retorna todas as configurações de limites da empresa
        :param company: Id da empresa
        :return: dict
        """

        try:

            return jsonify(EmpresaController.get_range_limit_config(company))

        except Exception as e:
            return ExceptionHandler.handler(e)

    @staticmethod
    def set_company_range_limit(company, limits):
        """
        Insere ou atualiza informações de limite de criação das campanhas
        :param company: Id da empresa
        :param limits: lista de dias da semana + quantidade de horas limite
        :return: dict
        """

        try:

            EmpresaController.get_company_by_id(company)  # Validando se empresa é pai e valida

            for l in limits:
                EmpresaController.set_range_limit_config(company, l["week"], l["limit"])

            return jsonify(EmpresaController.get_range_limit_config(company))
        except Exception as e:
            return ExceptionHandler.handler(e)

    @staticmethod
    def delete_company_range_limit(company, week=None):

        EmpresaController.delete_range_limit(company, week)

        return jsonify({"success": True})
