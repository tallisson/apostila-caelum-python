from myException import MyException as MEx

def div(x, y):
  try:
    if(y == 0):
      raise MEx()
  except MEx as error:
    print(error)
  else:
    print('O resultado é {}'.format(x/y))    

if __name__ == '__main__':
  div(2, 1)