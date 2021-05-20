class Sessao(object):
    counter = 0
    usuarios = []

    def salvar(self, usuario):
        Sessao.counter += 1
        usuario.id = Sessao.counter
        Sessao.usuarios.append(usuario)

    def listar(self):
        return Sessao.usuarios

    def roll_back(self):
        Sessao.counter = 0
        Sessao.usuarios = []

    def fechar(self):
        pass


class Conexao():
    def gerar_sessao(self):
        return Sessao()

    def fechar(self):
        pass