from random import randrange as rrange

def imprimir_mensagem_abertura():
  print("********************************")
  print("***Bem vindo ao jogo da forca***")
  print("********************************")

def carregar_palavra_secreta():
  palavras = []
  with open('palavras.txt', 'r') as arquivo:
    for linha in arquivo:
      linha = linha.strip()
      palavras.append(linha)

  arquivo.close()

  numero = rrange(0, len(palavras))

  palavra_secreta = palavras[numero].lower()

  return palavra_secreta


def jogar():
  imprimir_mensagem_abertura()

  palavra_secreta = carregar_palavra_secreta()

  acertou = False
  enforcou = False
  letras_acertadas = ["_" for letra in palavra_secreta]
  erros = 0

  print( 'Encontre a palavra com {} letras'.format(len(palavra_secreta)) )
  print(letras_acertadas)
  while(not acertou and not enforcou):
    chute = input('Qual a letra? ').strip().lower()

    if(chute in palavra_secreta):
      posicao = 0  
      for letra in palavra_secreta:
        if(chute == letra):
          letras_acertadas[posicao] = letra
          print('Letra encontrada na posição ', (posicao + 1))  
        
        posicao += 1
    else:
      erros += 1  
    
    acertou = '_' not in letras_acertadas
    enforcou = erros == 6

    print(letras_acertadas)
    print('Jogando')

  if(acertou):
    print('Você ganhou')
  else:
    print('Você perdeu, a palavra secreta é ', palavra_secreta)
  print('Fim do Jogo')

jogar()