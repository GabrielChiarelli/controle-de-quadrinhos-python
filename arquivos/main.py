from interface import *
from arquivo import *

arquivo = 'lista-quadrinhos.txt'

if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:
    resposta = menu(['Ver quadrinhos cadastrados', 'Cadastrar novo quadrinho', 'Remover quadrinho', 'Sobre o Programa', 'Sair do sistema'])
    if resposta == 1:
        lerArquivo(arquivo, 'QUADRINHOS CADASTRADOS')
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        titulo = str(input('Título: '))
        numero = int(input('Número: '))
        ano = int(input('Ano de Lançamento: '))
        #quantidade = int(input('Quantiade de edições: '))
        cadastrar(arquivo, titulo, numero, ano)
    elif resposta == 3:
        removerQuadrinho(arquivo)
    elif resposta == 4:
        cabecalho('''\nAcredito que a melhor maneira de se aprender algo é aplicando o conhecimneto em algo que se ama.
                  \nEntão criei esse programa para colocar em prática os meus conhecimentos de Python e também para organizar a minha coleção de Quadrinhos!
                  \nEspero que goste :)
                  \nControle de Quadrinhos - V1.0 - 01/07/2022 - Desenvolvido por Gabriel Chiarelli''')
    elif resposta == 5:
        cabecalho('Saindo do sistema... Obrigado pela preferência :)')
        break
    else:
        print('Digite uma opção válida!')


# Controle de Quadrinhos - V1.0 - 01/07/2022 - Desenvolvido por Gabriel Chiarelli :)
