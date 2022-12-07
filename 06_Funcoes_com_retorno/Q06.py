# Raízes da Equação
# Elabore uma função raizes() que recebe como parâmetros os coeficientes a, b e c de uma equação de segundo grau ax²+bx+c e retorna a quantidade de raízes reais e distintas da equação. Em caso de não existirem raízes reais, a função deve retornar -1.
#
#
# A Entrada consiste de:
# Não há entrada para essa questão. A função raizes() recebe três parâmetros: a, b e c que são números inteiros.
#
# A Saída deve apresentar:
# Não há saída para essa questão. A função raizes() deve apenas retornar o número de raízes reais e distintas para a equação ax²+bx+c.
#
# Observações:
# Não é necessário validar se os valores dos parâmetros são do tipo definido.
#
# Descrição dos Exemplos:
# No primeiro exemplo, a = 6, b = 11 e c = -35. Para esses coeficientes, delta assume o valor de 961, portanto há duas raízes reais e distintas para a equação e a função retorna o valor 2.
# No segundo exemplo, a = 2 , b = 4 e c = 2. Para esses coeficientes, delta assume o valor de 0, portanto há duas raízes reais e iguais para a equação, e a função retorna o valor 1.
# No terceiro exemplo, a = -4, b = -7 e c = -12 . Para esses coeficientes, delta assume o valor de -143, portanto não há raízes reais para a equação e a função retorna o valor -1.

from math import sqrt, pow
def raizes(a:int, b:int, c:int) -> int:
    delta = pow(b,2)- 4 * a * c
    if delta == 0:
        return 1
    elif delta < 0:
        return -1
    return 2