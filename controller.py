# Define a classe StopwatchController, responsável por controlar a interação entre o modelo e a visualização
class StopwatchController:
    def __init__(self, model, view):
        # Inicializa o controlador com instâncias do modelo e da visualização
        self.model = model
        self.view = view

        # Configura os comandos dos botões na visualização para chamar os métodos do controlador
        self.view.start_button.config(command=self.start)
        self.view.stop_button.config(command=self.stop)
        self.view.reset_button.config(command=self.reset)

        # Atualiza a exibição inicial
        self.update_display()

    # Método para iniciar o cronômetro
    def start(self):
        # Verifica se o cronômetro não está em execução
        if not self.model.running:
            # Inicia o cronômetro no modelo
            self.model.start()
            # Atualiza o contador
            self.update_counter()

    # Método para parar o cronômetro
    def stop(self):
        # Verifica se o cronômetro está em execução
        if self.model.running:
            # Para o cronômetro no modelo
            self.model.stop()

    # Método para reiniciar o cronômetro
    def reset(self):
        # Reinicia o cronômetro no modelo
        self.model.reset()
        # Atualiza a exibição
        self.update_display()

    # Método para atualizar o contador de tempo do cronômetro e a exibição
    def update_counter(self):
        # Verifica se o cronômetro está em execução
        if self.model.running:
            # Incrementa o contador de tempo no modelo
            self.model.increment_counter()
            # Atualiza a exibição
            self.update_display()
            # Configura um temporizador para chamar recursivamente este método após 1 segundo
            self.view.root.after(1000, self.update_counter)

    # Método para atualizar a exibição do tempo no rótulo da visualização
    def update_display(self):
        # Formata o tempo (segundos) em horas:minutos:segundos
        display = self.format_time(self.model.counter)
        # Configura o texto do rótulo na visualização
        self.view.label.config(text=display)

    # Método estático para formatar o tempo em horas:minutos:segundos
    @staticmethod
    def format_time(seconds):
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        return f"{h:02d}:{m:02d}:{s:02d}"
