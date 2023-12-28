import tkinter as Tkinter
from datetime import datetime

counter = 0  # Inicializa o contador para 0
running = False  # Define a posição do cronômetro como parado


# Função para atualizar o texto do label do contador
def counter_label(label):
    # Função interna que atualiza o contador
    def count():
        if running:  # Verifica se o cronômetro está em execução
            global counter  # Permite modificar a variável counter fora do escopo atual
            if counter == 0:  # Se o contador for zero, exibe 'Ready!'
                display = 'Começando!'
            else:
                tt = datetime.utcfromtimestamp(counter)  # Converte o contador em um objeto de tempo
                string = tt.strftime('%H:%M:%S')  # Formata o tempo como uma string HH:MM:SS
                display = string  # Atualiza o texto do display com o tempo formatado
            label['text'] = display  # Define o texto do label como o valor do display

            # label.after(arg1, arg2) aguarda arg1 milissegundos e chama a função arg2
            # Aqui, chama recursivamente a função count após 1000ms (1 segundo)
            label.after(1000, count)
            counter += 1  # Incrementa o contador em 1 a cada segundo

    count()  # Chama a função count para iniciar a contagem


# Função para iniciar o cronômetro
def Start(label):
    global running  # Permite modificar a variável running fora do escopo atual
    running = True  # Altera o status para em execução
    counter_label(label)  # Chama a função para atualizar o label do contador
    start['state'] = 'disabled'  # Desabilita o botão 'Start'
    stop['state'] = 'normal'  # Habilita o botão 'Stop'
    reset['state'] = 'normal'  # Habilita o botão 'Reset'


# Função para parar o cronômetro
def Stop():
    global running  # Permite modificar a variável running fora do escopo atual
    start['state'] = 'normal'  # Habilita o botão 'Start'
    stop['state'] = 'disabled'  # Desabilita o botão 'Stop'
    reset['state'] = 'normal'  # Habilita o botão 'Reset'
    running = False  # Altera o status para parado


# Função para resetar o cronômetro
def Reset(label):
    global counter  # Permite modificar a variável counter fora do escopo atual
    counter = 0  # Reseta o contador para 0

    if not running:  # Se o cronômetro não estiver em execução ao pressionar reset
        reset['state'] = 'disabled'  # Desabilita o botão 'Reset'
        label['text'] = '00:00:00'  # Define o texto do label como '00:00:00'
    else:  # Se o cronômetro estiver em execução ao pressionar reset
        label['text'] = '00:00:00'  # Define o texto do label como '00:00:00'


root = Tkinter.Tk()  # Cria uma janela principal
root.title("Stopwatch")  # Define o título da janela como "Stopwatch"

root.minsize(width=250, height=70)  # Define o tamanho mínimo da janela

label = Tkinter.Label(root, text='pronto pra começar!', fg='black', font='Verdana 26 bold')  # Cria um label com texto 'Ready!'
label.pack()  # Coloca o label na janela

f = Tkinter.Frame(root)  # Cria um frame na janela principal
start = Tkinter.Button(f, text='Start', width=6, command=lambda: Start(label))  # Botão 'Start'
stop = Tkinter.Button(f, text='Stop', width=6, state='disabled', command=Stop)  # Botão 'Stop'
reset = Tkinter.Button(f, text='Reset', width=6, state='disabled', command=lambda: Reset(label))  # Botão 'Reset'

f.pack(anchor='center', pady=5)  # Posiciona o frame no centro da janela
start.pack(side='left')  # Posiciona o botão 'Start' à esquerda
stop.pack(side='left')  # Posiciona o botão 'Stop' à esquerda
reset.pack(side='left')  # Posiciona o botão 'Reset' à esquerda

root.mainloop()  # Inicia o loop principal da interface gráfica
