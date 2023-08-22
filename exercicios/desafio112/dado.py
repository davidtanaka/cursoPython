def leiaDinheiro(msg):
    while True:
        num = input(msg).strip().replace(',', '.')
        if num.replace('.', '').isnumeric():
            return float(num)
        else:
            print('\033[31mERRO: "num" é um preço inválido\033[m')