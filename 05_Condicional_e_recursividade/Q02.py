# Filtro de Códigos
# Para programar existem alguns requisitos que nossos códigos devem atender independente do problema. Para isso, algumas perguntas podem ser feitas durante a implementação de um programa, conforme demonstra o guia abaixo. Sua tarefa é implementar um programa que ajude os programadores a avaliarem seus códigos da mesma forma que o guia. A figura apresenta a ordem das perguntas que deverão ser feitas.
#
#
#
#
# A Entrada consiste de:
# Após cada pergunta é lida uma String que pode ser do tipo 'SIM' ou 'NÃO'.
#
# A Saída deve apresentar:
# Todas as perguntas de acordo com as respostas do usuário e por fim uma das cinco possíveis respostas finais.
#
# Observações:
# Não é necessário validar se os valores de entrada são do tipo definido.
#
# Descrição dos Exemplos:
# Os exemplo são auto explicativos.

print("O programa funciona?")
p1 = input()
if p1 == "SIM":
    print("Você entende o que fez?")
    p2 = input()
    if p2 == "SIM":
        print("Ótimo. Então não mexe!")
    else:
        print("Já foi na tutoria?")
        p3 = input()
        if p3 == "SIM":
            print("Choremos!")
        else:
            print("Temos um time a disposição!")
else:
    print("Você sabe onde está o erro?")
    p2 = input()
    if p2 == "SIM":
        print("Acha que pode solucionar sozinho?")
        p3 = input()
        if p3 == "SIM":
            print("Então mão na massa!")
        else:
            print("Já pesquisou no Google?")
            p4 = input()
            if p4 == "SIM":
                print("Já foi na tutoria?")
                p5 = input()
                if p5 == "SIM":
                    print("Choremos!")
                else:
                    print("Temos um time a disposição!")
            else:
                print("Corre lá então!")
    else:
        print("Já foi na tutoria?")
        p3 = input()
        if p3 == "SIM":
            print("Choremos!")
        else:
            print("Temos um time a disposição!")