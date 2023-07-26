nome = str(input('digite seu nome:')).strip()

print("seu nome em letras maiusculas fica: {}".format(nome.upper()))
print("seu nome eem letras minusculas fica: {}".format(nome.lower()))
print("Seu nome é {} e tem {} letras".format(nome, len(nome)-nome.count(' ')))
print("aqui está apenas o seu primeiro nome é: {}".format(nome.find(' ')))