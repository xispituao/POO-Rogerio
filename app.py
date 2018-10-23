from intermediario import *
from print_cores import *
import time
from datetime import datetime


def main():
    inter = Intermediario()
    p = printer()
    print('Microsoft Windows [versão 6.1.7601]\nCopyright <c> 2009 Microsoft Corporation. ', end='')
    print('Todos os direitos reservados.')
    print('C:\\Users\\Natanael>')
    time.sleep(1)
    print('C:\\Users\\Natanael>cd desktop')
    time.sleep(1)
    while True:
        comando = input('\n(Para ajuda digite help e sair digite exit.)\nC:\\Users\\Natanael\\Desktop> ')
        if comando == "help":
            p.print(msg="**Comandos**", color="RED", saltarlinha='1x')
            p.print(msg="\tgit init <nome>", color="GREEN", saltarlinha='pao')
            print(' -> Cria um novo diretorio.')
            p.print(msg="\tdel dir <nome>", color="GREEN", saltarlinha='pao')
            print(' -> Deleta o diretorio solicitado.')
            p.print(msg="\tuse <diretorio>", color="GREEN", saltarlinha='pao')
            print(' -> Usa o diretorio solicitado.')
            p.print(msg="\tcopy con <arquivo.txt>", color="GREEN", saltarlinha='pao')
            print(" -> Cria um arquivo no diretorio selecionado com o nome digitado e solicita que se digite"
                  " algo para o conteudo do arquivo.")
            p.print(msg="\tdel <arquivo.txt>", color="GREEN", saltarlinha='pao')
            print(' -> Deleta o arquivo solicitado.')
            p.print(msg="\tmodify <arquivo.txt>", color="GREEN", saltarlinha='pao')
            print(' - > Permite modificar conteudo do arquivo.')
            p.print(msg="\tgit status", color="GREEN", saltarlinha='pao')
            print(' -> Mostrar branch usado e os arquivos que estão prontos para o staging area e/oo para commit')
            p.print(msg="\tgit add <arquivo.txt>", color="GREEN", saltarlinha='pao')
            print(' -> Adiciona as mudancas dos arquivo do diretorio atual para a staging area.')
            p.print(msg="\tgit commit <arquivo.txt>", color="GREEN", saltarlinha='pao')
            print(' -> Desloca o arquivo da staging area para o repositorio local.')
            p.print(msg="\tgit log", color="GREEN", saltarlinha='pao')
            print(' -> Lista todos os commit já realizados de forma decrescente.')

        elif comando == "exit":
            break

        elif comando.split()[0] + comando.split()[1] == "gitinit":
            nome = comando.split()[2]
            inter.criar_repositorio(nome)
            p.print(msg="Sucesso!", color="GREEN", saltarlinha='sim')

        elif comando.split()[0] == "use":
            diretorio = comando.split()[1]
            if inter.selecionar_diretorio(diretorio):
                p.print(msg="Selecionado!", color="GREEN", saltarlinha='sim')
            else:
                p.print(msg="Diretorio não existe!(Use git init <nome>)", color="RED", saltarlinha='sim')

        elif comando.split()[0] + comando.split()[1] == "deldir":
            diretorio = comando.split()[2]
            inter.apagar_repositorio(diretorio)
            p.print(msg="Deletado!", color="GREEN", saltarlinha='sim')

        elif comando.split()[0] + comando.split()[1] == "copycon":
            nome = comando.split()[2]
            conteudo = input("Conteudo: ")
            inter.criar_arquivo(nome, conteudo)
            p.print(msg="Arquivo criado!", color="GREEN", saltarlinha='sim')

        elif comando.split()[0] == "modify":
            novo_conteudo = input("Novo conteudo: ")
            if inter.modificar_conteudo_arquivo(comando.split()[1], novo_conteudo):
                p.print(msg="Arquivo modificado!", color="GREEN", saltarlinha='sim')
            else:
                p.print(msg="Arquivo não existe!", color="GREEN", saltarlinha='sim')

        elif comando.split()[0] == "del":
            if inter.deletar_arquivo(comando.split()[1]):
                p.print(msg="Arquivo deletado!", color="GREEN", saltarlinha='sim')
            else:
                p.print(msg="Arquivo não existe!", color="GREEN", saltarlinha='sim')

        elif comando.split()[0] + comando.split()[1] == "gitstatus":
            if inter.status():
                aux = 0
                print('On branch master')
                if inter.status()[0]:
                    print("\nUntracked files:\n   <use 'git add <file>...' to include in what will be committed>")
                    for untracked_files in inter.status()[0]:
                        p.print(msg="\n\t\t" + untracked_files.getnome(), color="RED", saltarlinha='sim')
                    print('\n')
                    aux += 1
                if inter.status()[1]:
                    print("\nChanges not staged for commit:\n   <use 'git add <file>...' to update  what will be "
                          "committed>")
                    for nostaged_files in inter.status()[1]:
                        if nostaged_files.getstatus()[3]:
                            nome = nostaged_files.getstatus()[3]
                            p.print(msg="\n\t\t" + nostaged_files.getstatus()[2] + ":" + nome, color="RED", saltarlinha='sim')
                        else:
                            p.print(msg="\n\t\t"+nostaged_files.getstatus()[2]+":"+nostaged_files.getnome(), color="RED", saltarlinha='sim')
                    print('\n')
                    aux += 1
                if inter.status()[2]:
                    print("Changes to be committed:\n   <use 'git reset' to unstage>")
                    for be_committed_files in inter.status()[2]:
                        p.print(msg="\n\t\t"+be_committed_files.getstatus()[2]+":"+be_committed_files.getnome(), color="GREEN", saltarlinha='sim')
                    print('\n')
                    aux += 1
                if aux == 0:
                    print("nothing to commit, working tree clean")
            else:
                p.print(msg="Diretorio não selecionado!(use o comando use <diretorio> antes.)", color="RED", saltarlinha='sim')

        elif comando.split()[0] + comando.split()[1] == "gitadd":
            if inter.add(comando.split()[2]):
                p.print(msg="Sucesso!", color="GREEN", saltarlinha='sim')
            elif inter.add(comando.split()[2]) == "dir":
                p.print(msg="Diretorio não selecionado!(use o comando use <diretorio> antes.)", color="RED",
                        saltarlinha='sim')
            else:
                p.print(msg="Arquivo não existe!", color="GREEN", saltarlinha='sim')

        elif comando.split()[0] + comando.split()[1] == "gitcommit":
            nome = comando.split()[2]
            comentario = input("Comentario: ")
            now = datetime.now()
            if inter.commit(nome, comentario, now.day, now.month, now.year, now.hour, now.minute, now.second):
                p.print(msg="Sucesso!", color="GREEN", saltarlinha='sim')
            else:
                p.print(msg="Fracasso !", color="RED", saltarlinha='sim')

        else:
            print("Digite um comando válido!!")


if __name__ == '__main__':
    main()
