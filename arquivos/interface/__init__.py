def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: Por favor, digite um número válido: )')
            continue
        except KeyboardInterrupt:
            print('Nenhuma opção escolhida.')
            return 0
        else:
            return num


def linha(tamanho=100):
    return ('-' * tamanho)


def cabecalho(txt):
    print(linha())
    print(txt.center(100))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')

    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1

    print(linha())
    opc = leiaInt('Sua Opção: ')
    return opc

