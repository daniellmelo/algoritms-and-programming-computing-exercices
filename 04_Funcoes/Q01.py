# Computador Simpático
# Os computadores estão evoluindo rapidamente, alcançando feitos intelectuais e deixando o poder de raciocínio humano em risco nas próximas décadas. Mas existe uma coisa que os computadores não podem aprender sozinhos... Educação e simpatia nas relações.
#
# Ensine o computador, criando uma função simples em Python chamada saudacao(), a fazer uma saudação personalizada.
#
#
# A Entrada consiste de:
# Chamada da função com um parâmetro no formato string (nome) de até 10 letras, que representa o nome da pessoa que receberá a saudação.
# A Saída deve apresentar:
# Uma linha com a saudação personalizada.
#
# For example:
#
# Test	Result
# saudacao("Ricardo")
# Bom dia, querido(a) Ricardo! Como você está?
# saudacao("Paula")
# Bom dia, querido(a) Paula! Como você está?
# saudacao("André")
# Bom dia, querido(a) André! Como você está?
def saudacao(nome):
    print(f"Bom dia, querido(a) {nome}! Como você está?")
