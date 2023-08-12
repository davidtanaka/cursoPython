jogadores = list()
dados = dict()
gols = list()
while True:
    dados['Nome'] = input('\033[1;97mNome do(a) jogador(a): ').strip().title()
    partidas = int(input(f'Quantas patidas {dados["Nome"]} jogou? '))
    for p in range(partidas):
        gols.append(int(input(f'Quantos gols marcou na {p+1}° partida? ')))
    dados['Gols'] = gols[:]
    dados['Total'] = sum(gols)
    jogadores.append(dados.copy())
    dados.clear()
    gols.clear()
    while True:
        continuar = input('\033[1;97mQuer continuar [S/N]? ').upper().strip()
        if continuar == 'S' or continuar == 'N':
            break
        print('\033[1;31mRESPOSTA INVÁLIDA!')
    print(60*'\033[1;97m-')
    if continuar == 'N':
        print('\033[1;32mJOGADORES CADASTRADOS'.center(60))
        c = 0
        for jogador in jogadores:
            c += 1
            espaco = 12 - len(jogador["Nome"])
            print(f'\033[1;97mN°{c}   Nome: {jogador["Nome"]}', end=espaco*' ')
            print(f'Gols: {jogador["Gols"]}', end=espaco*' ')
            print(f'Total: {jogador["Total"]}')
        break
while True:
    mostrar = int(input('\033[1;97mMostrar dados de qual jogador (digite 999 p/ encerrar)? '))
    if mostrar == 999:
        print('\033[1;33m==================>PROGRAMA ENCERRADO<======================')
        break
    elif mostrar > len(jogadores) or mostrar <= 0:
        print('\033[1;31mRESPOSTA INVÁLIDA!')
    else:
        print(60 * '\033[1;97m-')
        print('\033[1;34m ', end='')
        print(f'=====>LEVANTAMENTO DO JOGADOR(A) {jogadores[mostrar-1]["Nome"]}<====='.upper())
        for jogador in jogadores:
            if jogador == jogadores[mostrar-1]:
                for p, gol in enumerate(jogador['Gols']):
                    print(f'\033[1;97mNo {p + 1}° jogo fez {gol} gol(s)')
    print(60*'\033[1;97m-')




# dados = dict()
# gols = list()
# aproveitamento = dict()
# total_gols = totA = 0
# while True:
#     dados['nome'] = str(input('Nome do jogador: '))
#     dados['partidas jogadas'] = int(input(f'Quantas partidas {dados["nome"]} jogou? # '))
#     for c in range(0, dados['partidas jogadas']):
#         gols.append(int(input(f'Quantos gols na partida {c+1}? ')))
 #        total_gols += gols[c]
 #        dados['gols'] = gols.copy()
 #        dados['total'] = total_gols
 #    continuar = str(input('Vovê quer continuar? [S/N]')).strip().upper()
 #    if continuar in 'N':
 #        break
# totA = dados['gols'] 
# for c in range(0, dados['partidas jogadas']):
#     dados['gols'] = aproveitamento.copy()
#     if aproveitamento['gols'] >= totA:
#         totA = aproveitamento
# print('-'*59)
# for k, v in dados.items():
#     print(f'{k}: {v}')
# print('-'*59)
# print(dados)
# print('-'*59)
# print(f'O jogador {dados["nome"]} jogou {dados["partidas jogadas"]}.')
# for k, v in enumerate(dados["gols"]):
#     print(f'   => Na partida {k+1}, fez {v} gols.')
# print(f'Foi um total de {dados["total"]} gols.')
# print('-=' * 35)
# print(f'O melhor aproveitamento foi de: {totA}')