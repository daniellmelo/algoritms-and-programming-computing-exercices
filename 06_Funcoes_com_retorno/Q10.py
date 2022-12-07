# MDC
# O máximo divisor comum (MDC) entre dois ou mais números inteiros é o maior número inteiro que é fator de todos eles. Por exemplo, os divisores comuns de 12 e 18 são 1, 2, 3 e 6, logo o mdc(12,18)=6. No ano 300 a.c., o livro Elementos descreve um método para encontrar o MDC de dois números que é utilizado até os dias atuais, e é conhecido como Algoritmo de Euclides. Esse método baseia-se na seguinte propriedade: mdc(a,b)==mdc(b,r), onde r é o resto da divisão de a por b.
# Dessa forma, aproveitando-se dessa propriedade, é possível realizar sucessivas divisões entre pares de valores e seus restos, até que o resto de alguma divisão seja zero. Quando o resto passa a ser zero, o segundo elemento do último mdc realizado é o MDC dos pares iniciais. O algoritmo funciona da seguinte maneira:
#
# mdc(32,26) - o resto da divisão de 32 por 26 é 6
#
# mdc(26,6) - o resto da divisão de 26 por 6 é 2
#
# mdc(6,2) - o resto da divisão de 6 por 2 é 0
#
# mdc(2,0) - o resultado é 2, para mdc(32,26)
#
# Dessa forma, é possível escrever um algoritmo recursivo para o método de euclides da seguinte forma:
#
# mdc(a,b)={amdc(b,a%b)se b=0se a%b>0,b>0
#
# Dada a especificação recursiva para o algoritmo de euclides, sua tarefa é implementar uma função ;mdc(a, b) que calcule o MDC entre dois números a e b.
#
#
# A Entrada consiste de:
# Dois números inteiros a e b que representam os valores cujo MDC é procurado (1≥a,b≥1015).
#
# A Saída deve retornar:
# O MDC entre os valores a e b, conforme o exemplo.
#
# Observações:
# Não é necessário validar se os valores de entrada estão dentro dos intervalos e tipos definidos.
# Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle irá descontar pontos caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome da função).
# Submeta SOMENTE o que foi solicitado.
#
# Descrição dos Exemplos:
# No primeiro exemplo, o MDC entre 6 e 6 é calculado conforme a propriedade mencionada: mdc(6,6)=mdc(6,0), resultando em 6.
# No segundo exemplo, o MDC entre 12 e 30 é calculado conforme a propriedade mencionada: mdc(12,30)=mdc(30,12)=mdc(12,6)=mdc(6,0), resultando em 6.
# No terceiro exemplo, o MDC entre 105 e 60 é calculado conforme a propriedade mencionada: mdc(105,60)=mdc(60,45)=mdc(45,15)=mdc(15,0), resultando em 15.
# For example:
#
# Test	Result
# print(mdc(6,6))
# 6
# print(mdc(12,30))
# 6
# print(mdc(105,60))
# 15

def mdc(a: int, b: int) -> int:
    if b == 0:
        return a
    else:
        if a > b:
            return mdc(b, a)
        else:
            return mdc(a, b - a)



