#
# Média Aritmética, Ponderada e Harmônica
# Escreva um programa que leia 3 números inteiros positivos e efetue o cálculo das médias Aritmética (A), Ponderada (P) e Harmônica (H) dependendo da letra dada pelo usuário, mostre qual o tipo de média e qual o valor da média. No caso do usuário digitar qualquer outro caractere, apresente a mensagem 'Operacao inexistente'.
#
#
# A Entrada consiste de:
# Linha contendo as três notas que são três números reais positivos.
# Linha contendo um caractere (para determinar qual a média), sendo (P) Ponderada, (H) Harmônica e (A) Aritmética
# Caso o caractere seja 'P', deve-se solicitar os três pesos de cada nota enviada, que são números positivos inteiros.
#
# A Saída deve apresentar:
# Na primeira linha, o tipo de média que ele fez ("Harmonica", "Ponderada", "Aritmetica" ou "Operacao inexistente")
# Na segunda linha, caso tenha sido digito um caractere válido, o resultado da média com precisão de 2 casas decimais.
#
# Observações:
# Não é necessário validar se os valores de entrada estão dentro dos intervalos e tipos definidos.
#
# Descrição dos Exemplos:
# Os exemplos são autoexplicativos.

n1, n2, n3 = map(int, input().split())
media_nome = str(input())
if media_nome == "P":
    p1, p2, p3 = map(int, input().split())

    print("Ponderada")
    print(f"{((p1 * n1 + p2 * n2 + p3 * n3) / (p1 + p2 + p3)):.2f}")
elif (media_nome == "H"):
    print("Harmonica")

    print(f"{(3 / ((1 / n1) + (1 / n2) + (1 / n3))):.2f}")
elif (media_nome == "A"):
    print("Aritmetica")
    print(f"{((n1 + n2 + n3) / 3):.2f}")
else:
    print("Operacao inexistente")
