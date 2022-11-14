from time import sleep
from defs.categorias import categorias
from defs.interface import menu
# Para a função limpar() funcionar no PyCharm, vá em Run > Edit Configurations.
# Na tela de Run/Debug Configurations, clique em + > Python, no canto superior esquerdo.
# Em 'script path', procure o local do arquivo principal do jogo.
# Em Execution, marque a opção 'Emulate terminal in output console' e clique em apply e ok.
opcao = 0
while opcao != 3:
    menu.inicio()
    opcao = menu.leiaint('Digite uma opção: ')
    if opcao == 1:
        categorias.fruta()
    elif opcao == 2:
        categorias.cor()
    elif opcao == 3:
        categorias.limpar()
        print('Encerrando jogo...')
        sleep(2)
    else:
        categorias.limpar()
        print('Opção inválida. Tente novamente!')
print('Jogo encerrado.')
