import pytest

import main

lista_area_paralelo = [
    (10, 50, 500),
    (7, -5, 'Valores invalidos'),
    ('a', 4, 'Entrada invalida')
]


@pytest.mark.parametrize('base, altura, resultado_esperado', lista_area_paralelo)
def teste_calcular_area_paralelo(base, altura, resultado_esperado):

    resultado_obtido = main.calcular_area_paralelo(base, altura)

    assert resultado_obtido == resultado_esperado
