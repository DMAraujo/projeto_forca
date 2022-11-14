from os import system, name
from random import choice
from defs.forca import forca


def limpar():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def fruta():
    limpar()
    chances = 6
    tentativas = []
    acertos = []
    erros = []
    alfabeto = list('abcdefghijklmnopqrstuvwxyz')
    frutas = ['manga', 'banana', 'abacaxi', 'melancia', 'goiaba', 'acerola', 'jabuticaba']
    palavra = choice(frutas)
    while True:
        print('Categoria: Frutas')
        forca.desenho(chances)
        print(f'''
                Acertos: {acertos}
                Erros: {erros}
                Chances: {chances}''')
        for letra in palavra:
            if letra in tentativas:
                print(letra, end=' ')
            else:
                print('_', end=' ')
        palpite = input('\nDigite o seu palpite: ').lower()
        if palpite not in alfabeto or palpite == '':
            limpar()
            print('\u001b[31mErro: Palpite inválido. Tente novamente!\u001b[m')
            continue
        elif palpite in tentativas:
            limpar()
            print('\u001b[31mErro: Você já tentou essa letra. Tente outra!\u001b[m')
            continue
        tentativas.append(palpite)
        if palpite in palavra:
            limpar()
            print('\u001b[32mVocê acertou!\u001b[m')
            acertos.append(palpite)
        else:
            limpar()
            print('\u001b[32mVocê errou!\u001b[m')
            chances -= 1
            erros.append(palpite)
        if chances == 0:
            forca.desenho(chances)
            print(f'\u001b[32m\nQue pena, você perdeu! A resposta correta era {palavra}.\u001b[m')
            input("\u001b[32mPressione ENTER para sair...\u001b[m")
            limpar()
            break
        elif set(palavra).issubset(set(tentativas)):
            forca.desenho(chances)
            print(f'\u001b[32m\nParabéns, você ganhou! A palavra era {palavra}.\u001b[m')
            input("\u001b[32mPressione ENTER para sair...\u001b[m")
            limpar()
            break


def cor():
    limpar()
    chances = 6
    tentativas = []
    acertos = []
    erros = []
    alfabeto = list('abcdefghijklmnopqrstuvwxyz')
    cores = ['azul', 'amarelo', 'verde', 'rosa', 'vermelho', 'laranja', 'violeta']
    palavra = choice(cores)
    while True:
        print('Categoria: Cores')
        forca.desenho(chances)
        print(f'''
                    Acertos: {acertos}
                    Erros: {erros}
                    Chances: {chances}''')
        for letra in palavra:
            if letra in tentativas:
                print(letra, end=' ')
            else:
                print('_', end=' ')
        palpite = input('\nDigite o seu palpite: ').lower()
        if palpite not in alfabeto or palpite == '':
            limpar()
            print('\u001b[31mErro: Palpite inválido. Tente novamente!\u001b[m')
            continue
        elif palpite in tentativas:
            limpar()
            print('\u001b[31mErro: Você já tentou essa letra. Tente outra!\u001b[m')
            continue
        tentativas.append(palpite)
        if palpite in palavra:
            limpar()
            print('\u001b[32mVocê acertou!\u001b[m')
            acertos.append(palpite)
        else:
            limpar()
            print('\u001b[32mVocê errou!\u001b[m')
            chances -= 1
            erros.append(palpite)
        if chances == 0:
            forca.desenho(chances)
            print(f'\u001b[32m\nQue pena, você perdeu! A resposta correta era {palavra}.\u001b[m')
            input("\u001b[32mPressione ENTER para sair...\u001b[m")
            limpar()
            break
        elif set(palavra).issubset(set(tentativas)):
            forca.desenho(chances)
            print(f'\u001b[32m\nParabéns, você ganhou! A palavra era {palavra}.\u001b[m')
            input("\u001b[32mPressione ENTER para sair...\u001b[m")
            limpar()
            break
