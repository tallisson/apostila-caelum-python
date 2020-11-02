#!/usr/bin/python
import random as rnd

print("**************")
print("* Advinhação *")
print("**************")

numero_secreto = rnd.randint(1, 100)
numero_rodadas = 5
acertou = False

for i in range(0, 5):
  print('Rodada ', i+1)
  chute = int( input('Digite um número entre 1 e 100: ') )

  if(chute == numero_secreto):
    acertou = True
    print('Você acertou na rodada {}. Parabéns!!!'.format(i+1))
    break
  elif(chute > numero_secreto):
    print('Tente um número menor')
  else:
    print('Tente um número maior')

if(acertou == False):
  print('O número secreto é ', numero_secreto)

print('Bye!');