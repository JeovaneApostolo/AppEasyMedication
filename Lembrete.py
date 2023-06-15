import datetime
import time
import winsound

class Lembrete:
    def __init__(self, horario, data, dosagem, medicamento):
        self.horario = horario
        self.data = data
        self.dosagem = dosagem
        self.medicamento = medicamento
        self.notificacao_ativa = False
    
    def criar_alarme(medicamento, dosagem, data, horario):
        while True:
            agora = datetime.datetime.now()
            alarme = datetime.datetime.strptime(data + ' ' + horario, '%d/%m/%Y %H:%M')
            
            if agora >= alarme:
                print(f"Alarme para {medicamento}! Hora de tomar {dosagem}.")
                winsound.Beep(1000, 1000)  # Emite um som de alarme (Windows)
                break
            
            time.sleep(60)

    def ativar_notificacao(self):
        self.notificacao_ativa = True
        print("Notificação ativada")

    def desativar_notificacao(self):
        self.notificacao_ativa = False
        print("Notificação desativada")

    def enviar_notificacao(self):
        if self.notificacao_ativa:
            mensagem = f"Lembrete: É hora de tomar {self.dosagem} de {self.medicamento.nome}"
            print(mensagem)
        else:
            print("Notificação desativada")

