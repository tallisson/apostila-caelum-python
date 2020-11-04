from pessoa import Pessoa

if (__name__ == '__main__'):
  p = Pessoa()
  p1 = Pessoa()
  p.nome = 'Thiago Allisson Ribeiro da Silva'
  p.idade = 30

  print(p)
  print(Pessoa.get_total_contas())
