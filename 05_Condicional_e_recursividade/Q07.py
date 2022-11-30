# Bomba relógio
# No treinamento do departamento de bombas da polícia, é preciso ser rápido para desarmar a bomba antes que ela exploda. Todos os policiais do setor possuem um tempo recorde em que eles conseguem desarmar a bomba, além disso cada bomba conta com um relógio regressivo que realiza a contagem de tempo que falta para a explosão. Porém, o programador do setor decidiu instalar travas de segurança nas bombas. De maneira que se o tempo recorde que o policial leva para desarmar uma bomba for maior que o tempo em que ela explode, a bomba é desativada automaticamente no último segundo antes de explodir. Caso o tempo recorde seja menor, o relógio segue com a contagem regressiva normalmente e portanto a bomba explode.
#
# Implemente um programa que simule um relógio regressivo e a cada segundo informe quanto tempo falta com a frase “ Atenção faltam n segundos...”. Faltando apenas 5 segundos ele deve mostrar a mensagem: “Seu tempo está acabando”, no último segundo, caso a bomba seja desativada a frase a ser apresentada é “Bomba desativada automaticamente!” e se encerra a contagem regressiva, se não apresenta a frase “Seja rápido. Falta apenas 1 segundo” e antes de explodir, no segundo 0,  a frase “Cabum!! Explodiu”.
#
#
# A Entrada consiste de:
# Duas variáveis do tipo inteiro, uma variável N (0<=N<=100) que indica o tempo inicial do relógio e uma P (0<=P<=100) que indica o tempo recorde do policial.
#
# A Saída deve apresentar:
# A contagem regressiva e as frases, "Seu tempo está acabando" no 5 segundo, "Bomba desativada automaticamente!" para casos em que for desativada, "Seja rápido. Falta apenas 1 segundo" e "Cabum!! Diga adeus ao mundo" caso não seja desativada.
#
# Observações:
# Não é necessário validar se os valores de entrada são do tipo definido.
#
# Descrição dos Exemplos:
# No primeiro exemplo, mesmo com o tempo do policial sendo maior que o da bomba, ainda assim ela explode pelo tempo ser 0.
# No segundo caso de teste vemos a contagem regressiva dos segundos e no 5 segundo a frase indicada. Como o tempo do policial é menor que o da bomba a trava de segurança não para a explosão e portanto a bomba explode.
# No terceiro caso de teste como o tempo do policial é maior que o da bomba, ela é desativada antes de explodir.


tempo_bomba = int(input())
tempo_recorde_bombeiro = int(input())
if tempo_bomba == 0:
    print("Cabum!!!! Explodiu")
    exit()

if tempo_bomba > tempo_recorde_bombeiro:
    for i in range(tempo_bomba, -1, -1):
        if i == 0:
            print("Cabum!!!! Explodiu")
            break
        if i == 1:
            print("Seja rápido. Falta 1 segundo")

        else:
            print(f"Atenção faltam {i} segundos...") if i != 5 else print("Seu tempo está acabando!")
else:
    for i in range(tempo_bomba, -1, -1):
        if i == 1:
            print("Bomba desativada automaticamente!")
            break
        else:
            print(f"Atenção faltam {i} segundos...") if i != 5 else print("Seu tempo está acabando!")