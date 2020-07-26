########################################################################################################################
# DATA: 02/07/2020
# DISCIPLINA: VISÃO COMPUTACIONAL NO MELHORAMENTO DE PLANTAS
# PROFESSOR: VINÍCIUS QUINTÃO CARNEIRO
# E-MAIL: vinicius.carneiro@ufla.br
# GITHUB: vqcarneiro
# ALUNO: JÚLIO AUGUSTO DE CASTRO MIGUEL
# E-MAIL: juliocastromiguel83@gmail.com
########################################################################################################################

# REO 01 - LISTA DE EXERCÍCIOS

########################################################## ########################################################## ####################
#'''
print ( "----------------------------------------------- -------------------------------------------------- -------------- " )
print ( "Exercício N ° 1" )
print ( "Declare os valores 43.5,150.30,17,28,35,79,20,99.07,15 como um array numpy." )
print ( "Letra A)" )
import  numpy  as  np
vetor =  np . array ([ 43.5,150.30,17,28,35,79,20,99.07,15 ])
print ( "O vetor =" , vetor )
print ( "" )
print ( "------------------------------------" )
print ( "" )
print ( "Letra B)" )
print ( "Exibir informações de tamanho, média, máximo, mínimo e variação deste vetor." )
dim_01 = len ( vetor )
print ( "Um registro do vetor é" , str ( dim_01 ))
print ( "O valor máximo é:" , np . max ( vetor ))
print ( "O menor valor no vetor é:" , np . min ( vetor ))
print ( "A Media é:" , np . mean ( Vetor ))
print ( "A variância é:" , np . var ( vetor ))
print ( "" )
print ( "----------------------------------------------- ------------------------------- " )
print ( "" )
print ( "Letra C)" )
print ( "Mostrar um novo vetor em que cada elemento é dado pelo quadrado da diferença entre cada elemento do vetor declarado na letra aeo valor da média deste." )
vetor_np = ( vetor  -  np . média ( vetor )) ** 2
print ( "Novo vetor =" , vetor_np )
print ( "" )
print ( "----------------------------------------------- ------------------------------- " )
print ( "" )
print ( "Letra D)" )
print ( "Mostrar um novo vetor que contém todos os valores superiores a 30." )
bool_vetor =  vetor > 30
menor_vetor = vetor [ bool_vetor ]
print ( "Novo vetor com os valores acima de 30 =" , menor_vetor )
print ( "" )
print ( "----------------------------------------------- ------------------------------- " )
print ( "" )
print ( "Letra E)" )
print ( "Identifique quais são as posições do vetor originais possuem valores superiores a 30" )
posi_vetor  =  np . onde ( vetor > 30 )
print ( "As posições com valores iguais a 30 são:" , posi_vetor [ 0 ])
print ( "" )
print ( "----------------------------------------------- ------------------------------- " )
print ( "" )
print ( "Letra F)" )
print ( "Apresente um vetor que contém os valores da primeira, quinta e última posição." )
vetor_1 = ( vetor [ 0 ])
vetor_5 = vetor [ 4 ]
vetor_last = vetor [ 8 ]
new_vetor = vetor_1 , vetor_5 , vetor_last
print ( "O novo vetor com os valores da posição 1 °, 5 ° e 9 ° =" , new_vetor )
print ( "" )
print ( "----------------------------------------------- ------------------------------- " )
#'''
print ( "" )
print ( "Letra G)" )
print ( "Crie uma estrutura de repetição usando para exibir cada valor e sua posição durante as iterações" )
it = 0
para  i  no  intervalo ( 0 , len ( vetor ), 1 ):
    it  =  it  +  1
    print ( 'Iteração:'  +  str ( it ))
    print ( 'Na posição'  +  str ( i ) +  'há o elemento:'  +  str ( vetor [ int ( i )]))
    hora . sono ( 0,5 )

print ( "" )
print ( "----------------------------------------------- ------------------------------- " )
print ( "" )
print ( "Letra H)" )
print ( "Crie uma estrutura de repetição usando o para fazer um soma dos quadrados de cada valor do vetor." )
it = 0
somador = 0
para  i  no  intervalo ( 0 , len ( vetor ), 1 ):
    it  =  it  +  1
    somador = somador +  vetor [ int ( i )] **  2
    print ( 'Iteração:'  +  str ( it ))
    print ( 'Na posição'  +  str ( i ) +  'há o valor:'  +  str ( vetor [ int ( i )]))
    hora . sono ( 0,5 )

print ( "" )
print ( "soma de quadrados dos valores é:" , somador )

print ( "" )
print ( "----------------------------------------------- ------------------------------- " )
print ( "" )
print ( "Letra I)" )
print ( "Crie uma estrutura de repetição usando enquanto exibe todos os valores do vetor" )
print ( "R: Abaixo estão apresentados todos os valores do vetor:" )
pos  =  0
while  vetor [ pos ] ! = 100 :
    print ( vetor [ pos ])
    pos  =  pos + 1
    hora . sono ( 0,5 )
    se  pos == ( len ( vetor )):
        print ( 'Posição igual a:'  +  str ( pos ) +  '- A condição retornou true, vamos sair while' )
        pausa

print ( "" )
print ( "----------------------------------------------- ------------------------------- " )
print ( "" )
print ( "Letra J)" )
print ( "Crie uma sequência de valores com o mesmo tamanho do vetor original e inicie em 1 e o passo seja também 1." )
n_seq  =  np . array ( np . arange ( 1 , len ( vetor ) + 1 , 1 )))

print ( "Novo vetor:" , n_seq )

print ( "" )
print ( "----------------------------------------------- ------------------------------- " )
print ( "" )
print ( "Letra K)" )
print ( "Concatene o vetor da letra a com o vetor da letra j." )
conc  =  np . concatenar (( vetor , n_seq ), eixo = 0 )
print ( "Novo vetor concaternado =" , conc )

print ( "================================================= ==================================================== ============== " )
print ( "Segundo roteiro" )
print ( "EXERCÍCIO NUMERO 2" )
print ( "Letra A)" )
print ( "Declare uma matriz abaixo com uma biblioteca numpy."
      "1 3 22"
      "2 8 18"
      "3 4 22"
      "4 1 23"
      "5 2 52"
      "6 2 18"
      "7 2 25" )
import  numpy  as  np
matriz_01  =  np . matriz ([[ 1 , 3 , 22 ],
                [ 2 , 8 , 18 ],
                [ 3 , 4 , 22 ],
                [ 4 , 1 , 23 ],
                [ 5 , 2 , 52 ],
                [ 6 , 2 , 18 ],
                [ 7 , 2 , 25 ]])
print ( matriz_01 )
print ( "" )
print ( "----------------------------------------------- ------------------------------- " )
print ( "" )
print ( "Letra B)" )
print ( "Exibir o número de linhas e colunas desta matriz" )
nl , nc = np . forma ( matriz_01 )
print ( "Número de linhas =" , nl )
print ( "Número de colunas =" , NC )
print ( "" )
print ( "----------------------------------------------- ------------------------------- " )
print ( "" )
print ( "Letra C)" )
print ( "Exibir as mídias das colunas 2 e 3." )
med1_2 = np . média ( matriz_01 [ 0 :, 1 ])
med1_3 = np . média ( matriz_01 [ 0 :, 2 ])
print ( "Média da coluna 2 é:" , med1_2 )
print ( "Média da coluna 3 é:" , med1_3 )
print ( "" )
print ( "----------------------------------------------- ------------------------------- " )
print ( "" )
print ( "Letra D)" )
print ( "Mostrar as mídias das linhas, considerando apenas as colunas 2 e 3" )
print ( "Linha Média" )
l1_2 = np . média ( matriz_01 [ 0 , 1 : 3 ])
l2 = np . média ( matriz_01 [ 1 , 1 : 3 ])
13 = np . média ( matriz_01 [ 2 , 1 : 3 ])
l4 = np . média ( matriz_01 [ 3 , 1 : 3 ])
l5 = np . média ( matriz_01 [ 4 , 1 : 3 ])
l6 = np . média ( matriz_01 [ 5 , 1 : 3 ])
l7 = np . média ( matriz_01 [ 6 , 1 : 3 ])
impressão ( "1" , l1_2 )
impressão ( "2" , l2 )
impressão ( "3" , l3 )
impressão ( "4" , l4 )
impressão ( "5" , l5 )
impressão ( "6" , l6 )
impressão ( "7" , l7 )
print ( "" )
print ( "----------------------------------------------- ------------------------------- " )
print ( "" )
print ( "Letra E)" )
print ( "definir que a primeira coluna seja uma identificação de genótipos, uma segunda nota de gravidade de uma doença e"
      "e o terceiro peso de 100 grãos. Mostrar os genótipos que possuem nota de severidade inferior a 5." )
menor_sev = matriz_01 [ 0 :, 1 ] < 5
position  =  np . onde ( menor_sev )
matriz_sev_bool = matriz_01 [ posição ]

imprimir ( "Os genótipos com severidade de Doença inferior that were 5:" , matriz_sev_bool [ 0 :, 0 ])
print ( "" )
print ( "----------------------------------------------- ------------------------------- " )
print ( "" )
print ( "Letra F)" )
print ( "definir que a primeira coluna seja uma identificação de genótipos, uma segunda nota de gravidade de uma doença e"
      "um terceiro peso de 100 grãos. Mostrar os genótipos que possuem uma nota de peso de 100 grãos superior ou igual a 22." )
maior_igual_22  =  matriz_01 [ 0 :, 2 ] > = 22
print ( maior_igual_22 )
big_position = np . onde ( maior_igual_22 )
maior_bool = matriz_01 [ big_position ]
print ( maior_bool )
print ( "" )
imprimir ( "Os genótipos com Maior nota de peso de 100 Grãos were:" , maior_bool [ 0 :, 0 ])
print ( "" )
print ( "----------------------------------------------- ------------------------------- " )
print ( "" )
print ( "Letra G)" )
print ( "definir que a primeira coluna seja uma identificação de genótipos, uma segunda nota de gravidade de uma doença e" )
print ( "um terceiro peso de 100 grãos. Mostrar os genótipos que possuem uma nota de gravidade igual ou inferior a 3 e peso de 100" )
print ( "grãos iguais ou superiores a 22." )
nota_3 = maior_bool [ 0 :, 1 ] <= 3
matriz_new = np . onde ( nota_3 )
matriz = maior_bool [ matriz_new ]
impressão ( matriz )
print ( "" )
imprimir ( "Os genótipos com nota de peso de 100 Grãos Maior OU igual a 22 e menor severidade that were 3:" , matriz [ 0 :, 0 ])
print ( "" )
print ( "----------------------------------------------- ------------------------------- " )
print ( "" )
print ( "Letra H)" )
print ( "Crie uma estrutura de repetição com o uso de (loop) para apresentar na tela cada uma das posições da matriz e o seu" )
print ( "esses valores. Utilize um iterador para mostrar ao usuário quantas vezes está sendo repetido." )
print ( "Apresente a seguinte mensagem a cada iteração {Na linha X e na coluna Y ocorre o valor: Z}" )
print ( "Nesta estrutura crie uma lista que armazena os genótipos com peso de 100 grãos iguais ou superiores a 25" )
 hora de importação
contador = 0
matriz_quadrados  =  np . zeros (( nl , nc ))
para  i  no  np . arange ( 0 , nl , 1 ):
    para  j  em  np . arange ( 0 , nc , 1 ):
        contador  + =  1
        print ( 'Iteração:' +  str ( contador ))
        print ( 'Na linha'  +  str ( i ) +  'e coluna'  +  str ( j ) +  'há o elemento:'  +  str ( matriz_01 [ int ( i ), int ( j )]))
        hora . sono ( 0,5 )
        matriz_quadrados [ int ( i ), int ( j )] = ( matriz_01 [ int ( i ), int ( j )]) ** 2
        print ( "" )
        print ( '----------------------------------------------- -------------------------------------------------- ---------------- ' )
        print ( "" )
np . set_printoptions ( precision = 2 )
np . set_printoptions ( suprimir = True )
print ( matriz_01 )
print ( "----------" )
print ( matriz_quadrados )
print ( "" )

print ( "================================================= ==================================================== ============== " )
print ( "Terceiro roteiro" )
print ( "EXERCÍCIO NUMERO 3" )
print ( "Letra A)" )
print ( "Crie uma função em um arquivo externo (outro arquivo .py) para calcular a média e a variação amostral de um vetor qualquer, com base em um loop (para)." )
print ( 'A função está no arquivo FUNCTION_4' )
print ( "" )
print ( "----------------------------------------------- ------------------------------- " )
print ( "" )
print ( "Letra B)" )
print ( "Simule três matrizes com uma biblioteca de 10, 100 e 1000 valores e com distribuição normal com média de 100 e variação de 2500. Pesquise em registros de numeração por funções de simulação." )
print ( "Valores aleatórios de 10, 100 e 1000 impressões" )
# np.set_printoptions (precision = 2)
# np.set_printoptions (suprimir = True)
import  numpy  as  np
dados_10 =  np . aleatório . normal ( loc = 100 , escala = 50 , tamanho = 10 )
print ( "Vetor de 10 cores aleatórias com mídia 100 e variação de 2500:" , dados_10 )
print ( "" )
print ( "----------------------------------------------- ------------------------------- " )
print ( "" )
dados_100  =  np . aleatório . normal ( loc = 100 , escala = 50 , tamanho = 100 )
print ( "Vetor 100 cores aleatórias com mídia 100 e variação de 2500:" , dados_100 )
print ( "" )
print ( "----------------------------------------------- ------------------------------- " )
print ( "" )
dados_1000  =  np . aleatório . normal ( loc = 100 , escala = 50 , tamanho = 1000 )
print ( "Vetor 1000 cores aleatórias com mídia 100 e variação de 2500:" , dados_1000 )
print ( "" )
print ( "----------------------------------------------- ------------------------------- " )
print ( "" )
print ( "Letra C)" )
print ( "Utilize uma função criada na letra para obter como mídias e variações dos vetores simulados na letra b." )
da  mídia de importação function_4
de  function_4  import  variancia
print ( "Conjunto de dados com 10 dimensões" )
print ( "mídia" , mídia ( dados_10 ))
print ( "variancia" , variancia ( dados_10 ))
print ( "------------------------------------" )
print ( "Conjunto de dados com 100 cores" )
print ( "mídia" , mídia ( dados_100 ))
print ( "variancia" , variancia ( dados_100 ))
print ( "------------------------------------" )
print ( "Conjunto de dados com 1000 dimensões" )
impressão ( "mídia" , mídia ( dados_1000 ))
print ( "variancia" , variancia ( dados_1000 ))
print ( "" )
print ( "----------------------------------------------- ------------------------------- " )
print ( "" )
print ( "Letra D)" )
print ( "Crie histogramas com uma biblioteca de vetores simulados com valores de 10, 100, 1000 e 100000." )
dados_100000  =  np . aleatório . normal ( loc = 100 , escala = 50 , tamanho = 100000 )
# nl1, nc1 = dados_10.shape
# nl2, nc2 = dados_100.shape
# nl3, nc3 = dados_1000.shape
# nl4, nc4 = dados_100000.shape
# fig = plt.figure ("Gráfico Histograma")
# plt.hist
import  matplotlib . pyplot  como  plt
de  matplotlib  import  colors
#from matplotlib.ticker import PercentFormatter
#histogra_exemplo = plt.hist (dados_1000, posições = 15) #para plotar com uma única cor (azul)
# plt.hist (dados_10, compartimentos = 15)
# plt.hist (dados_100, compartimentos = 15)
# plt.hist (dados_1000, compartimentos = 15)
# plt.hist (dados_100000, compartimentos = 15)
fig , machados  =  plt . subtramas ( 1 , tight_layout = True )
N , caixas , remendos  =  machados . hist ( dados_10 , compartimentos = 5 )
FRACS  =  N  /  N . max ()
norma  =  cores . Normalizar ( fracs . Min (), fracs . Max ())
para  thisfrac , thispatch  em  zip ( fracs , patches ):
    color  =  plt . cm . viridis ( norma ( thisfrac ))
    este remendo . set_facecolor ( cor )
plt . title ( 'Histograma 10' )
plt . xlabel ( 'Número de elementos na classe' )
plt . ylabel ( 'Valor médio da classe' )


fig , machados  =  plt . subtramas ( 1 , tight_layout = True )
N , caixas , remendos  =  machados . hist ( dados_100 , compartimentos = 10 )
FRACS  =  N  /  N . max ()
norma  =  cores . Normalizar ( fracs . Min (), fracs . Max ())
para  thisfrac , thispatch  em  zip ( fracs , patches ):
    color  =  plt . cm . viridis ( norma ( thisfrac ))
    este remendo . set_facecolor ( cor )
plt . título ( 'Histograma 100' )
plt . xlabel ( 'Número de elementos na classe' )
plt . ylabel ( 'Valor médio da classe' )
fig , machados  =  plt . subtramas ( 1 , tight_layout = True )
N , caixas , remendos  =  machados . hist ( dados_1000 , compartimentos = 15 )
FRACS  =  N  /  N . max ()


norma  =  cores . Normalizar ( fracs . Min (), fracs . Max ())
para  thisfrac , thispatch  em  zip ( fracs , patches ):
    color  =  plt . cm . viridis ( norma ( thisfrac ))
    este remendo . set_facecolor ( cor )
plt . título ( 'Histograma 1000' )
plt . xlabel ( 'Número de elementos na classe' )
plt . ylabel ( 'Valor médio da classe' )
fig , machados  =  plt . subtramas ( 1 , tight_layout = True )
N , caixas , remendos  =  machados . hist ( dados_100000 , compartimentos = 70 )
FRACS  =  N  /  N . max ()
norma  =  cores . Normalizar ( fracs . Min (), fracs . Max ())
# Agora, percorreremos nossos objetos e definiremos a cor de cada um de acordo
para  thisfrac , thispatch  em  zip ( fracs , patches ):
    color  =  plt . cm . viridis ( norma ( thisfrac ))

este remendo . set_facecolor ( cor )
plt . título ( 'Histograma 100000' )
plt . xlabel ( 'Número de elementos na classe' )
plt . ylabel ( 'Valor' )
plt . show ()
print ( "================================================= ==================================================== ============== " )
print ( "Terceiro roteiro" )
print ( "EXERCÍCIO NUMERO 4" )
print ( "Letra A)" )
print ( "O arquivo dados.txt contem uma avaliação de genótipos (primeira coluna) em repetições (segunda coluna) quanto a quatro"
      "variáveis ​​(terceira coluna na frente). Portanto, carrega ou arquivo de dados.txt com uma biblioteca numpy, apresenta os dados e obtém como informações"
      "de dimensão desta matriz." )
importar  numpy  como  np
dados_ex4  = np . loadtxt ( 'dados.txt' )
nl , nc  =  dados_ex4 . forma
print ( dados_ex4 )
print ( "" )
print ( "N ° de linhas:" , nl )
print ( "N ° de colunas:" , nc )
print ( "" )
print ( "----------------------------------------------- ------------------------------- " )
print ( "" )
print ( "Letra B)" )
print ( "Pesquise sobre as funções np.unique e np.where da biblioteca numpy" )
print ( "As funções:" )
print ( "np.unique = é capaz de identificar (objetos) repetidos dentro da matriz" )
print ( "np.where = é capaz de retornar uma condição de um vetor booleano" )
print ( "" )
print ( "----------------------------------------------- ------------------------------- " )
print ( "" )
print ( "Letra C" )
print ( "Mostrar forma automática dos genótipos e quantas repetições foram avaliadas" )
print ( "O experimento foi feito com" , len ( np . único ( dados_ex4 [:, 1 ])), "repetições" )
print ( "" )
print ( "----------------------------------------------- ------------------------------- " )
print ( "" )
print ( "Letra D)" )
print ( "Apresenta uma matriz contendo apenas as colunas 1, 2 e 4" )
sub_dados = dados_ex4 [:, [ 0 , 1 , 3 ]]
print ( sub_dados )
print ( "" )
print ( "----------------------------------------------- ------------------------------- " )
print ( "" )
print ( "Letra E)" )
print ( "Escolha uma matriz que contenha o máximo, o mínimo, a média e a variação de cada genótipo para uma variável da coluna 4. Salve esta matriz no bloco de notas." )
nl2 , nc2 = np . shape ( sub_dados )
impressão ( nl2 )
mat = np . zeros (( 10 , 4 ))
it = 0
genotipo =  np . remodelar ( np . exclusivo ( dados_ex4 [:, 0 ], eixo = 0 ), ( 10 , 1 ))
#print (genotipo)
para  num  em  np . arange ( 0 , nl2 , 3 ):
    mat [ it , 0 ] =  np . max ( sub_dados [ num : num  +  3 , 2 ], eixo = 0 )
    mat [ it , 1 ] =  np . min ( sub_dados [ num : num  +  3 , 2 ], eixo = 0 )
    mat [ it , 2 ] =  np . média ( sub_dados [ num : num  +  3 , 2 ], eixo = 0 )
    mat [ it , 3 ] =  np . var ( sub_dados [ num : num  +  3 , 2 ], eixo = 0 )
    it  + =  1  #incrementa + 1 não

#print (mat)
np . set_printoptions ( precision = 2 )
np . set_printoptions ( suprimir = True )
print ( 'Genótipos Max Min Média Variância' )
matriz_concat  =  np . concatenar (( genotipo , tapete ), eixo = 1 )
print ( matriz_concat )
#import os
#help (np.savetxt)
np . savetxt ( "Matriz de dados.txt" , matriz_concat , fmt = '% 2.2f' , delimitador = ' \ t ' )
# np.savetxt ('matriz_ex3.txt', matriz_concat, delimitador = '')
print ( "" )
print ( "----------------------------------------------- ------------------------------- " )
print ( "" )
print ( "Letra F)" )
print ( "Mostrar os genótipos que possuem média (mídia das repetições) igual ou superior a 500 da matriz gerada na letra anterior." )
print ( "" )
print ( "Matriz" )
print ( "___________________________________________________" )
print ( "Genótipos Max Min Média Variância" )
print ( matriz_concat )
print ( "___________________________________________________" )
print ( "" )
print ( "" )
matriz_med_maior = matriz_concat [ matriz_concat [:, 3 ] > = 500 ]
print ( "Os genótipos que possuem média maior ou igual a 500 são:" , matriz_med_maior [:, 0 ])
print ( "" )
print ( "----------------------------------------------- ------------------------------- " )
print ( "" )
print ( "Letra G)" )
print ( "Presentes os seguintes gráficos:" )
print ( "- Médias dos genótipos para cada variável. Utilizando o comando plt.subplot para mostrar mais de um gráfico por figura" )
print ( "___________________________________________________" )
print ( "GEN REP Var1 Var2 Var3 Var4 Var5" )
print ( "___________________________________________________" )
print ( dados_ex4 )
print ( "___________________________________________________" )
print ( "" )
nl3 , nc3 =  dados_ex4 . forma
mat_zeros = np . zeros (( 10 , 5 ))
it = 0
GEN =  np . remodelar ( np . exclusivo ( dados_ex4 [:, 0 ], eixo = 0 ), ( 10 , 1 ))
para  num  em  np . arange ( 0 , nl3 , 3 ):
    mat_zeros [ it , 0 ] =  np . média ( dados_ex4 [ num : num  +  3 , 2 ], eixo = 0 )
    mat_zeros [ it , 1 ] =  np . média ( dados_ex4 [ num : num  +  3 , 3 ], eixo = 0 )
    mat_zeros [ it , 2 ] =  np . média ( dados_ex4 [ num : num  +  3 , 4 ], eixo = 0 )
    mat_zeros [ it , 3 ] =  np . média ( dados_ex4 [ num : num  +  3 , 5 ], eixo = 0 )
    mat_zeros [ it , 4 ] =  np . média ( dados_ex4 [ num : num  +  3 , 6 ], eixo = 0 )
    it  + =  1  #incrementa + 1 não


mat_concat  =  np . concatenar (( GEN , mat_zeros ), eixo = 1 )
print ( "" )
print ( "Valor da Média das Variáveis" )
print ( "GEN REP Var1 Var2 Var3 Var4 Var5" )
print ( "___________________________________________________" )
print ( mat_concat )
print ( "___________________________________________________" )
do  matplotlib  import  pyplot  como  plt
importação  os
plt . estilo . use ( 'ggplot' )
fig  =  plt . figure ( 'Média dos genótipos para cada variável' )
plt . subparcela ( 2 , 3 , 1 )
plt . barra ( mat_concat [:, 0 ], mat_concat [:, 1 ], largura = 0,8 , cor = "guia: verde" )
plt . title ( 'Variável 1' )
plt . ylabel ( 'Valor médio' )
plt . xlabel ( 'Genótipo' )
plt . subparcela ( 2 , 3 , 2 )
plt . barra ( mat_concat [:, 0 ], mat_concat [:, 2 ], largura = 0.8 , color = "tab: red" )
plt . title ( 'Variável 2' )
plt . ylabel ( 'Valor médio' )
plt . xlabel ( 'Genótipo' )
plt . subparcela ( 2 , 3 , 3 )
plt . barra ( mat_concat [:, 0 ], mat_concat [:, 3 ], largura = 0,8 , cor = "guia: azul" )
plt . title ( 'Variável 3' )
plt . ylabel ( 'Valor médio' )
plt . xlabel ( 'Genótipo' )
plt . subparcela ( 2 , 3 , 4 )
plt . barra ( mat_concat [:, 0 ], mat_concat [:, 4 ], largura = 0.8 , color = "tab: pink" )
plt . title ( 'Variável 4' )
plt . ylabel ( 'Valor médio' )
plt . xlabel ( 'Genótipo' )
plt . subparcela ( 2 , 3 , 5 )
plt . barra ( mat_concat [:, 0 ], mat_concat [:, 5 ], largura = 0.8 , color = "tab: purple" )
plt . title ( 'Variável 5' )
plt . ylabel ( 'Valor médio' )
plt . xlabel ( 'Genótipo' )
print ( "Dispersão 2D de mídias dos genótipos (use as três primeiras variáveis)."
      "No eixo X uma variável e no eixo Y outra." )
cores  = [ 'preto' , 'azul' , 'vermelho' , 'verde' , 'amarelo' , 'rosa' , 'ciano' , 'laranja' , 'darkviolet' , 'slategray' ]
plt . estilo . use ( 'ggplot' )
plt . estilo . use ( 'ggplot' )
fig  =  plt . figure ( 'Dispersão 2D das mídias' )
nl_4 , nc_4 = mat_concat . forma
plt . subparcela ( 1 , 3 , 1 )
cores  = [ 'preto' , 'azul' , 'vermelho' , 'verde' , 'amarelo' , 'rosa' , 'ciano' , 'laranja' , 'darkviolet' , 'slategray' ]
# https://matplotlib.org/3.1.0/gallery/color/named_colors.html
para  i  no  np . arange ( 0 , nl_4 , 1 ):
    plt . dispersão ( mat_concat [ i , 1 ], mat_concat [ i , 2 ], s = 50 , alfa = 0,8 , label  =  mat_concat [ i , 0 ], c  =  núcleos [ i ])
plt . title ( 'Dispersão' )
plt . xlabel ( 'Var 1' )
plt . ylabel ( «Var 2» )
plt . legenda ()
plt . subparcela ( 1 , 3 , 2 )
para  i  no  np . arange ( 0 , nl_4 , 1 ):
    plt . dispersão ( mat_concat [ i , 1 ], mat_concat [ i , 3 ], s = 50 , alfa = 0,8 , label  =  mat_concat [ i , 0 ], c  =  núcleos [ i ])
plt . title ( 'Dispersão' )
plt . xlabel ( 'Var 1' )
plt . rótulo de identificação ( «Var 3» )
plt . legenda ()
plt . subparcela ( 1 , 3 , 3 )
para  i  no  np . arange ( 0 , nl_4 , 1 ):
    plt . dispersão ( mat_concat [ i , 2 ], mat_concat [ i , 3 ], s = 50 , alfa = 0,8 , label  =  mat_concat [ i , 0 ], c  =  núcleos [ i ])
plt . title ( 'Dispersão' )
plt . xlabel ( 'Var 2' )
plt . rótulo de identificação ( «Var 3» )
plt . legenda ()
plt . show ()

#Salvar grafico
#nome = 'dispersao2D'
# fig.savefig ((nome + '. png'), bbox_inches = "tight")
# os.startfile (nome + '. png')

