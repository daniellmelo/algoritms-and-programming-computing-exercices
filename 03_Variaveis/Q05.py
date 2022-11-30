# Depurando um programa Python
# O CodeRunner é um sistema para avaliação automática de programas de computador. A proposta é simples, cada questão apresenta um contexto e descreve um problema, e você deve prover como resposta um trecho de código que resolva este problema. A avaliação também é simples, o sistema fornece informações (dados de entrada) ao seu programa e compara o resultado obtido (dados de saída) com o resultado esperado (gabarito). Se forem iguais, você acertou a questão.
#
# Por exemplo, suponha que o problema seja: "Dado dois números inteiros de entrada que são a base e a altura de um triângulo, mostre o valor da área com duas casas decimais." Um código que resolve esse problema é mostrado abaixo. No entanto, ele tem erros de sintaxe e de semântica.
#
# base  = input()
# altura = input()
# base = int(Base)
# area = (base * altura)
# print(f'{area:.3f}')
# Verifique a solução apresentada e o corrija. Seu trabalho é consertar o programa.
#
#
# A Entrada consiste de:
# Duas linhas, cada uma contendo um número inteiro positivo.
#
# A Saída deve apresentar:
# Uma linha com a área de triângulo com duas casas decimais.
#
# Observações:
# Não é necessário validar se os valores de entrada estão dentro dos intervalos definidos.
#
# Descrição dos Exemplos:
# Os exemplos são autoexplicativos. Dada a entrada basta aplicar na equação.
# For example:
#
# Input	Result
# 0
# 0
#        0.00
# 2
# 3
#       3.00
# 4
# 5
#       10.00

base  = int(input())
altura = int(input())
area = (base * altura)/2
print(f'{area:.2f}')