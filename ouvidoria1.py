from operacoesbd import *

conexao = abrirBancoDados('localhost', 'root', 'sucesso1803#', 'ouvidoria2')

opcao = 6

while opcao != 5:
    print()
    print('Seja bem-vindo(A) a Ouvidoria!')
    print()
    print('Escolha sua opção: ')
    print()
    print('1- Listar uma reclamação, 2- Pesquisar uma reclamação pelo código, 3- Inserir uma nova reclamação, 4- Remover reclamação pelo código, 5- SAIR')
    print()
    opcao = int(input('Digite a sua escolha: '))
    print()

    if opcao == 1:
        consulta_reclamacao = 'select * from ouvidoria'
        listaReclamacao = listarBancoDados(conexao, consulta_reclamacao)
        if len(listaReclamacao) == 0:
            print('Não há reclamações registradas!')
        else:
            print()
            print('Listagem de reclamações')
        for reclamacao in listaReclamacao:
            print('codigo:', reclamacao[0], '/titular: ', reclamacao[1], '/Reclamação: ', reclamacao[2])
        print()

    elif opcao == 2:
        print('Pesquisa de reclamação pelo código')
        print()
        codigo = input('Digite o código da reclamação a ser consultada: ')
        pesquisarReclamacao = 'select * from ouvidoria where codigo_reclamacao =' + codigo
        listareclamacao = listarBancoDados(conexao, pesquisarReclamacao)
        if len(listareclamacao) == 0:
            print('Não existe nenhuma reclamação registrada!')
        else:
            print('listagem das reclamações')
            print()
            for reclamacao in listareclamacao:
                print('codigo:', reclamacao[0], '/titular:', reclamacao[1], '/Reclamação:', reclamacao[2])


    elif opcao == 3:
        autorReclamacao = input('Registre aqui o seu nome: ')
        novaReclamacao = input('Registre aqui a sua reclamação: ')
        consultarReclamacao = 'insert into ouvidoria (titular_reclamacao, reclamacao) values (%s,%s)'
        dados1 = (autorReclamacao, novaReclamacao)
        insertNoBancoDados(conexao, consultarReclamacao, dados1)
        print()
        print('Sua reclamação foi registrada com sucesso, Obrigado(a)!')

    elif opcao == 4:
        consulta_reclamacao = 'select * from ouvidoria'
        listaReclamacao = listarBancoDados(conexao, consulta_reclamacao)
        if len(listaReclamacao) == 0:
            print('Não há reclamações registradas!')
        else:
            print()
            print('Listagem de reclamações')
        for reclamacao in listaReclamacao:
            print('codigo:', reclamacao[0], '/titular: ', reclamacao[1], '/Reclamação: ', reclamacao[2])
            print()
            codigo = input('Digite o código a ser excluído: ')
            consultaRemoverReclamacao = 'delete from ouvidoria where codigo_reclamacao = %s'
            dados = (codigo,)

            excluirBancoDados(conexao,consultaRemoverReclamacao,dados)
            print('Sua reclamação foi removida com sucesso!')

encerrarBancoDados(conexao)

print('Obrigado(a) pela sua visita!')
