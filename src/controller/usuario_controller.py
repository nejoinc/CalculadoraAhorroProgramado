import psycopg2

from src.db import get_connection, create_tables, drop_tables
from src.model.usuario import Usuario


class UsuarioController:

    def insertar(usuario: Usuario):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO usuarios (id_usuario, nombre, email) VALUES (%s, %s, %s)",
            (usuario.id_usuario, usuario.nombre, usuario.email)
        )
        connection.commit()
        connection.close()

    def buscar(id_usuario: int) -> Usuario | None:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "SELECT id_usuario, nombre, email FROM usuarios WHERE id_usuario = %s",
            (id_usuario,)
        )
        row = cursor.fetchone()
        connection.close()
        if row is None:
            return None
        return Usuario(id_usuario=row[0], nombre=row[1], email=row[2])

    def crear_tablas():
        create_tables()

    def borrar_tablas():
        drop_tables()

    def eliminar(id_usuario: int):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "DELETE FROM usuarios WHERE id_usuario = %s",
            (id_usuario,)
        )
        connection.commit()
        connection.close()
