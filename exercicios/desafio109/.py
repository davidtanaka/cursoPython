import coin
x = float(input('Type a value: '))
y = float(input('Type a rate (in %): '))
answer = str(input(f'Do you want your value formatted ({coin.cl["b"]}Y{coin.cl["limit"]}/ {coin.cl["r"]}N{coin.cl["limit"]})? ')).title()[0]
if answer == 'Y':
    ft = True
else:
    ft = False
print(f'Increase of {coin.coin(x)} = {coin.increase(x, y, ft)}')
print(f'Decrease of {coin.coin(x)} = {coin.decrease(x, y, ft)}')
print(f'Half of {coin.coin(x)} = {coin.half(x, ft)}')
print(f'Double of {coin.coin(x)} = {coin.double(x, ft)}')