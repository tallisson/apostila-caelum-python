from conta import Conta
from cliente import Cliente

cliente = Cliente('Thiago', 'Ribeiro', '123456789-10')

conta = Conta('123-4', cliente, 10000, 20000)
print(conta)

try:
  conta.saca(100000)
except Exception as error:
  print(error)