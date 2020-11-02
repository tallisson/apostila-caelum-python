#!/usr/bin/python
import random as rnd

print("**************")
print("* Advinhação *")
print("**************")

numero_secreto = rnd.randint(1, 100)

print('Escolha seu nível:')
print('1- 20 tentativas')
print('2- 10 tentativas')
print('3- 05 tentativas')
nivel = int( input() )

numero_rodadas = 20
if(nivel == 2):
  numero_rodadas = 10
elif(nivel == 3):
  numero_rodadas = 5

acertou = False
i = 0
total_pontos = 1000

while (i < numero_rodadas):
  print('Rodada ', i+1)
  print('Sua pontuação é: ', total_pontos)
  chute = int( input('Digite um número entre 1 e 100: ') )

  if(chute == numero_secreto):
    acertou = True
    print('Você acertou na rodada {}. Parabéns!!!'.format(i+1))
    break
  elif(chute > numero_secreto):    
    print('Tente um número menor')
  else:
    print('Tente um número maior')
  total_pontos = total_pontos - abs(chute - numero_secreto)

  i = i + 1

if(acertou == False):
  print('O número secreto é ', numero_secreto)

print('Bye!');