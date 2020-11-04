class Pessoa:
  _total_pessoas = 0
  __slots__	=	['_nome',	'_idade']

  def __init__(self, nome = '', idade = 0):
    self._nome = nome
    self._idade = idade
    Pessoa._total_pessoas += 1

  @property
  def nome(self):
    return self._nome
  @nome.setter
  def nome(self, nome):
    self._nome = nome

  @property
  def idade(self):
    return self._idade
  @idade.setter
  def idade(self, idade):
    self._idade = idade

  def __str__(self):
    return '[ nome = {} e idade = {} ]'.format(self._nome, self._idade)

  @staticmethod
  def get_total_contas():
    return Pessoa._total_pessoas