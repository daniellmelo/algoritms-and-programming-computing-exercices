# Sequência de Deivis
# Dêivis está fascinado por sequências. Dessa vez, ele criou a Sequência de Dêivis que é dada pelo seguinte:
#
# 1, 2, 2, 3, 4, 6, 9, 14, 22, 35, ...
#
# Assim, Dêivis te desafiou a criar uma função chamada deivis_sequence(n) que deve retornar o n-ésimo número da Sequência de Dêivis.
#
#
# A Entrada consiste de:
# O único parâmetro da sua função será o valor 1≤n≤31, que indica a posição do número da Sequência de Deivis que você deve retornar.
#
# A Saída deve apresentar:
# A função deve retornar um inteiro: o n-ésimo número da Sequência de Dêivis.
#
# Observações:
# Não é necessário validar se os valores de entrada estão dentro dos intervalos e tipos definidos.
# Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle irá descontar pontos caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome da função).
# Submeta SOMENTE o que foi solicitado.
#
# Descrição dos Exemplos:
# Os exemplos mostrar os valores de cada posição da sequência, dado que a primeira posição é 1.
# For example:
#
# Test	Result
# print(deivis_sequence(2))
# 2
# print(deivis_sequence(5))
# 4
# print(deivis_sequence(10))
# 35

def deivis_sequence(n:int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2
    n1 = 1
    n2 = 2
    for i in range(0,n-2):
        n3 = n1 + n2 - 1
        n1 = n2
        n2 = n3
    return n3