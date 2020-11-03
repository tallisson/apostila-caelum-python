print("********************************")
print("***Bem vindo ao jogo da forca***")
print("********************************")

palavra_secreta = "banana"

acertou = False
enforcou = False
letras_acertadas = []
for i in range(0, len(palavra_secreta)):
  letras_acertadas.append('_')
erros = 0

print( 'Encontre a palavra com {} letras'.format(len(palavra_secreta)) )
print(letras_acertadas)
while(not acertou and not enforcou):
  chute = input('Qual a letra? ')

  if(chute in palavra_secreta):
    posicao = 0  
    for letra in palavra_secreta:
      if(chute.upper() == letra.upper()):
        letras_acertadas[posicao] = letra
        print('Letra encontrada na posição ', (posicao + 1))  
      
      posicao += 1
  else:
    erros += 1  
  
  acertou = '_' not in letras_acertadas
  enforcou = erros == 6

  print(letras_acertadas)
  print('Jogando')


print('Fim do Jogo')
if(acertou):
  print('Você ganhou')
else:
  print('Você perdeu')