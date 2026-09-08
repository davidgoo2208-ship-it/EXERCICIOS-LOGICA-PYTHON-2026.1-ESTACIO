nome= ' Ju ve n a l d o' + ' flo ren tin o   '
nome= "".join(nome.split()) 
# Explicação: O código '' e "" Servem pra criar uma string, o código . é usado para acessar métodos e atributos de objetos, a função join() é um método que junta elementos de uma lista em uma única string
# E a função split() é um método que divide uma string em uma lista de substrings com base em um delimitador (por padrão, espaços em branco).


import re
partes= re.findall(r'[A-Z][a-z]*', nome)
nome_corrigido= " ".join(partes)

print(nome_corrigido)
# Explicação: A função import serve para importar módulos e bibliotecas em Python, a função re serve para trabalhar com expressões regulares 
# O código * serve como operador de multiplicação ou para repetir sequências (o que é o caso nessa situação) e o código " " é usado nessa situação para definir que são os espaços em branco que devem ser corrigidos


# Métodos nativos para manipulação de strings
# capitalize(), lower(), upper(), title(), strip(), replace(), split(), join()
# Explicação: capitalize() converte o primeiro caractere de uma string para maiúscula e os demais para minúsculas, lower() converte todos os caracteres de uma string para minúsculas
# upper() converte todos os caracteres de uma string para maiúsculas, title() converte o primeiro caractere de cada palavra para maiúscula e os demais para minúsculas
# strip() remove espaços em branco do ínicio e do fim da string, replace() substitui todas as ocorrências de uma substring por outra
# split() divide uma string em uma lista de substrings com base em um delimitador e join() junta elementos de uma lista em uma única string


# Essas três aspas (''') servem para criar strings multilinhas ou comentários de bloco (docstrings)
'''
Manipulação de maiúsculas e minúsculas

.lower() -> Converte para minúsculas 
#Exemplo: texto= "FLORES SÃO LEGAIS"
          resultado= texto.lower()
          print(resultado)
          Resultado: flores são legais

.upper() -> Converte para maiúsculas
#Exemplo: texto= "flores são legais"
          resultado= texto.upper()
          print(resultado)
          Resultado: FLORES SÃO LEGAIS

.capitalize() -> Deixa só a primeira letra em maiúscula
#Exemplo: texto= "fLOrEs sãO lEGAis"
          resultado= texto.capitalize()
          print(resultado)
          Resultado: Flores são legais

.title() -> Coloca a primeira letra de cada palavra em maiúscula
#Exemplo: texto= "regando flores"
          resultado= texto.title()
          print(resultado)
          Resultado: Regando Flores

.swapcase() -> Inverte maiúsculas <> minúsculas
#Exemplo: texto= "Bom dia, Flores!"
          resultado= texto.swapcase()
          print(resultado)
          Resultado: bOM DIA, fLORES!

.casefold() -> Versão mais agressiva de lower() (bom para comparações)
#Exemplo: texto= "FLORES SÃO LEGAIS"
          resultado= texto.casefold()
          print(resultado)
          Resultado: flores são legais

'''

'''
Manipulação de espaços e caracteres

.strip() -> Remove espaços/brancos do ínicio e fim
#Exemplo: texto= "   Olá, Flores!   "
          resultado= texto.strip()
          print(resultado)
          Resultado: Olá, Flores!

.lstrip() -> Remove do lado esquerdo
#Exemplo: texto= "   Olá, Flores!   "
          resultado= texto.lstrip()
          print(resultado)
          Resultado: Olá, Flores!   |

.rstrip() -> Remove do lado direito
#Exemplo: texto= "   Olá, Flores!   "
          resultado= texto.rstrip()
          print(resultado)
          Resultado: |   Olá, Flores!

.removeprefix(prefix) -> Remove prefixo (se existir)
#Exemplo: texto= "Olá, Seth!"
          resultado= texto.removeprefix("Olá, ")
          print(resultado)
          Resultado: Seth!

.removesuffix() -> Remove sufixo (se existir)
#Exemplo: texto= "flores.txt"
          resultado= texto.removesuffix(".txt")
          print(resultado)
          Resultado: flores

'''

'''
Substituição e formatação

.replace(old, new[, count]) -> Substitui partes da string
#Exemplo: texto= "Eu gosto de Flores. Flores são muito legais, e também Flores!"
          resultado= texto.replace("Flores", "Cartas" 2)
          print(resultado)
          Resultado: Eu gosto de Cartas. Cartas são muito legais, e também Flores!

.format(*args, **kwargs) -> Interpolação de valores
#Exemplo: nome= "Seth"
          idade= 16
          mensagem= "Meu nome é {0} e tenho {1} anos.".format(nome, idade)
          print(mensagem)
          Resultado: Meu nome é Seth e tenho 16 anos.

.format_map(mapping) -> Como format(), mas com dicionário direto
#Exemplo: dados= {
             "nome": "Seth",
             "idade": 16
          }
          mensagem= "Nome: {nome}, Idade: {idade}".format_map(dados)
          print(mensagem)
          Resultado: Nome: Seth, Idade: 16

.expandtabs(tabsize=8) -> Troca \t por espaços
#Exemplo: texto= "Nome:\tSeth"
          resultado= texto.expandtabs(8)
          print(resultado)
          Resultado: Nome:        Seth

.translate(table) -> Substituições baseadas em tabela (com str.maketrans)
#Exemplo: texto= "seth"
          tabela= str.maketrans("seth", "SETH")
          resultado= texto.translate(tabela)
          print(resultado)
          Resultado: SETH

'''


'variaveis string - função len'

nome= "Heitor"
print (len(nome)) 
# Explicação: A função len serve para retorna um número que representa o tamanho da string e 'nome' é a variável que essa função vai usar

'Manipulação de string'

alfabeto= "abcdefghijklmnopqrstuvwxyz"
print(alfabeto[0])
# Explicação: A função [ ] serve pra retornar um caractere específico da string, o 0 indica que esse caractere é o primeiro e 'alfabeto' é a variável que essa função vai usar

'Concatenação'

Letras= "ABDE"
print(Letras + "FGH") 
print(Letras + "F" * 5) 
print("X" + "-"*10 + "X") 
# Explicação: 'Letras' é uma variável, "ABDE" é o valor dessa variável, "FGH" é um outro valor 
# O código + vai servir para concanetar as strings em uma única string, como "ABDE" + "FGH" em "ABDEFGH", e "X" + "-"*10 + "X" em "X----------X"
# E o código * vai servir pra concanetar a string com "F" repetido 5 vezes 

'Fatiamento de string'

Cidade= "Fortaleza"
Fateada= (Cidade[0:3])
print(Fateada) 
# Explicação: 'Cidade' é uma variável, 'Fateada" é uma outra variável, o código : vai servir pra fatear uma margem específica de caracteres da String de 'cidade' e 0 e 3 representam essa margem de caracteres