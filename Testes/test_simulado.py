import unittest
from simulado import CalculadoraAbstrata, CalculadoraConsole

class TestSimulado(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.calculadora_teste = CalculadoraConsole()
    def test_2_mais_2_retorna_4(self):
        self.assertEqual(4, self.calculadora_teste.parser('2 mais 2'))
    def test_2_menos_4_retorna_2_negativo(self):
        self.assertEqual(-2, self.calculadora_teste.parser('2 menos 4'))
    def test_4_vezes_7_retorna_28(self):
        self.assertEqual(28, self.calculadora_teste.parser('4 vezes 7'))
    def test_26_dividido_3_retorna_8_ponto_67(self):
        self.assertAlmostEqual(8.67, self.calculadora_teste.parser('26 dividido por 3'), 2)
    def test_7_elevado_3_retorna_343(self):
        self.assertEqual(343, self.calculadora_teste.parser('7 elevado a 3'))


if __name__ == '__main__':

    unittest.main(verbosity=2)