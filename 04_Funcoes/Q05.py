# Áreas
# Crie uma função chamada areas() que recebe 3 números inteiros (A, B e C) e calcula, em ordem:
#
# A área de um retângulo com lados A e B;
# A área de um triângulo com base B e altura C;
# A área de um trapézio de altura A, base menor B e base maior C.
# Apresente os valores ignorando a parte decimal.
#
#
# A Entrada consiste de:
# A entrada compreende os parâmetros da função areas(A,B,C), que são três números inteiros, sendo C maior que B.
# A Saída deve apresentar:
# Três linhas apresentando os valores solicitados. Para ignorar a parte decimal, pode-se utilizar a função int().
# Dica:
#
# Para ignorar a parte decimal, pode-se utilizar a função int() para mudar o tipo de ponto flutuante para inteiro.


def areas(A, B, C):
    print(int(A*B))
    print(int((B*C)/2))
    print(int(((B+C)*A)/2))