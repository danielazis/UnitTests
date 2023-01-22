import unittest

import main


class TesteAreaCubo(unittest.TestCase):

    def teste_calcular_area_positivo(self):
        lado = 3
        resultado_esperado = 27
        resultado_obtido = main.calcular_area_cubo(lado)

        self.assertEqual(resultado_esperado, resultado_obtido)

    def teste_calcular_area_negativo(self):
        lado = -3
        resultado_esperado = 'Valores invalidos'
        resultado_obtido = main.calcular_area_cubo(lado)
        self.assertEqual(resultado_esperado, resultado_obtido)
