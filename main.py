dicionario = {12345:["Caio", "Aluno"]}

def exibir():
  for chave,lista in dicionario.items():
    print("Cod. do funcionario...", chave)
    print("Nome...", lista[0])
    print("Cargo...", lista[1])
