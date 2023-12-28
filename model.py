# Define a classe StopwatchModel, que representa a lógica de dados do cronômetro
class StopwatchModel:
    def __init__(self):
        # Inicializa o contador e o estado de execução do cronômetro
        self.counter = 0  # Contador de tempo, inicializado em 0
        self.running = False  # Estado de execução, inicializado como falso (parado)

    # Reinicia o cronômetro, definindo o contador como 0 e o estado de execução como falso (parado)
    def reset(self):
        self.counter = 0
        self.running = False

    # Inicia o cronômetro, alterando o estado de execução para verdadeiro (em execução)
    def start(self):
        self.running = True

    # Para o cronômetro, alterando o estado de execução para falso (parado)
    def stop(self):
        self.running = False

    # Retorna o valor atual do contador (tempo decorrido)
    def get_counter(self):
        return self.counter

    # Incrementa o contador em 1 (simulando a passagem do tempo)
    def increment_counter(self):
        self.counter += 1
