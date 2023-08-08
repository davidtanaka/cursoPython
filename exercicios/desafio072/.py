contagem = ('Zero', 'Um', 'Dois', 'Trez', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Desessete', 'Dezoito', 'Dezenove', 'Vinte')
num = int(input('Digite um numero: '))
while num > 20 or num < 0:
    num = int(input('Digite um numero: (entre 0 e 20)'))
print(f'Você digitou o numero {contagem[num]}')