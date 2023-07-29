anoAtual = 2023
ano = int(input('digite o ano em que você nasceu: '))

if  anoAtual - ano <= 17:
    print('Ainda não esta na hora de você se alistar, mas se prepare pois esta chegando')
elif anoAtual - ano > 18 <= 19:
    print('Já esta na hora de você se alistar')
elif anoAtual - ano > 20: 
    print('Já passou muito da hora de você se alistar!!')
else:
    print('Boa Vida!!')