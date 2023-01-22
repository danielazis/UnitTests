
def calcular_area_cubo(lado):
    if lado >= 0:
        return lado**3
    else:
        return 'Valores invalidos'


def calcular_area_paralelo(base, altura):
    try:
        if base >= 0 and altura >= 0:
            return base*altura
        else:
            return 'Valores invalidos'
    except TypeError:
        return 'Entrada invalida'


def calcular_area_piramide(base, altura):
    try:
        if base >= 0 and altura >= 0:
            return (base**2)+(((altura**2 + (base/2)**2)**0.5)*base/2)*4
        else:
            return 'Valores invalidos'
    except TypeError:
        return 'Entrada invalida'


if __name__ == '__main__':
    print(f'A area do cubo: {calcular_area_cubo(3)}')
    print(f'A area do paralelogramo: {calcular_area_paralelo(3, 9)}')
    print(f'A area da piramide retangular: {calcular_area_piramide(100, 50)}')
