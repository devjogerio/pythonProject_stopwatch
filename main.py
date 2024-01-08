# Import the tkinter library and rename it as Tkinter (using capital letters to follow conventions)
import tkinter as Tkinter

# Imports the specific classes or functions from the 'model' module (presumably contains MVC model logic)
from model import StopwatchModel

# Imports the specific classes or functions from the 'view' module (presumably contains the visual part of MVC)
from view import StopwatchView

# Importa as classes ou funções específicas do módulo 'controller' (presumivelmente contém a lógica de controle do MVC)
from controller import StopwatchController


# Define a função principal 'main()' que controla a execução do programa
def main():
    # Cria uma instância da janela principal usando o Tkinter
    root = Tkinter.Tk()

    # Cria uma instância do modelo da aplicação (presumivelmente lógica de dados)
    model = StopwatchModel()

    # Cria uma instância da visualização (view) passando a janela principal como argumento
    view = StopwatchView(root)

    # Cria uma instância do controlador, passando as instâncias do modelo e da visualização como argumentos
    controller = StopwatchController(model, view)

    # Inicia o loop principal do Tkinter, exibindo a janela e aguardando interações do usuário
    root.mainloop()


# Verifica se este arquivo está sendo executado diretamente
if __name__ == "__main__":
    # Chama a função 'main()' para iniciar a aplicação
    main()
