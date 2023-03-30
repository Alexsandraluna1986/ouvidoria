
from operacoesbd import *

#abrirBancoDados(host,user,password,database)

conexao = abrirBancoDados('localhost','root','sucesso1803#','ouvidoria2')

#inserir uma nova reclamação

autorReclamacao =input('Registre aqui o seu nome: ')
novaReclamacao = input('Registre aqui a sua reclamação: ')

consultarReclamacao = 'insert into ouvidoria (titular_reclamacao, reclamacao) values (%s,%s)'
dados = (autorReclamacao,novaReclamacao)
insertNoBancoDados (conexao,consultarReclamacao,dados)
print()
print('Sua reclamação foi registrada com sucesso, Obrigado(a)!')

#listar reclamações
consulta_reclamacao = 'select * from ouvidoria'
listaReclamacao = listarBancoDados(conexao,consulta_reclamacao)
if len(listaReclamacao) == 0:
    print('Não há reclamações registradas!')
else:
    print()
    print('Listagem de reclamações')
for reclamacao in listaReclamacao:
    print('codigo:',reclamacao[0],'titular: ', reclamacao[1], 'Reclamação: ',reclamacao[2])
print()

#pesquisar uma reclamação
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
        print('codigo:',reclamacao[0], 'titular:', reclamacao[1],'Reclamação:',reclamacao[2])





encerrarBancoDados(conexao)