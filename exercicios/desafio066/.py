n = s = v = 0

while True:
    n = int(input('Digite um numero: (999 para parar)'))
    if n == 999:
        break
    v += 1
    s += n
print(f'Foram digitados {v} E a soma vale {s}')