def notas(*n, sit=False, tab=False):
    """
    -> Função para analisar funções e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias).
    :param sit: opcional, indica se deve ou não adicionar a situação da turma.
    :param tab: opcional, indica se deve ou não mostrar os dados em forma de tabela.
    :return: dicionário e/ou tabela com os dados solicitados.
    """
    dados = {}
    total = maior = menor = soma = 0
    s = ''
    for i in n:# laço para obter: total, maior, menor e soma
        soma += i
        total += 1
        if i == n[0]:
            maior = i
            menor = i
        else:
            if i > maior:
                maior = i
            if i < menor:
                menor = i
    media = soma / total# cálculo da média das notas
    if media < 5:# classificação da situação de acordo com a média de notas.
        s = 'RUIM'
    if 5 <= media < 7:
        s = 'RAZOÁVEL'
    if media > 7:
        s = 'BOA'
    dados['total'] = total
    dados['maior'] = maior
    dados['menor'] = menor
    dados['média'] = media
    if sit == True:# opção caso desejar mostrar a situação da sala, de acordo com a média.
        dados['situação'] = s
    if tab == True:# opção caso desejar mostrar os dados em forma de tabela.
        if sit == True:
            print()
            print('=' * 50)
            print(f'\033[1;34;43m{"ALUNOS DA SALA (NOTAS)":^50}\033[m')
            print('=' * 50)
            print(f'{"Total":<10}{"Maior":<10}{"Menor":<10}{"Média":<10}{"Situação":<12}')
            print('-' * 50)
            print(f'{dados["total"]:<10}{dados["maior"]:<10}{dados["menor"]:<10}{dados["média"]:<10.3f}{dados["situação"]:<12}')
            print()
        else:
            print()
            print('=' * 37)
            print(f'\033[1;34;43m{"ALUNOS DA SALA (NOTAS)":^37}\033[m')
            print('=' * 37)
            print(f'{"Total":<10}{"Maior":<10}{"Menor":<10}{"Média":<10}')
            print('-' * 37)
            print(f'{dados["total"]:<10}{dados["maior"]:<10}{dados["menor"]:<10}{dados["média"]:<10.3f}')
            print()

