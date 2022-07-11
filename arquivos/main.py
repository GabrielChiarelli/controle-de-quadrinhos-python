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
        titulo = str(input('Título: '))
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
        cabecalho('''\nAcredito que a melhor maneira de se aprender algo é aplicando o conhecimneto em algo que se ama.
                  \nEntão criei esse programa para colocar em prática os meus conhecimentos de Python e também para organizar a minha coleção de Quadrinhos!
                  \nEspero que goste :)
                  \nControle de Quadrinhos - V1.1 - 11/07/2022 - Desenvolvido por Gabriel Chiarelli''')
    elif resposta == 6:
        cabecalho('Saindo do sistema... Obrigado pela preferência :)')
        break
    else:
        print('Digite uma opção válida!')


# Controle de Quadrinhos - V1.1 - 11/07/2022 - Desenvolvido por Gabriel Chiarelli :)
# Controle de Quadrinhos - V1.0 - 01/07/2022 - Desenvolvido por Gabriel Chiarelli :)
