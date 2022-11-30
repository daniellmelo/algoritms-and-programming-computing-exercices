# Termômetro
# Pedrinho está estudando sobre temperatura e precisa converter vários valores de temperatura entre as diversas unidades. Para facilitar, Pedrinho pediu ajuda para você, de forma a pular todo esse trabalho chato e extenso de conversão.
#
# Dada uma temperatura T, em graus Celsius, crie uma função fahrenheit() que calcule e apresente a temperatura correspondente em graus Fahrenheit e uma função kelvin() que calcule e apresente a temperatura correspondente em Kelvin.
#
#
# A Entrada consiste de:
# Chamada das duas funções, fahrenheit(T) e kelvin(T), com o parâmetro T, um número inteiro, que representa a temperatura em graus Celsius.
# A Saída deve apresentar:
# Duas linhas que dispõem a temperatura em Fahrenheit e em Kelvin.
# Observações:
# Atente para o tipo de variável utilizado. Cálculos devem ser feitos com variáveis int ou float, já a impressão por meio do print, deve ser feito com string.
# Para correção correta, devem ser definidas duas funções, uma para cada conversão.
# Descrição dos Exemplos:
# No primeiro exemplo, a temperatura é de 32°C, que representa 89,6°F ou 305,15 K. O cálculo foi feito utilizando a conversão padrão entre temperaturas:
# fahrenheit = 1,8 * celsius + 32
# kelvin = celsius + 273,15


def fahrenheit(T):
    print(f"Fahrenheit: {1.8 * T + 32}")


def kelvin(T):
    print(f"Kelvin: {273.15 + T}")
