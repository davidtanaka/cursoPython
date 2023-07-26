from datetime import date

ano = int(input('digite o ano em que voce esta: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('esse é um ano bisexto')
else:
    print("esse ano não é bisexto")