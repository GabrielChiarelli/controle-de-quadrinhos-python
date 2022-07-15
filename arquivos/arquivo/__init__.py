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
        indice = 0
        for linha in a:
            dict_original = str(linha)
            infos = eval(dict_original)
            indice += 1
            print(f"{indice:>4} - {infos['titulo']:<30}{'N°':>3}{infos['numero']:<4} ({infos['ano']}{')':<5} | Quantidade: {infos['quantidade']:>4} | ID: {infos['id']}")
        if indice == 0:
            print(f"{'Nenhum quadrinho cadastrado.':>32}")
    finally:
        a.close()


def cadastrar(arquivo, titulo='desconhecido', numero=0, ano=0000, quantidade=1):
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
            dict = {}
            dict['titulo'] = titulo
            dict['numero'] = numero
            dict['ano'] = ano
            dict['quantidade'] = quantidade
            ultimo_id = 0
            with open(arquivo, 'rt') as arq:
                linhas = arq.readlines()
                for linha in linhas:
                    nova_linha = eval(linha)
                    ultimo_id = nova_linha['id']
            dict['id'] = ultimo_id + 1
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
        resposta = str(input(f"Deseja deletar o quadrinho {infos['titulo']} {infos['numero']}? [S/N] ")).strip().upper()

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
                while quantidade_desejada > int(infos['quantidade']) or quantidade_desejada <= 0:
                    if quantidade_desejada > int(infos['quantidade']):
                        quantidade_desejada = int(input('Quantidade desejada superior a quantidade atual. Por favor, digite um número menor: '))
                    elif quantidade_desejada <= 0:
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
                    nova_info = {'titulo': infos['titulo'], 'numero': infos['numero'], 'ano': infos['ano'], 'id': infos['id'], 'quantidade': infos['quantidade'] - quantidade_desejada}
                    # sobreescrever toda a linha, com a nova quantidade
                    list_of_lines[linha_desejada - 1] = str(nova_info)
                    a = open(arquivo, 'w')
                    a.writelines(list_of_lines)
                    a.close()


def buscarQuadrinho(arquivo, palavra_chave):
    try:
        arq = open(arquivo, 'rt')
    except:
        print(f'Erro ao ler o arquivo {arquivo}')
    else:
        indice = 0
        quadrinhos_encontrados = 0
        palavra_chave_maiuscula = str(palavra_chave).upper()
        palavra_chave_sem_hifen = palavra_chave_maiuscula.replace('-', ' ')

        for linha in arq:
            dict_original = str(linha)
            infos = eval(dict_original)

            if palavra_chave_sem_hifen in str(infos['titulo']).upper().replace('-', ' '):
                quadrinhos_encontrados += 1

        if quadrinhos_encontrados == 1:
            cabecalho(f'Foi encontrado 1 quadrinho com o título: {palavra_chave}')
        elif quadrinhos_encontrados >= 2:
            cabecalho(f'Foram encontrados {quadrinhos_encontrados} quadrinhos com o título: {palavra_chave}')
        else:
            cabecalho(f'Nenhum quadrinho encontrado com o título: {palavra_chave}')

        arq.seek(0)

        for linha in arq:
            dict_original = str(linha)
            infos = eval(dict_original)

            if palavra_chave_sem_hifen in str(infos['titulo']).upper().replace('-', ' '):
                indice += 1
                print(f"{indice:>4} - {infos['titulo']:<30}{'N°':>3}{infos['numero']:<4} ({infos['ano']}{')':<5} | Quantidade: {infos['quantidade']:>4} | ID: {infos['id']}")

    finally:
        arq.close()





