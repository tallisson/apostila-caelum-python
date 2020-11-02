def velocidade_media(distancia, tempo):
  velocidade = distancia / tempo
  return velocidade

def soma(x, y):
  return x + y

def sub(x, y):
  return x - y

def mult(x, y):
  return x * y

def div(x, y):
  return x / y

def calculadora(x, y):
  return { 
    'soma': soma(x, y), 'sub': sub(x, y),
    'mult': mult(x, y), 'div': div(x, y)
  }


print(calculadora(10, 2))