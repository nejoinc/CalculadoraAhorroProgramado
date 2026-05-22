import psycopg2

from secret_config import DB_CONFIG
from src.model.usuario import Usuario


class UsuarioController:

    def obtener_cursor():
        connection = psycopg2.connect(**DB_CONFIG)
        return connection.cursor()

    def crear_tabla():
        cursor = UsuarioController.obtener_cursor()
        with open("sql/01_usuarios.sql", "r", encoding="utf-8") as archivo:
            consulta = archivo.read()

        cursor.execute(consulta)
        cursor.connection.commit()
        cursor.connection.close()

    def insertar(usuario: Usuario):
        cursor = UsuarioController.obtener_cursor()
        cursor.execute(
            "INSERT INTO usuarios (id_usuario, nombre, email) VALUES (%s, %s, %s)",
            (usuario.id_usuario, usuario.nombre, usuario.email)
        )
        cursor.connection.commit()
        cursor.connection.close()

    def obtener_siguiente_id():
        cursor = UsuarioController.obtener_cursor()
        cursor.execute("SELECT MAX(id_usuario) FROM usuarios")
        row = cursor.fetchone()
        cursor.connection.close()
        if row is None or row[0] is None:
            return 1
        return row[0] + 1

    def buscar(id_usuario: int) -> Usuario | None:
        cursor = UsuarioController.obtener_cursor()
        cursor.execute(
            "SELECT id_usuario, nombre, email FROM usuarios WHERE id_usuario = %s",
            (id_usuario,)
        )
        row = cursor.fetchone()
        cursor.connection.close()
        if row is None:
            return None
        return Usuario(id_usuario=row[0], nombre=row[1], email=row[2])

    def eliminar(id_usuario: int):
        cursor = UsuarioController.obtener_cursor()
        cursor.execute(
            "DELETE FROM usuarios WHERE id_usuario = %s",
            (id_usuario,)
        )
        cursor.connection.commit()
        cursor.connection.close()
