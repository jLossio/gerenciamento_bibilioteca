# controller.py

from models import Livro, Usuario, Biblioteca

class BibliotecaController:
    def __init__(self, biblioteca):
        self.biblioteca = biblioteca

    def cadastrar_livro(self, titulo, autor, isbn):
        livro = Livro(titulo, autor, isbn)
        self.biblioteca.adicionar_livro(livro)
        return "Livro cadastrado com sucesso!"

    def cadastrar_usuario(self, nome, id_usuario):
        usuario = Usuario(nome, id_usuario)
        self.biblioteca.usuarios.append(usuario)
        return "Usuário cadastrado com sucesso!"

    def buscar_livro(self, termo, tipo):
        return self.biblioteca.buscar_livro(termo, tipo)

    def emprestar_livro(self, isbn, id_usuario):
        if self.biblioteca.emprestar_livro(isbn, id_usuario):
            return "Livro emprestado com sucesso!"
        return "Livro não disponível ou usuário não encontrado."

    def devolver_livro(self, isbn, id_usuario):
        if self.biblioteca.devolver_livro(isbn, id_usuario):
            return "Livro devolvido com sucesso!"
        return "Erro na devolução. Livro ou usuário não encontrado."
