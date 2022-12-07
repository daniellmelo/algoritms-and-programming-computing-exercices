# múltiplo
# de
# 3? Como
# descobrir
# usando
# recursividade
# mútua?
# Uma
# forma
# de
# se
# descobrir
# se
# um
# número
# é
# múltiplo
# de
# 3
# é
# ir
# diminuindo
# ele
# de
# 3
# até
# que
# não
# se
# possa
# mais
# subtrair
# 3
# sem
# que
# o
# resultado
# seja
# negativo.
#
# Por
# exemplo
# o
# número
# 12, será
# que
# ele
# é
# múltiplo
# de
# 3? É
# só
# ir
# subtraindo
# 3
# para
# ver
# se
# chega
# no
# zero, se
# chegar
# no
# zero
# é
# múltiplo
# de
# 3! 12 - 3 = 9;
# 9 - 3 = 6, 6 - 3 = 3;
# 3 - 3 = 0! Ou
# seja
# a
# sequência
# gerada
# terminou
# em
# zero, logo
# 12
# é
# múltiplo
# de
# 3.
#
# E
# o
# número
# 10, é
# múltiplo
# de
# 3? A
# sequência
# gerada
# é
# 10, 7, 4, 1;
# ou
# seja, não
# termina
# em
# zero, logo
# não
# é
# múltiplo
# de
# 3.
#
# Vendo
# estas
# sequências, Zezinho, que
# está
# tentando
# identificar
# um
# padrão
# para
# implementar
# uma
# solução
# usando
# recursividade
# mútua(duas
# ou
# mais
# funções
# sendo
# que
# uma
# chama
# a
# outra), tentou
# solucionar
# o
# problema
# da
# seguinte
# forma:
#
#
# def multiplo3(n):
#     if n == 0:
#         return True
#     elif n == 1 or n == 2:
#         return False
#     else:
#         return não_multiplo3(n - 3)
#
#
# def não_multiplo3(n):
#     if n == 0:
#         return False
#     elif n == 1 or n == 2:
#         return True
#     else:
#         return multiplo3(n - 3)
#
# Mas
# esta
# solução
# funciona
# para
# o
# número
# 12, por
# exemplo, mas
# não
# funciona
# para
# o
# número
# 15.
# Verifique
# por
# que
# isto
# acontece.Ache
# um
# padrão
# de
# sequência
# para
# que
# não
# aconteça
# o
# problema
# verificado
# e
# # implemente
# # a
# # recursão
# # mútua
# # de
#
# forma
# que
# ela
# funcione
# corretamente.
#
# A
# Entrada
# consiste
# de:
# de
# # uma
# # função
# # mutuamente
# # recursiva
# # que
# # pode
# ser
# ou
# multiplo3(n)
# ou
# não_multiplo3(n)
# onde / (n /)
# é
# o
# número
# que
# se
# quer
# verificar
# se
# é
# múltiplo
# de
# 3.
#
# A
# Saída
# # deve
# # apresentar:
# # True, se
# # for múltiplo de 3 e False, se não for múltiplo de 3
# # Exemplo:
# # o
# # enunciado
# # e
# # o
# # texto
# # são
# auto - explicativos


