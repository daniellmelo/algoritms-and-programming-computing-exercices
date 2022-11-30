# Mensagem com estilo
# Camila gosta de ficar até tarde conversando com seus amigos. Mas, de vez em quando, Camila acaba ignorada no seu grupo de mensagens. Ajude ela a criar mensagens que chamem mais atenção.
#
# Crie uma função chamada estilo()que receba um símbolo, um número e uma mensagem. O texto final deve ser a mensagem original, rodeada pela esquerda e pela direita com o símbolo, repetido um respectivo número de vezes.
#
#
# A Entrada consiste de:
# Chamada das duas funções, estilo(S,N,M), com parâmetros S, string com um símbolo único, N, número inteiro e M, string com a mensagem inicial.
# A Saída deve apresentar:
# Uma linha com a mensagem final de Camila.
#
# Descrição dos Exemplos:
# O símbolo "!" foi repetido 10 vezes, antes e depois da mensagem original.

def estilo(S, N, M):
    print(f"{S*N}{M}{S*N}")