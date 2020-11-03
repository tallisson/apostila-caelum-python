class MyException(Exception):
  def __init__(self):
    self.message = 'Divisão por zero'
  
  def __str__(self):
    return self.message