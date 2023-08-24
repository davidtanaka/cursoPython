from exercicios.desafio115.lib.arquivo import *
from time import sleep

arq = 'Cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar novas pessoas', 'Sair do sistema'])
    if resposta == 1:
        # opção de listar o conteudo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
       cabecalho('NOVO CADASTRO')
       nome = str(input('nome: '))
       idade = leiaInt('Idade: ')
       cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema, até logo....')
        break
    else:
        print('\033[31mErro digite uma opção valida\033[m')
    sleep(2)
