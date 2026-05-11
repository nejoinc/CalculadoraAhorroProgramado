import psycopg2

from model.usuario import Usuario


class UsuarioController:

    def insertar(usuario: Usuario):
        connection = psycopg2.connect(
            host="",
            database="",
            user="",
            password="",
            port="5432"
        )
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO usuarios (id_usuario, nombre, email) VALUES (%s, %s, %s)",
            (usuario.id_usuario, usuario.nombre, usuario.email)
        )
        connection.commit()
        connection.close()

    def buscar(id_usuario: int) -> Usuario | None:
        connection = psycopg2.connect(
            host="",
            database="",
            user="",
            password="",
            port="5432"
        )
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
