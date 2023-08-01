from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 7 + 1):
    nasc = int(input('Digite o Ano em que você nasceu: '))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
        
        
print('ao todo tivemos {} pessoas MAIOR de idade '.format(totmaior))
print('ao todo tivemos {} pessoas MENOR de idade '.format(totmenor))