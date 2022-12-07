# Livro de Colorir
# Malu é uma artista renomada que, inspirada pelos sucessos dos livros de colorir para adultos decidiu criar ela mesma o seu próprio. Acontece que a arte de Malu tem um estilo muito peculiar: suas obras seguem um método estrito para serem produzidas, e ela deseja transmitir esse método através do seu livro de colorir.
#
# Considere que o livro elaborado por Malu terá sempre um quadriculado, com número igual de linhas e de colunas. No exato centro desse quadriculado haverá o caractere '⚫' simbolizando o ponto de início da coloração. Partindo do centro, a cada espaço do quadriculado será atribuído um número inteiro representando a distância deste espaço ao centro da figura. No entanto, para que a figura obtida seja satisfatória, Malu não permite que a distância entre um dado espaço vazio e o centro seja calculado considerando um caminho diagonal. É sempre necessário calcular a distância considerando um deslocamento horizontal e em seguida um deslocamento vertical, e a distância entre um espaço vazio e o centro é sempre a menor possível seguindo esses regras.
#
# A maior parte do programa para gerar essas artes já está pronto, mas Malu ainda não implementou a função calcula_distancia(), que recebe as coordenadas x e y do espaço vazio na matrix, e as coordenadas xc e yc do centro da figura e retorna um inteiro representando a distância entre esse espaço e o centro, considerando as regras impostas por Malu.
#
# Elabore a função calcula_distancia() que obtém a distância conforme especificado pelas regras de Malu e retorna um número inteiro representando a distância calculada.
#
#
# A Entrada consiste de:
# Não há entrada para essa questão. A função calcula_distancia() recebe parâmetros x, y, xc, e yc, todos inteiros positivos representando uma posição no quadriculado.
#
# A Saída deve apresentar:
# Não há saída para essa questão. A função calcula_distancia() deve retornar apenas um número inteiro representando a distância calculada conforme as regras de Malu.
#
# Observações:
# Não é necessário validar se os valores dos parâmetros são do tipo definido.
# É apenas necessário definir a função calcula_distancia().
# O nome deve necessariamente ser digitado como exposto no corpo da questão.
# Essa distãncia tamb´me é conhecida como distância Manhattan.
#
# Descrição dos Exemplos:
# Os exemplos são auto-explicativos.

