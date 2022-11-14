from defs.categorias import categorias


def inicio():
    print('-' * 70)
    print('UNIESP'.center(70))
    print('INTRODUÇÃO À PROGRAMAÇÃO'.center(70))
    print('-' * 70)
    print(''' Grupo:                                                     
              Diego Moura Araújo - 2022211510093@iesp.edu.br
              Gessica Gomes de Melo - 2022211510030@iesp.edu.br
              Leiliane Silva de Morais - 2022211510005@iesp.edu.br
              Letícia Leite Batista da Silva - 2022211510082@iesp.edu.br  
              Paula Mota Gomes - 2022211510027@iesp.edu.br
              Thais Paiva Madruga - 2022211510053@iesp.edu.br''')
    print('-' * 70)
    print('JOGO DA FORCA'.center(70))
    print('-' * 70)
    print('''Categorias:
                [1] Frutas                                           
                [2] Cores                                           
                [3] Sair''')
    print('-' * 70)


def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            categorias.limpar()
            print('\u001b[31mErro: Digite uma opção válida.\u001b[m')
            inicio()
            continue
        else:
            return n
