from datetime import date
def voto(ano):
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com idade  {idade} NÃO VOTA'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} O VOTO NÃO É OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATORIO'

nasc =  int(input('Em que ano você nasceu? '))
print(voto(nasc))