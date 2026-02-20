import unittest
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from core.ahorro import AhorroProgramado
 

class TestAhorroProgramado(unittest.TestCase):
    def test_caso_normal(self):
        ahorro = AhorroProgramado(meta=1100000, plazo=6, extra=0, mes_extra=1)
        self.assertEqual(ahorro.calcular_ahorro(), 179925.80) 

    def test_caso_normal_dos(self):
        ahorro = AhorroProgramado(meta=9000000, plazo=12, extra=0, mes_extra=1)
        self.assertEqual(ahorro.calcular_ahorro(), 719563.29)

    def test_caso_normal_tres(self):
        ahorro = AhorroProgramado(meta=170000000, plazo=36, extra=0, mes_extra=1)
        self.assertEqual(ahorro.calcular_ahorro(), 4130954.55)


    ### CASOS EXTRAORDNARIOS

    def test_ahorro_cero(self):
        ahorro = AhorroProgramado(meta=0, plazo=1, extra=0, mes_extra=1)
        self.assertEqual(ahorro.calcular_ahorro(), 0)

    def test_ahorro_unico(self):
        ahorro = AhorroProgramado(meta=90000, plazo=1, extra=0, mes_extra=1)
        self.assertEqual(ahorro.calcular_ahorro(), 90000)

    def test_ahorro_unico(self):
        ahorro = AhorroProgramado(meta=400000, plazo=2, extra=400000, mes_extra=1)
        self.assertEqual(ahorro.calcular_ahorro(), 0)


    #CASOS DE ERROR.


    def valor_a_ahorrar_mayor_que_cero(self):
        ahorro = AhorroProgramado(meta=-1300000, plazo=15, extra=0, mes_extra=1)
        self.assertAlmostEqual(ahorro.calcular_ahorro(), "Error: el valor a ahorrar debe ser mayor a 0")

    def test_plazo_cero_o_menor(self):
        ahorro = AhorroProgramado(meta=5000, plazo=0, extra=0, mes_extra=1)
        self.assertEqual(ahorro.calcular_ahorro(), "Error: el plazo debe ser mayor a 0")

    def test_abono_superior(self): 
        ahorro = AhorroProgramado(meta=400000, plazo=2, extra=800000, mes_extra=1)
        self.assertEqual(ahorro.calcular_ahorro(), "Error: abono supera meta de ahorro")

    def test_mes_extra_mayor_que_plazo(self):
        ahorro = AhorroProgramado(meta=200000, plazo=3, extra=20000, mes_extra=4)
        self.assertEqual(ahorro.calcular_ahorro(), "Error")


if __name__ == '__main__':  
    unittest.main()