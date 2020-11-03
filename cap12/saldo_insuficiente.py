class SaldoInsuficienteError(RuntimeError):
  def __init__(self, message = ''):
    if(message != ''):
      self.message = message
    else:
      self.message = 'Saldo insuficiente'
  
  def __str__(self):
    return self.message