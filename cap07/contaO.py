from historico import Historico

class Conta:
  def __init__(self, numero, cliente, saldo, limite = 10.0):
    print('inicializando a conta')
    self.numero = numero
    self.cliente = cliente
    self.saldo = saldo
    self.limite = limite
    self.historico = Historico()

  def dict(self):
    return dict(
      numero = self.numero,
      cliente = self.cliente.toString(),
      saldo = self.saldo
    )
  
  def deposita(self, valor):
    self.saldo += valor
    self.historico.transacoes.append("depósito de {}".format(valor))

  def saca(self, valor):
    if(self.saldo < valor):
      return False
    else:
      self.saldo -= valor
      self.historico.transacoes.append("saque	de {}".format(valor))
      return True
  
  def extrato(self):
    print("numero:	{}	\nsaldo:	{}".format(self.numero,	self.saldo))
    print(self.historico.toString())

  def transfere(self, destino, valor):
    if(self.saca(valor)):
      destino.deposita(valor)
      self.historico.transacoes.append("transferencia	de {} para	conta	{}".format(valor,	destino.numero))
      return True
    else:
      return False