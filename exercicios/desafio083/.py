expr = str(input('Digite a sua expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.appen(')')
            break
if len(pilha) == 0:
    print('Sua expressão está VALIDA')
else:
    print('Sua expressão não é VALIDA(INVALIDA)')