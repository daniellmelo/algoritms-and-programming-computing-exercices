# O maior entre 3
# Uma característica importante das funções é que elas permitem realizar chamadas a outras funções durante sua execução. Dispondo de uma função chamada max2() que recebe os parâmetros a e b, dois números inteiros e retorna o maior valor entre eles, crie uma nova função max3() que receba os parâmetros a, b e c, três números inteiros e retorne o maior valor entre eles. Lembre-se que o processo para verificar o maior de 3 números pode ser quebrado em verificar o maior de dois números exatamente duas vezes.
#
#
# A Entrada consiste de:
# Não há entrada para esse problema, apenas crie a função max3() com parâmetros a, b e c.
#
# A Saída deve apresentar:
# Não há saída para esse problema, a função deve retornar apenas o maior número dentre os três.
#
# Observações:
# Não é necessário validar se os valores da função são do tipo definido.
# Utilizar-se da função max2() já implementada pode tornar a solução do problema mais simples.
#
# Descrição dos Exemplos:
# No primeiro exemplo, pode-se verificar, por exemplo, que 1 é maior que 2. Comparando o valor encontrado 2 com  o restante 3, a função retorna corretamente que o maior valor encontrado é 3.
# No segundo exemplo, pode-se verificar, por exemplo, que 7 é igual a 7, portanto, portanto, o maior entre os dois valores é o próprio 7. Comparando o valor encontrado 7 com o restante 7, a função retorna corretamente que o maior valor encontrado é 7.
# No terceiro exemplo, pode-se verificar, por exemplo, que -1 é maior que -2. Comparando o valor encontrado -1 com o valor restante -3, a função retorna corretamente que o maior valor encontrado é -1.

def max2(a, b):
    if a > b:
        return a
    else:
        return b


def max3(a, b, c):
    x = max2(a, b)
    y = max2(x, c)
    return y

