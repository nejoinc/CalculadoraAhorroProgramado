import psycopg2
from secret_config import DB_CONFIG


def get_connection():
    return psycopg2.connect(
        host=DB_CONFIG["host"],
        database=DB_CONFIG["database"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
        port=DB_CONFIG["port"],
    )


def create_tables():
    sql = """
    CREATE TABLE IF NOT EXISTS usuarios (
        id_usuario SERIAL PRIMARY KEY,
        nombre VARCHAR(100),
        email VARCHAR(150) UNIQUE,
        fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS metas_ahorro (
        id_meta SERIAL PRIMARY KEY,
        id_usuario INT REFERENCES usuarios(id_usuario),
        meta DECIMAL(18,2),
        plazo INT,
        extra DECIMAL(18,2) DEFAULT 0,
        mes_extra INT DEFAULT 0,
        tasa DECIMAL(6,4) DEFAULT 0.0075,
        cuota_mensual DECIMAL(18,2),
        fecha_calculo TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS historial_calculos (
        id_historial SERIAL PRIMARY KEY,
        id_usuario INT REFERENCES usuarios(id_usuario),
        meta DECIMAL(18,2),
        plazo INT,
        extra DECIMAL(18,2) DEFAULT 0,
        mes_extra INT DEFAULT 0,
        tasa DECIMAL(6,4) DEFAULT 0.0075,
        valor_futuro_extra DECIMAL(18,2),
        factor_anualidad DECIMAL(18,6),
        cuota_mensual DECIMAL(18,2),
        fecha_calculo TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    connection.close()


def drop_tables():
    sql = """
    DROP TABLE IF EXISTS historial_calculos;
    DROP TABLE IF EXISTS metas_ahorro;
    DROP TABLE IF EXISTS usuarios;
    """
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    connection.close()
