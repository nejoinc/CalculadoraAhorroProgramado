import psycopg2

from secret_config import DB_CONFIG
from src.model.ahorro import Ahorro, AhorroProgramado
from src.model.meta_ahorro import MetaAhorro
from src.model.historial_calculo import HistorialCalculo


class AhorroController:

    def obtener_cursor():
        connection = psycopg2.connect(**DB_CONFIG)
        return connection.cursor()

    def crear_tabla():
        for nombre_sql in ("sql/02_metas_ahorro.sql", "sql/03_historial_calculos.sql"):
            cursor = AhorroController.obtener_cursor()
            with open(nombre_sql, "r", encoding="utf-8") as archivo:
                consulta = archivo.read()

            cursor.execute(consulta)
            cursor.connection.commit()
            cursor.connection.close()

    def calcular_y_guardar(id_usuario: int, ahorro: Ahorro):
        cuota = AhorroProgramado().calcular_ahorro(ahorro)
        cursor = AhorroController.obtener_cursor()
        cursor.execute(
            """INSERT INTO metas_ahorro
               (id_usuario, meta, plazo, extra, mes_extra, cuota_mensual)
               VALUES (%s, %s, %s, %s, %s, %s)""",
            (id_usuario, ahorro.meta, ahorro.plazo,
             ahorro.extra, ahorro.mes_extra, cuota)
        )
        cursor.connection.commit()
        cursor.connection.close()

    def buscar_meta(id_meta: int) -> MetaAhorro | None:
        cursor = AhorroController.obtener_cursor()
        cursor.execute(
            "SELECT id_meta, id_usuario, meta, plazo, extra, mes_extra, cuota_mensual FROM metas_ahorro WHERE id_meta = %s",
            (id_meta,)
        )
        row = cursor.fetchone()
        cursor.connection.close()
        if row is None:
            return None
        return MetaAhorro(
            id_meta=row[0], 
            id_usuario=row[1], 
            meta=row[2],
            plazo=row[3], 
            extra=row[4], 
            mes_extra=row[5], 
            cuota_mensual=row[6]
        )

    def buscar_metas_por_usuario(id_usuario: int) -> list[MetaAhorro]:
        cursor = AhorroController.obtener_cursor()
        cursor.execute(
            "SELECT id_meta, id_usuario, meta, plazo, extra, mes_extra FROM metas_ahorro WHERE id_usuario = %s",
            (id_usuario,)
        )
        rows = cursor.fetchall()
        cursor.connection.close()

        metas = []
        for row in rows:
            metas.append(MetaAhorro(
                id_meta=row[0], id_usuario=row[1], meta=row[2],
                plazo=row[3], extra=row[4], mes_extra=row[5]
            ))
        return metas

    def eliminar_metas_por_usuario(id_usuario: int):
        cursor = AhorroController.obtener_cursor()
        cursor.execute(
            "DELETE FROM metas_ahorro WHERE id_usuario = %s",
            (id_usuario,)
        )
        cursor.connection.commit()
        cursor.connection.close()

    def buscar_historial(id_historial: int) -> HistorialCalculo | None:
        cursor = AhorroController.obtener_cursor()
        cursor.execute(
            "SELECT id_historial, id_usuario, meta, plazo, extra, mes_extra, cuota_mensual FROM historial_calculos WHERE id_historial = %s",
            (id_historial,)
        )
        row = cursor.fetchone()
        cursor.connection.close()
        if row is None:
            return None
        return HistorialCalculo(
            id_historial=row[0], id_usuario=row[1], meta=row[2],
            plazo=row[3], extra=row[4], mes_extra=row[5],
            cuota_mensual=row[6]
        )
