from datetime import date
atual = date.today().year
ano = int(input('digite o ano em que você nasceu: '))
idade = atual - ano
if  idade < 18:
    print('Ainda não esta na hora de você se alistar, mas se prepare pois esta chegando')
elif idade == 18:
    print('Já esta na hora de você se alistar')
elif idade > 20: 
    print('Já passou muito da hora de você se alistar!!')
else:
    print('Boa Vida!!')