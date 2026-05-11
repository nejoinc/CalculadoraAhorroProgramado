import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.model.usuario import Usuario
from src.controller.usuario_controller import UsuarioController


class TestUsuario(unittest.TestCase):

    def test_insertar_y_buscar(self):
        usuario_prueba = Usuario(
            id_usuario=100,
            nombre="Luisa Espinal",
            email="luisa@email.com"
        )

        UsuarioController.insertar(usuario_prueba)

        usuario_buscado = UsuarioController.buscar(100)

        self.assertEqual(usuario_prueba, usuario_buscado)

    def test_insertar_y_buscar_con_acentos(self):
        usuario_prueba = Usuario(
            id_usuario=200,
            nombre="José Jaramillo",
            email="jose@email.com"
        )

        UsuarioController.insertar(usuario_prueba)

        usuario_buscado = UsuarioController.buscar(200)

        self.assertEqual(usuario_prueba, usuario_buscado)

    def test_insertar_y_buscar_nombre_largo(self):
        usuario_prueba = Usuario(
            id_usuario=300,
            nombre="Usuario con nombre extremadamente largo para pruebas",
            email="largonombre@email.com"
        )

        UsuarioController.insertar(usuario_prueba)

        usuario_buscado = UsuarioController.buscar(300)

        self.assertEqual(usuario_prueba, usuario_buscado)


if __name__ == '__main__':
    unittest.main()
