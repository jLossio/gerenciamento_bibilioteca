# views.py

from controller import BibliotecaController

class BibliotecaView:
    def __init__(self, controller):
        self.controller = controller

    def menu(self):
        print("\nBem-vindo à Biblioteca")
        print("1. Cadastrar Livro")
        print("2. Cadastrar Usuário")
        print("3. Buscar Livro")
        print("4. Emprestar Livro")
        print("5. Devolver Livro")
        print("6. Sair")

    def exibir_mensagem(self, mensagem):
        print(mensagem)

    def cadastrar_livro(self):
        titulo = input("Título do Livro: ")
        autor = input("Autor do Livro: ")
        isbn = input("ISBN do Livro: ")
        mensagem = self.controller.cadastrar_livro(titulo, autor, isbn)
        self.exibir_mensagem(mensagem)

    def cadastrar_usuario(self):
        nome = input("Nome do Usuário: ")
        id_usuario = input("ID do Usuário: ")
        mensagem = self.controller.cadastrar_usuario(nome, id_usuario)
        self.exibir_mensagem(mensagem)

    def buscar_livro(self):
        tipo = input("Buscar por (titulo/autor): ")
        termo = input("Informe o termo de busca: ")
        resultados = self.controller.buscar_livro(termo, tipo)
        for livro in resultados:
            print(f"Título: {livro.titulo}, Autor: {livro.autor}, ISBN: {livro.isbn}, Emprestado: {'Sim' if livro.emprestado else 'Não'}")

    def emprestar_livro(self):
        isbn = input("ISBN do Livro para empréstimo: ")
        id_usuario = input("ID do Usuário: ")
        mensagem = self.controller.emprestar_livro(isbn, id_usuario)
        self.exibir_mensagem(mensagem)

    def devolver_livro(self):
        isbn = input("ISBN do Livro para devolução: ")
        id_usuario = input("ID do Usuário: ")
        mensagem = self.controller.devolver_livro(isbn, id_usuario)
        self.exibir_mensagem(mensagem)
