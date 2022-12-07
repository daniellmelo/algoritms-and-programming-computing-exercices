# Distância entre Pontos
# Elabore uma função chamada distancia() que tem como parâmetros as coordenadas x1, y1, x2, y2, representando dois pontos no plano cartesiano. A função deve retornar a distância entre esses dois pontos como um número de ponto flutuante.
#
#
# A Entrada consiste de:
# Não há entrada para essa questão, só é necessário definir a função distancia() com parâmetros x1, y1, x2 e y2.
#
# A Saída deve apresentar:
# Não há saída para essa questão, só é necessário que a função retorne a distância entre os dois pontos.
#
# Observações:
# É garantido que os parâmetros serão sempre números inteiros, positivos, no intervalo [0;20]
# Uma forma de realizar a operação de radiciação em Python é utilizar o operador de potenciação ** com índice fracionário, como por exemplo 1/2 para a raiz quadrada.
#
# Descrição dos Exemplos:
# No primeiro exemplo, os pontos dados são (2,0) e (2,0). Considerando a fórmula para a distância entre dois pontos: Distância = ((2 - 2)² + (0 - 0)²)^1/2 = 0.0
# No segundo exemplo, os pontos dados são (0,0) e (10,10). Considerando a fórmula para a distância entre dois pontos: Distância = ((10 - 0)² + (10 - 0)²)^1/2 = 14.142135623730951
# No terceiro exemplo, os pontos dados são (1,5) e (1,10). Considerando a fórmula para a distância entre dois pontos: Distância = ((1 - 1)² + (10 - 5)²)^1/2 = 5.0

from math import sqrt
def distancia(x1, y1, x2, y2):
    res = sqrt((x1-x2)**2 + (y1 - y2)**2)
    return res