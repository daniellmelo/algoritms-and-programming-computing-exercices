# Gêmeos Pitá e Goras
# Pitá e Goras são irmãos gêmeos que amam matemática e gostam de aplicá-la em tudo o que vão fazer. Até mesmo na hora de comer eles utilizam números para definir o que vão jantar. Sua tarefa é ajudar os irmãos a implementarem um programa que os ajude a tomar a decisão do que irão jantar conforme o critério que eles estabeleceram. Para isso, os gêmeos decidiram que se a quantidade de minutos do relógio for um número par na hora que eles forem comer, então eles irão jantar arroz e feijão, mas se for um número ímpar eles irão fazer apenas um lanche.
#
#
# A Entrada consiste de:
# Uma variável M do tipo inteiro representando os minutos do relógio.
#
# A Saída deve apresentar:
#
# 1 linha contendo a frase “Fome de comida! Queremos arroz e feijão” para casos com números pares ou a frase "Só um lanchinho cai bem!" para os casos ímpares, sem as aspas conforme apresentado nos exemplos.
#
# Observações:
# Para a variável M serão considerados apenas valores entre 0  e 60 inclusive.
#
# Descrição dos Exemplos:
# No primeiro exemplo, a saída corresponde ao caso da entrada par conforme solicitado no enunciado.

M = int(input())
if M % 2 == 0:
    print("Fome de comida! Queremos arroz e feijão")
else:
    print("Só um lanchinho cai bem!")