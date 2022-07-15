from interface import *
from arquivo import *

arquivo = 'lista-quadrinhos.txt'

if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:
    resposta = menu(['Ver quadrinhos cadastrados', 'Cadastrar novo quadrinho', 'Buscar quadrinho', 'Remover quadrinho', 'Sobre o Programa', 'Sair do sistema'])
    if resposta == 1:
        lerArquivo(arquivo, 'QUADRINHOS CADASTRADOS')
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        titulo = str(input('Título: ')).strip()
        numero = leiaInt('Número: ')
        ano = leiaInt('Ano de Lançamento: ')
        quantidade = leiaInt('Quantidade de edições: ')
        while quantidade <= 0:
            quantidade = leiaInt('Quantidade de edições inválida. Por favor, cadastre pelo menos uma: ')
        cadastrar(arquivo, titulo, numero, ano, quantidade)
    elif resposta == 3:
        palavra_chave = str(input('Digite o título que gostaria de procurar: ')).strip()
        while palavra_chave == '':
            palavra_chave = str(input('Título inválido. Por favor, digite outro: '))
        buscarQuadrinho(arquivo, palavra_chave)
    elif resposta == 4:
        removerQuadrinho(arquivo)
    elif resposta == 5:
        cabecalho('''Seja muito bem-vindo ao "Controle de Quadrinhos em Python".
Este programa te permite listar todos os seus Quadrinhos, incluindo seus títulos, números, ano de lançamento e quantidade de edições.
Você também pode deletar quadrinhos que não possui mais, e pesquisar por um título específico!
Espero que ele lhe divirta e lhe ajude com sua Coleção!
Muito obrigado e abraços :) 
v1.2 (15/07/2022) - Desenvolvido por Gabriel Chiarelli\n''')
    elif resposta == 6:
        cabecalho('Saindo do sistema... Obrigado pela preferência :)')
        break
    else:
        print('Digite uma opção válida!')


# Controle de Quadrinhos - v1.2 - 15/07/2022 - Desenvolvido por Gabriel Chiarelli :)
# Controle de Quadrinhos - V1.1 - 11/07/2022 - Desenvolvido por Gabriel Chiarelli :)
# Controle de Quadrinhos - V1.0 - 01/07/2022 - Desenvolvido por Gabriel Chiarelli :)
