import unittest
import sys
from pathlib import Path

# Permite importar desde la carpeta raíz del proyecto
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.model.ahorro import *

class TestAhorroProgramado(unittest.TestCase):
    # CASOS NORMALES
    def test_caso_normal_uno(self):
        ahorro = Ahorro(meta=1100000, plazo=6, extra=0, mes_extra=1)
        ahorroprogramado = AhorroProgramado()
        self.assertEqual(ahorroprogramado.calcular_ahorro(ahorro), 179925.80)

    def test_caso_normal_dos(self):
        ahorro = Ahorro(meta=9000000, plazo=12, extra=1000000, mes_extra=6)
        ahorroprogramado = AhorroProgramado()
        self.assertEqual(ahorroprogramado.calcular_ahorro(ahorro), 635945.86)

    def test_caso_normal_tres(self):
        ahorro = Ahorro(meta=170000000, plazo=36, extra=0, mes_extra=1)
        ahorroprogramado = AhorroProgramado()
        self.assertEqual(ahorroprogramado.calcular_ahorro(ahorro), 4130954.55)

    #CASOS EXTRAORDINARIOS
    def test_ahorro_cero(self):
        ahorro = Ahorro(meta=0, plazo=1, extra=0, mes_extra=1)
        ahorroprogramado = AhorroProgramado()
        self.assertEqual(ahorroprogramado.calcular_ahorro(ahorro), 0)


    def test_ahorro_unico(self):
        ahorro = Ahorro(meta=90000, plazo=1, extra=0, mes_extra=1)
        ahorroprogramado = AhorroProgramado()
        self.assertEqual(ahorroprogramado.calcular_ahorro(ahorro), 90000)

    def test_extra_igual_a_ahorro(self):
        ahorro = Ahorro(meta=400000, plazo=2, extra=400000, mes_extra=1)
        ahorroprogramado = AhorroProgramado()
        self.assertEqual(ahorroprogramado.calcular_ahorro(ahorro), 0)


    # CASOS DE ERROR
    def test_ahorro_negativo(self):
        with self.assertRaises(ErrorMetaMayorACero):
            ahorro = Ahorro(meta=-1300000, plazo=15, extra=0, mes_extra=1)
            ahorroprogramado = AhorroProgramado()
            ahorroprogramado.calcular_ahorro(ahorro)

    def test_plazo_cero(self):
        with self.assertRaises(ErrorPlazoMayorACero):
            ahorro = Ahorro(meta=5000, plazo=0, extra=0, mes_extra=1)
            ahorroprogramado = AhorroProgramado()
            ahorroprogramado.calcular_ahorro(ahorro)

    def test_abono_superior(self):
        with self.assertRaises(ErrorAbonoSuperaMeta):
            ahorro = Ahorro(meta=400000, plazo=2, extra=800000, mes_extra=1)
            ahorroprogramado = AhorroProgramado()
            ahorroprogramado.calcular_ahorro(ahorro)

    def test_mes_extra_superior(self):
        with self.assertRaises(ErrorMesExtraFueraDelRango):
            ahorro = Ahorro(meta=200000, plazo=3, extra=20000, mes_extra=5)
            ahorroprogramado = AhorroProgramado()
            ahorroprogramado.calcular_ahorro(ahorro)
    
    def test_abono_negativo(self):
        with self.assertRaises(ErrorAbonoExtraMenorAcero):
            ahorro = Ahorro(meta=200000, plazo=3, extra=-200000, mes_extra=1)
            ahorroprogramado = AhorroProgramado()
            ahorroprogramado.calcular_ahorro(ahorro)

    
if __name__ == '__main__':
    unittest.main()