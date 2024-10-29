# main.py

from models import Biblioteca
from controller import BibliotecaController
from views import BibliotecaView

def main():
    # Criar a instância principal da Biblioteca
    biblioteca = Biblioteca()
    
    # Criar o controlador com base na biblioteca
    controller = BibliotecaController(biblioteca)
    
    # Criar a view para interagir com o usuário
    view = BibliotecaView(controller)
    
    while True:
        view.menu()  # Exibe o menu para o usuário
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            view.cadastrar_livro()
        elif opcao == "2":
            view.cadastrar_usuario()
        elif opcao == "3":
            view.buscar_livro()
        elif opcao == "4":
            view.emprestar_livro()
        elif opcao == "5":
            view.devolver_livro()
        elif opcao == "6":
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
