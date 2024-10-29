# models.py

class Livro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.emprestado = False  # Indica se o livro está emprestado ou não


class Usuario:
    def __init__(self, nome, id_usuario):
        self.nome = nome
        self.id_usuario = id_usuario
        self.livros_emprestados = []  # Lista de livros emprestados pelo usuário


class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def buscar_livro(self, termo, tipo):
        resultados = []
        if tipo == 'titulo':
            resultados = [livro for livro in self.livros if termo.lower() in livro.titulo.lower()]
        elif tipo == 'autor':
            resultados = [livro for livro in self.livros if termo.lower() in livro.autor.lower()]
        return resultados

    def emprestar_livro(self, isbn, id_usuario):
        livro = next((l for l in self.livros if l.isbn == isbn and not l.emprestado), None)
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        
        if livro and usuario:
            livro.emprestado = True
            usuario.livros_emprestados.append(livro)
            return True
        return False

    def devolver_livro(self, isbn, id_usuario):
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        if usuario:
            livro = next((l for l in usuario.livros_emprestados if l.isbn == isbn), None)
            if livro:
                livro.emprestado = False
                usuario.livros_emprestados.remove(livro)
                return True
        return False
