from datetime import datetime as dt

class Historico:
  def __init__(self):
    self.data_abertura = dt.today()
    self.transacoes = []

  def toString(self):
    print('Data de abertura: ', self.data_abertura)
    print('Transações: ')
    for t in self.transacoes:
      print('-', t)