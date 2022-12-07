
# N-ésimo termo da PA
# Elabore uma função n_termo() que recebe como parâmetros:  i o primeiro termo de uma progressão aritmética, r a razão dessa progressão aritmética e n seu número de termos e retorne o n-ésimo termo da PA.
#
#
# A Entrada consiste de:
# Não há entrada para essa questão, apenas os parâmetros da função n_termo(), i, r e n, três números inteiros.
#
# A Saída deve apresentar:
# Não há saída para essa questão, apenas é necessário que a função retorne o n-ésimo da progressão aritmética.
#
# Observações:
# Não é necessário validar se os valores dos parâmetros são do tipo definido.
#
# Descrição dos Exemplos:
# No primeiro exemplo, a razão 1 é somada a si mesma 98 vezes. Em seguida esse resultado é somado ao termo inicial 1, para obter o centésimo termo, resultando em 100.
# No segundo exemplo, a razão -1 é somada a si mesma 98 vezes. Em seguida esse resultado é somado ao termo inicial 100, para obter o centésimo termo, resultando em 1.
# No terceiro exemplo, a razão  é -5. Essa razão é somada ao termo inicial 5 para obter o segundo termo, resultando em 0.

def n_termo(i: int, r: int, n: int) -> int:
    return i + (n - 1) * r
