def exercicio01():
  lista = [12,	-2,	4,	8,	29,	45,	78,	36,	-17,	2,	12,	8,	3,	3,	-52]

  maior = max(lista)
  menor = min(lista)
  print('Maior = {} e menor = {}'.format(maior, menor))

  print('Numeros pares')
  for item in lista:
    if(item % 2 == 0):
      print(item)

  print('Numero de ocorrências do 1º elemento da lista:')
  print(lista.count(lista[0]))

  print('Media dos elmentos')
  soma = 0
  for item in lista:
    soma += item

  print(soma/len(lista))

  print('Soma dos elementos negativos')
  soma = 0
  for item in lista:
    if(item < 0):
      soma += item
  print(soma)

def exercicio02():
  nome = input('Digite seu nome: ')
  sobrenome = input('Digite seu sobrenome: ')
  idade = int( input('Digite sua idade: ') )

  lista = (nome, sobrenome, idade)

  print(lista)

def exercicio03():
  lista = []

  soma = 0
  for i in range(1, 5):
    nota = float( input( 'Digite a nota {}: '.format(i) ) )
    soma += nota
    lista.append(nota)

  media = soma / len(lista)

  print('Notas: ', lista)
  print('A média é ', media)

def exercicio04():  
  pessoas = []

  inserir = True
  while(inserir):
    nome = input('Digite seu nome: ')
    cidade = input('Digite sua cidade: ')
    idade = int( input('Digite sua idade: ') )

    pessoa = dict(nome=nome, cidade=cidade, idade=idade)
    print(pessoa)

    pessoas.append(pessoa)

    inserir = input('Deseja inserir outra pessoa? Y/N ').lower() == 'y'
  
  print('Pessoas: ', pessoas)

exercicio04()