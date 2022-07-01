from interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso.')


def lerArquivo(nome, txt):
    try:
        a = open(nome, 'rt')
    except:
        print(f'Erro ao ler o arquivo {nome}')
    else:
        cabecalho(txt)
        # print(f'{"Título":>12}{"Número":>32}     id')
        indice = 1
        for linha in a:
        #    dado = linha.split(';')
        #    dado[1] = dado[1].replace('\n', '')
        #    dado[2] = dado[2].replace('\n', '')
        #    print(f'{indice} - {dado[0]:<30}{dado[1]:>3} ({dado[2]}) id: {dado[3]}')
            dict_original = str(linha)
            infos = eval(dict_original)
            print(f"{indice:>4} - {infos['titulo']:<30}{infos['numero']:>3} ({infos['ano']}) id: {infos['id']} quantidade: {infos['quantidade']}")
            indice += 1
    finally:
        a.close()


def cadastrar(arquivo, titulo='desconhecido', numero=0, ano=0000, quantidade = 1):
    try:
        a = open(arquivo, 'at')
    except:
        print(f'Houve um erro na abertura do arquivo {arquivo}')
    else:
        try:
            # percorre todas as linhas do arquivo
            with open(arquivo, 'rt') as arq:
                linhas = arq.readlines()

            # escreve uma nova linha com: TÍTULO do quadrinho - NÚMERO da edição - ANO DE LANÇAMENTO - ID de cadastro
            # a.write(f'{titulo};{numero};{ano};{len(linhas) + 1}\n')
            dict = {}
            dict['titulo'] = titulo
            dict['numero'] = numero
            dict['ano'] = ano
            #dict['id'] = len(linhas) + 1
            ultimo_id = 0
            with open(arquivo, 'rt') as arq:
                linhas = arq.readlines()
                for linha in linhas:
                    nova_linha = eval(linha)
                    ultimo_id = nova_linha['id']
            dict['id'] = ultimo_id + 1
            dict['quantidade'] = quantidade
            a.write(str(dict))
            a.write('\n')
        except:
            print('Houve um erro na hora de cadastrar os dados.')
        else:
            print(f'Novo registro de "{titulo} {numero}" adicionado!')
            a.close()


def removerQuadrinho(arquivo):
    with open(arquivo, 'r+') as arq:
        lerArquivo(arquivo, 'REMOVER QUADRINHO')
        linha_desejada = int(input('\nQual quadrinho você deseja deletar? '))
        linhas = arq.readlines()

        dict_original = str(linhas[linha_desejada - 1])
        infos = eval(dict_original)
        resposta = str(input(f"Deseja deletar o quadriho {infos['titulo']} {infos['numero']}? [S/N] ")).strip().upper()

        while resposta not in 'SN':
            resposta = str(input('Respota inválida. Por favor, coloque S ou N: ')).strip().upper()

        if resposta == 'S':
            quadrinho = f"'{infos['titulo']} {infos['numero']}'"
            if(infos['quantidade'] == 1):
                try:
                    del linhas[linha_desejada - 1]
                    arq.seek(0)
                    arq.truncate()
                    arq.writelines(linhas)
                except:
                    print(f"Ocorreu um ERRO. Não foi possível deletar o quadrinho '{quadrinho}'")
                else:
                    print(f"Quadrinho {quadrinho} deletado com sucesso.")
            else:
                quantidade_desejada = int(input('Deseja remover quantas edições? '))
                while quantidade_desejada > int(infos['quantidade']) or quantidade_desejada < int(infos['quantidade']):
                    if quantidade_desejada > int(infos['quantidade']):
                        quantidade_desejada = int(input('Quantidade desejada superior a quantidade atual. Por favor, digite um número menor: '))
                    elif quantidade_desejada < int(infos['quantidade']):
                        quantidade_desejada = int(input(
                            'Quantidade desejada inferior a quantidade atual. Por favor, escolha uma quantidade maior: '))
                if quantidade_desejada == infos['quantidade']:
                    print(f"Deletando todo o registro do quadrinho {quadrinho}")
                    del linhas[linha_desejada - 1]
                    arq.seek(0)
                    arq.truncate()
                    arq.writelines(linhas)
                else:
                    print(f"Deletando {quantidade_desejada} edições do quadrinho {quadrinho}")
                    a = open(arquivo, 'r')
                    list_of_lines = a.readlines()
                    info_antiga = list_of_lines[linha_desejada - 1]
                    nova_info = {'titulo': infos['titulo'], 'numero': infos['numero'], 'ano': infos['ano'], 'id': infos['id'], 'quantidade': infos['quantidade'] - quantidade_desejada}
                    # sobreescrever toda a linha, com a nova quantidade
                    list_of_lines[linha_desejada - 1] = str(nova_info)
                    a = open(arquivo, 'w')
                    a.writelines(list_of_lines)
                    a.close()



