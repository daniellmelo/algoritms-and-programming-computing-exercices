# NN
# Escreva um programa que recebe um número inteiro  de dois dígitos, mas representado como um número real com zeros após o ponto decimal. Retorne a parte inteira desse número multiplicado por 100 mais ele mesmo, isto é, um inteiro de quatro dígitos.
#
#
# A Entrada consiste de:
# Um número inteiro x, tal que 10.00≤x<99.00
#
# A Saída deve apresentar:
# Um número inteiro y, tal que 1000≤x<9999
#
# Observações:
# Não é necessário validar se os valores de entrada são do tipo definido.
#
# Descrição dos Exemplos:
# No primeiro exemplo a entrada é o número 51. Multiplicando este número uma vez por 100 e somando ele ao resultado da multiplicação a saída é 5151.
# For example:
#
# Input	Result
# 51
# 5151
# 14
# 1414
# 33
# 3333

x = float(input())
x = int(x)
print(f"{str(x)}{str(x)}")