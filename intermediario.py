from models import *


class Intermediario:
    def __init__(self):
        self.diretorios = []
        self.diretorio = None

    def criar_repositorio(self, nome):
        for diretorio in self.diretorios:
            if diretorio.getnome() == nome:
                return False

        self.diretorios.append(Diretorio(nome))
        return True

    def apagar_repositorio(self, nome):
        for diretorio in self.diretorios:
            if diretorio.getnome() == nome:
                self.diretorios.remove(diretorio)
                return True

        return False

    def selecionar_diretorio(self, nome):
        for diretorio in self.diretorios:
            if diretorio.getnome() == nome:
                self.diretorio = diretorio
                return True

        return False

    def criar_arquivo(self, nome, conteudo):
        if self.diretorio is None:
            return False
        else:
            self.diretorio.adicionar_arquivo_no_repositorio(Arquivo(nome, conteudo))
            return True

    def modificar_conteudo_arquivo(self, nome, novo_conteudo):
        if self.diretorio is None:
            return "dir"
        else:
            if self.diretorio.modificar_arquivo(nome, novo_conteudo):
                return True
            else:
                return False

    def deletar_arquivo(self, nome):
        if self.diretorio.apagar_arquivo(nome):
            return True
        else:
            return False

    def status(self):
        if not self.diretorio:
            return False
        else:
            untracked_files = list(filter(lambda arquivo: arquivo.getstatus()[0] == "untracked", self.diretorio.getarquivos()))
            nostaged_files = list(filter(lambda arquivo:arquivo.getstatus()[0] == "tracked" and arquivo.getstatus()[1] == "notstaged", self.diretorio.getarquivos()))
            be_commit_files = list(filter(lambda arquivo: arquivo.getstatus()[1] == "staged", self.diretorio.getarquivos()))
            return untracked_files, nostaged_files, be_commit_files

    def add(self, nome):
        if self.diretorio is None:
            return "dir"
        else:
            if self.diretorio.add(nome):
                return True
            else:
                return False

    def commit(self, nome, comentario, dia, mes, ano, hora, minutos, segundos):
        if self.diretorio is None:
            return "dir"
        else:
            if self.diretorio.commit(nome, comentario, dia, mes, ano, hora, minutos, segundos):
                return True
            else:
                return False

    def getarquivos(self):
        return self.diretorio.getarquivos()
