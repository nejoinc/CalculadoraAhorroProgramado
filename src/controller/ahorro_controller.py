import psycopg2

from src.db import get_connection
from src.model.ahorro import Ahorro, AhorroProgramado
from src.model.meta_ahorro import MetaAhorro
from src.model.historial_calculo import HistorialCalculo


class AhorroController:

    def calcular_y_guardar(id_usuario: int, ahorro: Ahorro):
        cuota = AhorroProgramado().calcular_ahorro(ahorro)

        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(
            """INSERT INTO metas_ahorro
               (id_usuario, meta, plazo, extra, mes_extra, cuota_mensual)
               VALUES (%s, %s, %s, %s, %s, %s)""",
            (id_usuario, ahorro.meta, ahorro.plazo,
             ahorro.extra, ahorro.mes_extra, cuota)
        )
        connection.commit()
        connection.close()

    def buscar_meta(id_meta: int) -> MetaAhorro | None:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "SELECT id_meta, id_usuario, meta, plazo, extra, mes_extra FROM metas_ahorro WHERE id_meta = %s",
            (id_meta,)
        )
        row = cursor.fetchone()
        connection.close()
        if row is None:
            return None
        return MetaAhorro(
            id_meta=row[0], id_usuario=row[1], meta=row[2],
            plazo=row[3], extra=row[4], mes_extra=row[5]
        )

    def buscar_historial(id_historial: int) -> HistorialCalculo | None:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "SELECT id_historial, id_usuario, meta, plazo, extra, mes_extra, cuota_mensual FROM historial_calculos WHERE id_historial = %s",
            (id_historial,)
        )
        row = cursor.fetchone()
        connection.close()
        if row is None:
            return None
        return HistorialCalculo(
            id_historial=row[0], id_usuario=row[1], meta=row[2],
            plazo=row[3], extra=row[4], mes_extra=row[5],
            cuota_mensual=row[6]
        )
