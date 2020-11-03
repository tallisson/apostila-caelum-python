def exercicio01():
  arquivo = open('palavras.txt', 'a')

  arquivo.write('banana\n')
  arquivo.write('melancia\n')
  arquivo.write('morango\n')
  arquivo.write('manga')

  arquivo.close()

exercicio01()