from random import randint 
maior = menor = 0
aleatorio = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print(f'Os numeros sorteados foram {aleatorio}')
print(f'O maior numero sorteado foi: {max(aleatorio)}')
print(f'O menor numero sorteado foi {min(aleatorio)}')

#if aleatorio[0] > aleatorio[1]:
#    maior = aleatorio[0]
#elif aleatorio[1] > aleatorio[0]:
 #   maior = aleatorio[1]
#if aleatorio[0] > aleatorio[2]:
#    maior = aleatorio[0]
#elif aleatorio[2] > aleatorio[0]:
#    maior = aleatorio[2]
#elif aleatorio[0] > aleatorio[3]:
#    maior = aleatorio[0]
#elif aleatorio[3] > aleatorio[0]:
#    maior = aleatorio[3]
#elif aleatorio[0] > aleatorio[4]:
#    maior = aleatorio[0]
#elif aleatorio[4] > aleatorio[0]:
#    maior = aleatorio[4]
#elif aleatorio[0] > aleatorio[5]:
#    maior = aleatorio[0]
#    maior = aleatorio[5]
    
#if aleatorio[0] < aleatorio[1]:#
 #   menor = aleatorio[0]
#elif aleatorio[1] < aleatorio[0]:#
   # menor = aleatorio[1]
#if aleatorio[0] < aleatorio[2]:#
   # menor = aleatorio[0]
#elif aleatorio[2] < aleatorio[0]:#
   # menor = aleatorio[2]
#elif aleatorio[0] < aleatorio[3]:#
  #  menor = aleatorio[0]
#elif aleatorio[3] < aleatorio[0]:#
  #  menor = aleatorio[3]
#elif aleatorio[0] < aleatorio[4]:#
   # menor = aleatorio[0]
#elif aleatorio[4] < aleatorio[0]:#
   # menor = aleatorio[4]
#elif aleatorio[0] < aleatorio[5]:#
 #   menor = aleatorio[0]
#elif aleatorio[5] < aleatorio[0]:#
  #  menor = aleatorio[5]