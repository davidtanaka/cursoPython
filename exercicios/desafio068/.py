from random import randint
print('Vamos jogar par ou impar...')

computador = jogador = ganhou = PouI = 0
computador = randint(0, 11)
soma = jogador + computador
Jganhou = True
Cganhou = False
totj = 0
while Jganhou == True:
    jogador = int(input('qual numero você quer:  '))
    PouI = str(input(f'Você quer par ou impar? [P/I]: ')).strip().upper()
    while PouI not in 'PI':
        PouI = str(input(f'Você quer par ou impar? [P/I]: ')).strip().upper()
    computador = randint(0, 10)
    soma = jogador + computador
    if PouI == 'P':
        PouI = 'P'
    else:
        PouI = 'I'

    if soma % 2 == 0 and PouI == 'P':
            ganhou = jogador
            Jganhou = True
            Cganhou = False
            totj += 1
            print(f'Parabens!! Você pensou no numero {jogador} e o Computador no numero {computador} E a soma dos numeros fica {soma} Que é PAR você ganhou')
    elif soma % 2 == 1 and PouI =='P':
        totj += 1
        ganhou = computador
        Jganhou = False
        Cganhou = True
        print(f'Você perdeu, a soma dos numeros ficou {soma} e é impar, você jogou {totj} vezes')
        break
    if soma % 2 == 1 and PouI == 'I':
            ganhou = jogador 
            Jganhou = True 
            Cganhou = False
            totj += 1
            print(f'Parabens!! Você pensou no numero {jogador} e o Computador no numero {computador} E a soma dos numeros fica {soma} Que é IMPAR você ganhou')
        
    elif soma % 2 == 0 and PouI =='I':
        ganhou = jogador 
        Jganhou = True
        Cganhou = False
        totj += 1
        print(f'Você perdeu, a soma dos numeros ficou {soma} e é par, você jogou {totj} vezes')
        break
    elif Cganhou == True and Jganhou == False:
            Cganhou = True
            Jganhou = False
            print(f'Você perdeu o numero {soma} é Impar então você perdeu')
            break
print(f'Fim de programa, Volte sempre')
