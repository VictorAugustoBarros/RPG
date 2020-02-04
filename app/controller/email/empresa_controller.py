# -*- coding: utf-8 -*-
from datetime import datetime
from utils.database import Database
from model.email.limite import Limite
from model.email.empresa import Empresa
from utils.custom_exceptions import NoRangeLimitException
from utils.custom_exceptions import InvalidCompanyIdException


class EmpresaController:

    @staticmethod
    def get_company_by_id(compay):
        """
        Retorna objeto Empresa do ID informado
        :param compay: Id da empresa
        :return: Empresa
        """

        with Database("email") as db:

            query = "SELECT * FROM EMPRESA_MAIL WHERE ID_EMPRESA_EPML = %s AND ID_EMPRESA_PAI_EPML = 1"

            result = db.execute(query, (compay,))

            if result.rowcount <= 0:
                raise InvalidCompanyIdException({"msg": "Invalid company ID.", "code": 400})

            return Empresa(result.fetchone())

    @staticmethod
    def get_time_range_limit(company, date, week):
        """
        :param company: Id da empresa
        :param date: Data de inicio da campanha
        :param week: Dia da semana
        :return: datetime - Horário limite para termino da campanha
        """

        with Database("email") as db:

            query = """ SELECT DATE_ADD(%s, INTERVAL QT_HORA_LIMITE_LFCML HOUR) LIMITE
                        FROM 
                        LIMITE_FINALIZACAO_CAMPANHA_MAIL 
                        WHERE 
                        ID_EMPRESA_LFCML = %s 
                        AND
                        ID_SEMANA_LFCML = %s
                    """

            result = db.execute(query, (date, company, week))

            if result.rowcount <= 0:
                raise NoRangeLimitException({"msg": "No limit configuration found.", "code": 404})

            return datetime.strptime(result.fetchone()["LIMITE"], '%Y-%m-%d %H:%M:%S')

    @staticmethod
    def get_range_limit_config(company):
        """
        :param company: Id da empresa
        :return: array - Todos os limites cadastrados para a empresa
        """

        limits = []

        with Database("email") as db:

            query = """ SELECT
                        *
                        FROM 
                        LIMITE_FINALIZACAO_CAMPANHA_MAIL 
                        WHERE 
                        ID_EMPRESA_LFCML = %s 
                    """

            result = db.execute(query, (company,))

            if result.rowcount <= 0:
                raise NoRangeLimitException({"msg": "No limit configuration found.", "code": 404})

            for r in result.fetchall():
                limite = Limite(r)
                limits.append(limite.pretify())

        return limits

    @staticmethod
    def set_range_limit_config(company, week, limit):
        """
        Insere ou atualiza quantidade de horas limites para a criação de campanhas
        :param company: Id da empresa
        :param week: Dia da semana
        :param limit: Quantidade de hora limite para criar uma campanha
        :return: None
        """

        with Database("email") as db:

            query = """ INSERT INTO 
                        LIMITE_FINALIZACAO_CAMPANHA_MAIL 
                        (ID_EMPRESA_LFCML, ID_SEMANA_LFCML, QT_HORA_LIMITE_LFCML) 
                        VALUES 
                        (%s, %s, %s)
                        ON DUPLICATE KEY UPDATE QT_HORA_LIMITE_LFCML = %s"""

            db.execute(query, (company, week, limit, limit))
            db.commit()

    @staticmethod
    def delete_range_limit(company, week=None):
        """
        Remove configuração de limite, se não for informado o dia da semana, remove toda configuração.
        :param company: Id da empresa
        :param week: Dia da semana (0 - domingo | 6 - Sabado)
        :return: None
        """

        with Database("email") as db:

            where_week = " AND ID_SEMANA_LFCML = " + week if week else ""

            query = "DELETE FROM LIMITE_FINALIZACAO_CAMPANHA_MAIL WHERE ID_EMPRESA_LFCML = %s" + where_week

            db.execute(query, (company,))
            db.commit()
