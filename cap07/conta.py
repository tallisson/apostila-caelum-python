# arquivo para criar e gerenciar contas

# criar_conta: função para criar contas
def criar_conta():
  conta = dict(
    numero = input('Número: '),
    titular = input('Titular: '),
    saldo = float( input('Saldo: ') ),
    limite = float( input('Limite: ') )
  )
  return conta

# função para depositar valor ao saldo de uma conta
# @param conta: dados da conta [dict]
# @param valor: valor a ser depositado [float]
def deposita(conta, valor):
  conta['saldo'] += valor

def saca(conta, valor):
  conta['saldo'] -= valor

def extrato(conta):
  print(conta)