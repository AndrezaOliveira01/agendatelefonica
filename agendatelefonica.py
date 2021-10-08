# Agenda Telefônica em Python
# Bibliotecas
import pandas as pd
import os

# Variáveis Globais
menu = 0
agenda = []


# Funções do Menu 1 ao 5
# Função para inserir um ou mais contatos
def inserir():
    qtdeContato = int(input('Quantos contatos deseja incluir?'))  # Solicitação para inclusão de 1 ou mais contatos
    contador = 0
    while contador < qtdeContato:
        contador += 1
        contato = {  # Inclusão de contato
            'Nome': input('Informe o nome: '),
            'Telefone': int(input('Informe o telefone: ')),
            'E-mail': input('Informe o e-mail: '),
            'Twitter': input('Informe a conta do Twitter: '),
            'Instagram': input('Informe a conta do Instagram: '),
            'Facebook': input('Informe a conta do Facebook: ')
        }
        agenda.append(contato)


# Função de pesquisa de contato
def pesquisar():
    pesquisa = input('Informe o nome para pesquisa: ')
    resultadoEncontrado = False  # Variável usada para verificar se o dado foi encontrado
    for itemAgenda in agenda:  # Examina os itens da lista
        if pesquisa == itemAgenda['Nome']:  # Validar se o nome informado na pesquisa esta no dicionário corrente
            print('Resultado: ', itemAgenda)
            resultadoEncontrado = True
            break
    if not resultadoEncontrado:
        print('Não localizado')


# Função de excluir contato
def excluir():
    pesquisa = input('Informe o nome para pesquisa: ')
    contatoRemover = {}
    resultadoEncontrado = False  # Variável usada para verificar se o dado foi encontrado
    for itemAgenda in agenda:  # Examina os itens da lista
        if pesquisa == itemAgenda['Nome']:  # Validar se o nome informado na pesquisa esta no dicionário corrente
            resultadoEncontrado = True
            contatoRemover = itemAgenda  # Variável para guardar item pesquisado
            break
    if resultadoEncontrado:
        agenda.remove(contatoRemover)  # Remoção do contato
        print('Contato removido')
    else:
        print('Não localizado')


# Função de alterar contato
def alterar():
    pesquisa = input('Informe o nome para pesquisa: ')
    contatoAlterar = {}
    resultadoEncontrado = False  # Variável usada para verificar se o dado foi encontrado
    for itemAgenda in agenda:  # Examina os itens da lista
        if pesquisa == itemAgenda['Nome']:  # Validar se o nome informado na pesquisa esta no dicionário corrente
            resultadoEncontrado = True
            contatoAlterar = itemAgenda  # Variável para guardar item pesquisado
            break
    if resultadoEncontrado:  # Alteração do contato por item
        novoNome = input('Altere o nome: ')
        if novoNome != '':
            contatoAlterar['Nome'] = novoNome
        novoTelefone = input('Altere o telefone: ')
        if novoTelefone != '':
            contatoAlterar['Telefone'] = novoTelefone
        novoEmail = input('Altere o e-mail: ')
        if novoEmail != '':
            contatoAlterar['E-mail'] = novoEmail
        novoTwitter = input('Altere o Twitter: ')
        if novoTwitter != '':
            contatoAlterar['Twitter'] = novoTwitter
        novoInstagram = input('Altere o Instagram: ')
        if novoInstagram != '':
            contatoAlterar['Instagram'] = novoInstagram
        novoFacebook = input('Altere o Facebook: ')
        if novoFacebook != '':
            contatoAlterar['Facebook'] = novoFacebook
        print('Contato alterado')
    else:
        print('Não localizado')


# Função para visualizar agenda
def visualizar():
    if agenda is None or len(agenda) == 0:  # Verifica se a agenda esta vazia
        print('Nenhum registro encontrado')
    else:
        from prettytable import PrettyTable  # Importação para impressão da tabela
        t = PrettyTable(['Nome', 'Telefone', 'E-mail', 'Twitter', 'Instagram', 'Facebook'])  # Impressão do cabeçalho
        for itemAgenda in agenda:  # Retorna os contatos da agenda
            t.add_row([itemAgenda['Nome'],
                      itemAgenda['Telefone'],
                      itemAgenda['E-mail'],
                      itemAgenda['Twitter'],
                      itemAgenda['Instagram'],
                      itemAgenda['Facebook']])
        print(t)

        # Decisão de exportar agenda para TXT
        while True:
            print('Deseja exportar sua agenda?')
            print('1 - Sim')
            print('2 - Não')
            opcao = int(input('Escolha a opção: '))
            if opcao == 2:
                print('Fim.')
                break
            elif opcao == 1:
                if os.path.isfile('agenda.txt'):  # Verificar se arquivo existe
                    os.remove('agenda.txt')  # Excluindo arquivo existente
                for itemAgenda in agenda:
                    df = pd.DataFrame.from_dict([itemAgenda])
                    df.to_csv('agenda.txt', header=False, index=True, mode='a')  # Criando novo arquivo
                print('Arquivo importado.')
                print('_______________________', end='\n')


# Menu Inicial da Agenda
while True:
    print('Agenda Telefônica')
    print('_______________________', end='\n')
    print('1 - Inserir novo contato')
    print('2 - Pesquisar')
    print('3 - Excluir')
    print('4 - Alterar')
    print('5 - Visualizar agenda')
    print('6 - Sair')
    menu = int(input('Escolha a opção: '))
    # Opção 6-Sair
    if menu == 6:
        print('Fim.')
        break
    print('_______________________', end='\n')
    # Opção 1-Inserir
    if menu == 1:
        inserir()
        print('_______________________', end='\n')
    # Opção 2-Pesquisar
    elif menu == 2:
        pesquisar()
        print('_______________________', end='\n')
    # Opção 3-Excluir
    elif menu == 3:
        excluir()
        print('_______________________', end='\n')
    # Opção 4-Alterar
    elif menu == 4:
        alterar()
        print('_______________________', end='\n')
    # Opção 5-Visualizar
    elif menu == 5:
        visualizar()
        print('_______________________', end='\n')
