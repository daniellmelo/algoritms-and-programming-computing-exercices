# 5 patinhos? E se forem mais?
# Gael, um garotinho muito a frente de seu tempo, está aprendendo a programar. Ele fez um programa para imprimir a música dos 5 patinhos que foram passear. Um clássico infantil! O programa de Gael imprime todas as frases da música e ele sabe que um clássico devemos respeitar. Neste caso, a música tradicional conta 5 patinhos. Veja abaixo:
#
# print(f'5 patinhos')
# print(f'Foram passear')
# print(f'Além das montanhas')
# print(f'Para brincar')
# print(f'A mamãe gritou')
# print(f'Quá, quá, quá, quá!')
# print(f'Mas só 4 patinhos')
# print(f'Voltaram de lá')
# print(f'4 patinhos')
# print(f'Foram passear')
# print(f'Além das montanhas')
# print(f'Para brincar')
# print(f'A mamãe gritou')
# print(f'Quá, quá, quá, quá!')
# print(f'Mas só 3 patinhos')
# print(f'Voltaram de lá')
# print(f'3 patinhos')
# print(f'Foram passear')
# print(f'Além das montanhas')
# print(f'Para brincar')
# print(f'A mamãe gritou')
# print(f'Quá, quá, quá, quá!')
# print(f'Mas só 2 patinhos')
# print(f'Voltaram de lá')
# print(f'2 patinhos')
# print(f'Foram passear')
# print(f'Além das montanhas')
# print(f'Para brincar')
# print(f'A mamãe gritou')
# print(f'Quá, quá, quá, quá!')
# print(f'Mas só 1 patinhos')
# print(f'Voltaram de lá')
# print(f'1 patinhos')
# print(f'Foram passear')
# print(f'Além das montanhas')
# print(f'Para brincar')
# print(f'A mamãe gritou')
# print(f'Quá, quá, quá, quá!')
# print(f'Mas só 0 patinhos')
# print(f'Voltaram de lá')
# Mas e se fossem mais? Gael percebeu então que repetiu demais as frases e que dava pra fazer um código muito mais limpo e inteligente. Imagina 20 patinhos? Seria uma loucura esse código! Ele está ciente que você sabe modularizar um programa e pediu para que criasse duas funções de nome estrofe e refrao, onde cada uma deve receber um dos dois blocos de repetição que são possíveis observar nessa música. Ambas as funções devem receber como argumento um número n de patinhos que irá aparece na letra da música. A função estrofe deve chamar a execução da função refrao.
#
#
# A Entrada consiste de:
# Não se aplica. O CodeRunner irá aplicar os valores para realizar os testes.
#
# A Saída deve apresentar:
# As saídas exatamente como no código original, para cada bloco.
#
# Observações:
# Não é necessário validar se os valores de entrada estão dentro dos intervalos definidos.
# Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle irá descontar pontos caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome da função).
# Submeta SOMENTE o que foi solicitado
# O objetivo da questão é identificar os blocos e modularizá-los. Não se preocupe em apresentar a música por completo.
#
# Descrição dos Exemplos:
# Os exemplos são auto-explicativos. Veja que o CodeRunner vai testar ambas as funções.

def estrofe(n):
    #for i in range(0,2):
    print(f'{n} patinhos')
    print('Foram passear')
    print(f'Além das montanhas')
    print(f'Para brincar')
    print(f'A mamãe gritou')
    print(f'Quá, quá, quá, quá!')
    print(f'Mas só {n-1} patinhos')
    print(f'Voltaram de lá')
    print('Agora só falta aprender a fazer loop!')