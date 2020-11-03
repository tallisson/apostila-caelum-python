from contaO import Conta
from cliente import Cliente

cliente = Cliente('José', 'Mota', '123456789-10')

c = Conta('123-4', cliente, 10000, 20000)
c.saca(1000)

c.extrato()
print(c.dict())