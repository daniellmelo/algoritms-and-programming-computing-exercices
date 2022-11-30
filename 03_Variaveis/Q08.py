# Mônica em: criando sequências
# Quando está no tédio, Mônica gosta de criar sequências de letras. Mas ela não faz isso de uma maneira aleatória, segue todo um raciocínio para inventar uma sequência e em seguida, ela a escreve em seu caderninho vermelho.
#
# A fórmula de Mônica para criar uma sequência consiste em alguns elementos: três números inteiros a, b e c, todos maiores que zero e duas sequências p1 e p2 que já existem (podendo ou não ser de autoria da Mônica). Com todos os elementos, a Mônica cria a sequência da seguinte maneira:
#
# Repete a sequência "p1" a+b vezes;
#  Repete a sequência "p2" b+c vezes;
# Concatena o resultado do primeiro passo com o resultado do segundo passo;
# Repete o resultado do terceiro passo a+c vezes.
# Mônica gostaria de automatizar esse processo elaborando um programa com toda a lógica que ela desenvolveu, mas como o PC dela foi pro conserto, ela não pode fazer. Você poderia fazer esse favor a ela?
#
#
# A Entrada consiste de:
# Três números inteiros positivos.
# Duas strings, uma em cada linha, como apresentado nos exemplos.
#
# A Saída deve apresentar:
# Uma string, representando a sequência criada por Mônica.
#
# Observações:
# Não é necessário validar se os valores de entrada estão dentro dos intervalos definidos.
# Se atente aos parênteses.
#
# Descrição dos Exemplos:
# No primeiro exemplo, temos a = 1, b = 3 e c = 1, a primeira sequência "kj" e a segunda "yyu" são repetidas 4 vezes (a+b e b+c respectivamente). A concatenação das duas é "kjkjkjkjyyuyyuyyuyyu", que repetida duas vezes se torna "kjkjkjkjyyuyyuyyuyyukjkjkjkjyyuyyuyyuyyu".
# No segundo exemplo, a primeira sequência é repetida 2 vezes (a+b), e a segunda, 4 (b+c). Após a concatenação no passo três a sequência resultante repetida a+c vezes é "wdvwdvdadadadadadadadawdvwdvdadadadadadadadawdvwdvdadadadadadadadawdvwdvdadadadadadadada".

a = int(input())
b = int(input())
c = int(input())
ab = a + b
bc = b + c
ac = a + c
p1 = input()
p2 = input()
for i in range(0,ac):
    print(ab*p1 + bc*p2, end='')