import pytest

import csv

import main


def ler_dados_csv():
    # Retorna uma lista de dados a partir do arquivo CSV
    nome_arquivo = '../../vendors/lista_piramide.csv'
    dados_csv = []
    try:
        with open(nome_arquivo) as arquivo_csv:
            campos = csv.reader(arquivo_csv, quoting=csv.QUOTE_NONNUMERIC)
            next(campos)
            for linha in campos:
                dados_csv.append(linha)

        return dados_csv
    except FileNotFoundError:
        print(f'Arquivo não encontrado: {nome_arquivo}')
    except Exception as fail:
        print(f'Falha não prevista: {fail}')


@pytest.mark.parametrize('base, altura, resultado_esperado', ler_dados_csv())
def teste_calcular_area_piramide(base, altura, resultado_esperado):
    resultado_obtido = main.calcular_area_piramide(base, altura)
    assert resultado_obtido == resultado_esperado
