# Bolos
# Drikinha gosta de bolos de vários sabores. Uma vez por semana ela vai em uma padaria perto de casa e pede x pedaços de bolo de algum sabor, o pedaço de bolo tem o valor fixo de 3.25 reais, independentemente do sabor. Escreva um programa que recebe o sabor do bolo e a quantidade de pedaços que Drikinha irá comprar e retorne a frase do atendente: "Foram x pedaços de bolo de s, então fica z reais". Onde x é a quantidade de pedaços, s o sabor do bolo e z o total da compra de Drikinha em reais. Imprima o valor da compra com apenas duas casas após a vírgula.
#
#
# A Entrada consiste de:
# Uma string e um número inteiro positivo, representando o sabor do bolo e quantidade de pedaços respectivamente.
#
# A Saída deve apresentar:
# Uma string, como especificado no enunciado.
#
# Observações:
# Não é necessário validar se os valores de entrada são do tipo definido.
# Se atente ao formato dos valores da saída especificados no enunciado.
#
# Descrição dos Exemplos:
# No primeiro exemplo, o sabor do bolo escolhido foi baunilha e a quantidade de pedaços é 5, dessa forma a saída é "Foram 5 pedaços de bolo de baunilha, então fica 16.25 reais".
# Dica:
#
# Para ler mais de um valor por linha use a função split(), como mostrado a seguir, para ler 2 ou mais valores em uma mesma linha:
# x, y, z = input().split()
#
# Para quem quiser se aprofundar no funcionamento da função split() consulte a documentação de Python 3.x, em particular procure pelos métodos da classe str.
#
#
# For example:
#
# Input	Result
# baunilha 5
# Foram 5 pedaços de bolo de baunilha, então fica 16.25 reais
# morango 7
# Foram 7 pedaços de bolo de morango, então fica 22.75 reais
# passas 4
# Foram 4 pedaços de bolo de passas, então fica 13.00 reais
x, y = input().split()
print(f"Foram {y} pedaços de bolo de {x}, então fica {int(y)*3.25:.2f} reais")