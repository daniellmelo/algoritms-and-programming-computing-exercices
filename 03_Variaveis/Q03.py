# Expres(u)s(u)ão
# Susu terminou sua tarefa de matemática e para revisar mais um pouco o conteúdo ela resolveu aplicar vários números em uma expressão numérica que ela mesma criou: para cada número x, primeiro multiplica-se x por 2, desse resultado subtrai-se 5 e por último acrescenta-se 2x. Escreva um programa que recebe um inteiro x, o aplica na expressão de Susu e retorna o resultado.
#
# A Entrada consiste de:
# x, um número inteiro positivo.
#
# A Saída deve apresentar:
# Um número inteiro, o resultado da expressão numérica.
#
# Observações:
# Não é necessário validar se os valores de entrada são do tipo definido.
#
# Descrição dos Exemplos:
# No primeiro exemplo, como x=7, multiplicamos o sete por dois, em seguida subtrai-se cinco desse resultado e por último adiciona-se 27: 14−5+128=137.
# For example:
#
# Input	Result
# 7
# 137
# 15
# 32793
# 1
# -1


x = int(input())
xi = x
x = x*2 # 7*2 = 14
x = x-5 # 14 - 5 = 9
x = x + (2**xi) #9 + (2^9)
print(x)