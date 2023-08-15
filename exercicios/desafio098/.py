from time import sleep
def linhas():
    print('-=' * 15)
    
    
def contador(inicio, fim, passo):
     for c in range(inicio, fim, passo):
        print(c)
        sleep(0.5)
        if passo == 0:
            passo = 1
    

linhas()
print('Contagem de 1 até 10 de 1 em 1')
linhas()
for c in range(1, 10, 1):
    print(c)
    sleep(0.5)
linhas()
print('Contagem de 10 até 0 de 2 em 2')
linhas()
for c in range(10, 0, -2):
    print(c)
    sleep(0.5)
linhas()
i = int(input('Inicio: '))
f = int(input('Fim: ') + 1)
p = int(input('De quanto em quanto? '))
linhas()
print(f'Iniciando contagem do {i} ao {f} de {p} em {p}')
linhas()
contador(i, f, p)
