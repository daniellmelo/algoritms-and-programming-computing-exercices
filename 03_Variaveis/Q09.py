# Textões
# Malu utiliza uma rede social muito famosa, conhecida por permitir que você se expresse sobre os mais diversos e importantes temas da atualidade, perpetuando sempre questionamentos relevantes. Essa rede social, no entanto, preza pela objetividade acima de tudo, e desde sua fundação tem o histórico de permitir apenas uma quantidade limitada de caracteres por postagem, para que as pessoas não gastem tempo demais lendo sobre apenas um assunto.
#
# Alguns usuários, no entanto, arrumaram um método sorrateiro para poder escrever longos e tediosos textos e assim ocupar o tempo de todos os usuários da rede.
#
# Para salvar a todos deste destino terrível, você tem a missão de criar uma ferramenta capaz de detectar os chamados "textões" da internet. Considere que um adulto médio consegue ler aproximadamente de 1200 a 1550 caracteres por minuto.
#
# Dada uma postagem qualquer, calcule o tempo necessário para que um adulto médio consiga ler todo seu conteúdo. Mostre em duas linhas diferentes o pior tempo estimado e o melhor tempo estimado (em minutos), com uma precisão de 3 casas decimais.
#
#
# A Entrada consiste de:
# Uma string S contendo todo o texto da postagem.
#
# A Saída deve apresentar:
# Na primeira linha, o pior tempo de leitura estimado em minutos sob a seguinte formatação: "Pior dos casos: PC", onde PC é um número real (de ponto decimal) que representa o pior tempo estimado com três casas decimais de precisão.
# Na segunda linha, o melhor tempo de leitura estimado em minutos sob a seguinte formatação: "Melhor dos casos: MC ", onde MC é um número real que representa o melhor tempo estimado com três casas decimais de precisão.
#
# Observações:
# Não é necessário validar se os valores de entrada estão dentro dos intervalos definidos.
# Espaços em brancos são lidos como caracteres normais.
# Descrição dos Exemplos:
# No primeiro exemplo, a quantidade de caracteres total da string é igual a 728. No pior dos casos o usuário demora 0,607 minutos pra ler. No melhor dos casos, ele demora 0,470 minutos.
# Dica:
#
# Uma forma eficiente de contar a quantidade total de caracteres em uma string é utilizar a função len(), que para o caso de strings retorna sua quantidade total de caracteres.
#
# Por exemplo: len('batata') retorna o valor inteiro 6.
#
# Essa função possui uma variedade de usos, então acostume-se a utiliza-la quando necessário!
#


S = len(input())
print(f"Pior dos casos: {(S/1200):.3f}")
print(f"Melhor dos casos: {(S/1550):.3f}")