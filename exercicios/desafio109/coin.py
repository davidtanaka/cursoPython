cl = {'r': '\033[31m', 'g': '\033[32m', 'w': '\033[33m', 'b': '\033[34m', 'limit': '\033[m'}


def increase(param=0, rate=0, format=False):
    inv = param * (1 + rate / 100)
    return f'{inv:.2f}' if format is False else coin(inv)


def decrease(param=0, rate=0, format=False):
    dev = param * (1 - rate / 100)
    return f'{dev:.2f}' if format is False else coin(dev)


def double(param=0, format=False):
    db = param * 2
    return f'{db:.2f}' if format is False else coin(db)


def half(param=0, format=False):
    hal = param / 2
    return f'{hal:.2f}' if format is False else coin(hal)


def coin(param=0, coin='R$'):
    return f'{cl["g"]}{coin}{cl["limit"]}{param:.2f}'