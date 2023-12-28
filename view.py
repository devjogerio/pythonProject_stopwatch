# Importa a biblioteca tkinter e a renomeia como Tkinter (usando maiúscula para seguir convenções)
import tkinter as Tkinter


# Define a classe StopwatchView, responsável pela interface gráfica
class StopwatchView:
    def __init__(self, root):
        # Inicializa a classe com o parâmetro 'root' (que é a janela principal)
        self.root = root

        # Define o título da janela como "Stopwatch"
        self.root.title("Stopwatch")

        # Define o tamanho mínimo da janela como largura=250 e altura=70 pixels
        self.root.minsize(width=250, height=70)

        # Cria um rótulo (label) na janela com o texto 'Ready!', cor do texto preta (fg='black') e fonte 'Verdana 30
        # bold'
        self.label = Tkinter.Label(self.root, text='Ready!', fg='black', font='Verdana 30 bold')
        self.label.pack()  # Adiciona o rótulo à janela

        # Cria um frame na janela para organizar os botões
        self.frame = Tkinter.Frame(self.root)

        # Cria três botões: 'Start', 'Stop' e 'Reset'
        self.start_button = Tkinter.Button(self.frame, text='Start', width=6)
        self.stop_button = Tkinter.Button(self.frame, text='Stop', width=6, state='disabled')
        self.reset_button = Tkinter.Button(self.frame, text='Reset', width=6, state='disabled')

        # Posiciona os botões no frame ('Start', 'Stop' e 'Reset' da esquerda para a direita)
        self.start_button.pack(side='left')
        self.stop_button.pack(side='left')
        self.reset_button.pack(side='left')

        # Adiciona o frame à janela, centralizado verticalmente com um espaço de 5 pixels acima e abaixo
        self.frame.pack(anchor='center', pady=5)
