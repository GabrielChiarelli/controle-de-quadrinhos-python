def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: Por favor, digite uma opção válida: )')
            continue
        except KeyboardInterrupt:
            print('Nenhuma opção escolhida.')
            return 0
        else:
            return num


def linha(tamanho=52):
    return ('-' * tamanho)


def cabecalho(txt):
    print(linha())
    print(txt.center(52))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')

    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1

    print(linha())
    opc = leiaInt('Sua Opção: ')
    #opc = int(input('Sua Opção: '))
    return opc

