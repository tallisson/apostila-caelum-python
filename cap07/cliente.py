class Cliente:
  def __init__(self, nome, sobrenome, cpf):
    self.nome = nome
    self.sobrenome = sobrenome
    self.cpf = cpf

  def toString(self):
    return dict(
      nome = self.nome,
      sobrenome = self.sobrenome,
      cpf = self.cpf
    )