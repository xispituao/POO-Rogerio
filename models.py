class Arquivo:
    def __init__(self, nome, conteudo):
        self.nome = nome
        self.conteudo = conteudo
        self.status = ["untracked", "notstaged", "new", None, False]

    def modificar_conteudo(self, conteudo_novo):
        if self.status[1] == "staged":
            nome = self.getnome() + "2"
            a = Arquivo(nome, conteudo_novo)
            a.status[0], a.status[2], a.status[3] = "tracked", "modified", self.getnome()
            return a
        elif self.status[0] == "untracked":
            self.conteudo = conteudo_novo
        #else:
         #   self.conteudo = conteudo_novo
          #  self.status[2] = "modified"

    def apagar(self):
        if self.status[0] == "untracked":
            return "unt"
        else:
            if self.status[1] == "staged":
                nome = self.getnome() + "2"
                a = Arquivo(nome, self.conteudo)
                a.status[0], a.status[2], a.status[3] = "tracked", "deleted", self.getnome()
                return a

    def add(self, arquivo=None):
        if arquivo is not None:
            arquivo.conteudo = self.conteudo

        elif self.status[0] == "untracked":
            self.status[0] = "tracked"
            self.status[1] = "staged"
        elif self.status[0] == "tracked" and self.status[1] == "notstaged":
            self.status[1] = "staged"

    def commit(self):
        if self.status == "untracked":
            return "Error_1"
        elif self.status == "tracked" and self.status[1] == "notstaged":
            return "Error_2"
        else:
            self.status[4] = True
            return True

    def getnome(self):
        return self.nome

    def getconteudo(self):
        return self.conteudo

    def getstatus(self):
        return self.status


class Commit:
    def __init__(self, nome, status, comentario, dia, mes, ano, hora, minutos, segundos):
        self.nome = nome
        self.status =status
        self.data = str(dia) + "/" + str(mes) + "/" + str(ano)
        self.horario = str(hora) + "/" + str(minutos) + "/" + str(segundos)
        self.comentario = comentario

    def getdata(self):
        return self.data

    def gehora(self):
        return self.hora

    def gethash(self):
        return self.hash


class Diretorio:
    def __init__(self, nome):
        self.nome = nome
        self.arquivos = []
        self.commmits = []

    def adicionar_arquivo_no_repositorio(self, arquivo):
        self.arquivos.append(arquivo)
        return True

    def getnome(self):
        return self.nome

    def getarquivos(self):
        return self.arquivos

    def modificar_arquivo(self, nome, novo_conteudo):
        for arquivo in self.arquivos:
            if arquivo.getnome() == nome:
                aux = arquivo.modificar_conteudo(novo_conteudo)
                if aux:
                    self.arquivos.append(aux)

                return True
        return False

    def apagar_arquivo(self, nome):
        for arquivo in self.arquivos:
            if arquivo.getnome() == nome:
                if arquivo.apagar() == "unt":
                    self.arquivos.remove(arquivo)
                    return True
                else:
                    self.arquivos.append(arquivo.apagar())
                    return True
        return False

    def add(self, nome):
        for arquivo in self.arquivos:
            if arquivo.getnome() == nome + "2":
                for arquivo2 in self.arquivos:
                    if arquivo2.getnome() == nome:
                        if arquivo.getstatus()[2] == "modified":
                            arquivo.add(arquivo2)
                            self.arquivos.remove(arquivo)
                        else:
                            self.arquivos.remove(arquivo)
                            self.arquivos.remove(arquivo2)
                        return True

        for arquivo in self.arquivos:
            if arquivo.getnome() == nome:
                arquivo.add()
                return True
        return False

    def commit(self, nome, comentario, dia, mes, ano, hora, minutos, segundos):
        for arquivo in self.arquivos:
            if arquivo.getnome() == nome:
                if arquivo.commit():
                    a = Commit(arquivo.getnome(), arquivo.status[2], comentario, dia, mes, ano, hora, minutos, segundos)
                    self.commmits.append(a)
                    return True

        return False
