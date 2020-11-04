class Conta:
  _total_contas = 0
  __slots__ = ['_id', '_numero', '_titular', '_saldo', '_limite']

  def __init__(self, numero, titular, saldo, limite = 10.0):
    self._numero = numero
    self._titular = titular
    self._saldo = saldo
    self._limite = limite
    Conta._total_contas += 1
    self._id = Conta._total_contas

  @property
  def id(self):
    return self._id
  
  @property
  def numero(self):
    return self._numero
  
  @property
  def titular(self):
    return self._titular

  @property
  def saldo(self):
    return self._saldo
  
  @property
  def limite(self):
    return self._limite
  @limite.setter
  def limite(self, limite):
    self._limite = limite

  def __str__(self):
    return dict(
      id = self._id,
      numero = self._numero,
      titular = self._titular,
      saldo = self._saldo
    ).__str__()
  
  def deposita(self, valor):
    if(valor < 0):
      raise ValueError('Você tentou depositar um valor inválido')
    else:
      self._saldo += valor

  def saca(self, valor):
    if(valor < 0):
      raise ValueError('Você tentou depositar um valor inválido')
    
    if(self._saldo < valor):
      raise ValueError('Saldo insuficiente')
    else:
      self._saldo -= valor
  
  def extrato(self):
    print("numero:	{}	\nsaldo:	{}".format(self._numero,	self._saldo))

  def transfere(self, destino, valor):
    self.saca(valor)
    destino.deposita(valor)

  @staticmethod
  def get_total_contas():
    return Conta._total_contas