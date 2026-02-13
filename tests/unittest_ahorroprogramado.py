import unittest
import sys
from pathlib import Path

# Agregar el directorio src al path de Python
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.core.ahorro import AhorroProgramado
 

class TestAhorroProgramado(unittest.TestCase):
    def test_caso_normal(self):
        ahorro = AhorroProgramado(1100000, 6, 0)
        self.assertEqual(ahorro.calcular_ahorro(), 183333.33)

    def test_caso_normal_dos(self):
        ahorro = AhorroProgramado(9000000, 12, 0)
        self.assertEqual(ahorro.calcular_ahorro(), 750000)

    def test_calcular_tiempo_ahorro(self):
        # Aquí puedes agregar pruebas para la función calcular_tiempo_ahorro
        pass

if __name__ == '__main__':  
    unittest.main()