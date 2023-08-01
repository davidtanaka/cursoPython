frase = str(input('Digite uma frase: ')).strip().upper
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('o inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('temos um palindromo')
else:
    print('não temos um palindromo')
    