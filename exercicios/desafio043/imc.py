peso = float(input('digite o seu peso: '))
altura = float(input('digite a sua altura: '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('abaixo do peso o seu peso é de: {}'.format(imc))
elif imc > 18.5 < 25:
    print('Peso ideal o seu peso é de {}'.format(imc))
elif imc > 25 <= 30:
    print('sobrepeso o seu peso é de {}'.format(imc))
elif imc > 30 < 40:
    print('obesidade o seu peso é de {}'.format(imc))
elif imc >= 40:
    print('obesidade morbida o seu peso é de {}'.format(imc))