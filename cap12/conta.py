from historico import Historico 
from saldo_insuficiente import SaldoInsuficienteError

class Conta:
  def __init__(self, numero, cliente, saldo, limite = 10.0):
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
    if(valor < 0):
      raise ValueError('Você tentou depositar um valor inválido')
    else:
      self.saldo += valor
      self.historico.transacoes.append("depósito de {}".format(valor))

  def saca(self, valor):
    if(valor < 0):
      raise ValueError('Você tentou depositar um valor inválido')
    
    if(self.saldo < valor):
      raise SaldoInsuficienteError()
    else:
      self.saldo -= valor
      self.historico.transacoes.append("saque	de {}".format(valor))
  
  def extrato(self):
    print("numero:	{}	\nsaldo:	{}".format(self.numero,	self.saldo))
    print(self.historico.toString())

  def transfere(self, destino, valor):
    self.saca(valor)
    destino.deposita(valor)
    self.historico.transacoes.append("transferencia	de {} para	conta	{}".format(valor,	destino.numero))