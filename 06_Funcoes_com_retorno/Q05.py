# Par ou Impar
# Mariane está tentando ensinar a sua filha diferença entre os números ímpares pares. Mariane sabe que todo número dividido por 2 e com resto 0 será considerado par ou caso contrario será considerado ímpar. Ajude Mariana criando uma função ePar que diz se um número inteiro inserido é par ou não.
#
# Veja bem, este programa deve conter uma função que retorne os valores True ou False
#
#
# A Entrada consiste de:
# Não há valores de entrada, o sistema se encarrega de chamar a função
#
# A Saída deve apresentar:
# Não há saída expĺicita, o sistema se encarrega de chamar a função e apresentar um resultado.
#
# Observações:
# Não é necessário validar se os valores de entrada são do tipo definido.
#
# Descrição dos Exemplos:
# Exemplos autoexplicativos. Uma pequena estrutura de decisão recebe o valor de retorna da função e imprime se o número recebido é par ou ímpar.

def ePar(n:int)->str:
    if n % 2 == 0:
        return True
    return False