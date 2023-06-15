class Medicamento:
    def __init__(self, nome, dosagem):
        self.nome = nome
        self.dosagem = dosagem
    
    def editar_dosagem(self, nova_dosagem):
        self.dosagem = nova_dosagem


class ListaMedicamentos:
    def __init__(self):
        self.medicamentos = []
    
    def adicionar_medicamento(self, medicamento):
        self.medicamentos.append(medicamento)
    
    def editar_medicamento(self, indice, nova_dosagem):
        medicamento = self.medicamentos[indice]
        medicamento.editar_dosagem(nova_dosagem)

    