import unittest
import sys
from src.controller.usuario_controller import UsuarioController
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.model.usuario import Usuario
from src.controller.usuario_controller import UsuarioController
from src.model.ahorro import Ahorro, AhorroProgramado
from src.model.meta_ahorro import MetaAhorro
from src.controller.ahorro_controller import AhorroController


class TestUsuario(unittest.TestCase):

    def test_insertar_y_buscar(self):
        UsuarioController.eliminar(100)

        usuario_prueba = Usuario(
            id_usuario=100,
            nombre="Luisa Espinal",
            email="luisa@email.com"
        )

        UsuarioController.insertar(usuario_prueba)

        usuario_buscado = UsuarioController.buscar(100)

        self.assertEqual(usuario_prueba, usuario_buscado)

    def test_insertar_y_buscar_con_acentos(self):
        UsuarioController.eliminar(200)

        usuario_prueba = Usuario(
            id_usuario=200,
            nombre="José Jaramillo",
            email="jose@email.com"
        )

        UsuarioController.insertar(usuario_prueba)

        usuario_buscado = UsuarioController.buscar(200)

        self.assertEqual(usuario_prueba, usuario_buscado)

    def test_insertar_y_buscar_nombre_largo(self):
        UsuarioController.eliminar(300)

        usuario_prueba = Usuario(
            id_usuario=300,
            nombre="Usuario con nombre extremadamente largo para pruebas",
            email="largonombre@email.com"
        )

        UsuarioController.insertar(usuario_prueba)

        usuario_buscado = UsuarioController.buscar(300)

        self.assertEqual(usuario_prueba, usuario_buscado)


class TestMetasAhorro(unittest.TestCase):

    def test_crear_y_buscar_meta_sin_extra(self):
        """Test para crear y buscar meta sin aporte extra en la BD"""
        id_usuario = UsuarioController.obtener_siguiente_id()

        usuario_prueba = Usuario(
            id_usuario=id_usuario,
            nombre="Usuario Test Meta 1",
            email=f"test.meta1.{id_usuario}@email.com"
        )
        UsuarioController.insertar(usuario_prueba)
        
        ahorro = Ahorro(meta=1000000, plazo=10, extra=0, mes_extra=0)
        AhorroController.calcular_y_guardar(id_usuario, ahorro)
        
        metas = AhorroController.buscar_metas_por_usuario(id_usuario)
        
        self.assertGreater(len(metas), 0)
        meta_buscada = metas[0]
        self.assertEqual(meta_buscada.meta, 1000000)
        self.assertEqual(meta_buscada.plazo, 10)
        
        AhorroController.eliminar_metas_por_usuario(id_usuario)
        UsuarioController.eliminar(id_usuario)

        """Test para crear y buscar meta con aporte extra en la BD""" 
           
    def test_crear_y_buscar_meta_con_extra(self):

        id_usuario = UsuarioController.obtener_siguiente_id()

        usuario_prueba = Usuario(
            id_usuario=id_usuario,
            nombre="Usuario Test Meta 2",
            email=f"test.meta2.{id_usuario}@email.com"
        )
        UsuarioController.insertar(usuario_prueba)
        
        ahorro = Ahorro(meta=1000000, plazo=10, extra=100000, mes_extra=5)
        AhorroController.calcular_y_guardar(id_usuario, ahorro)
        
        ahorro_sin_extra = Ahorro(meta=1000000, plazo=10, extra=0, mes_extra=0)
        cuota_con_extra = AhorroProgramado().calcular_ahorro(ahorro)
        cuota_sin_extra = AhorroProgramado().calcular_ahorro(ahorro_sin_extra)
        
        self.assertLess(cuota_con_extra, cuota_sin_extra)
        


if __name__ == '__main__':
    unittest.main()
