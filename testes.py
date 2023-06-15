from Usuario import Usuario
from Medicamento import Medicamento
from Lembrete import Lembrete

def main():
    # criando usuario
    usuario = Usuario("João", "joao@gmail.com", "senha123", "60")
    medicamento1 = Medicamento("Paracetamol", "500mg")
    medicamento2 = Medicamento("Ibuprofeno", "200mg")

    #usuario.cadastrar_medicamento(medicamento1)
    #usuario.cadastrar_medicamento(medicamento2)

    medicamento1 = "Paracetamol"
    medicamento2 = "Ibuprofeno"
    usuario.cadastrar_medicamento(medicamento1)
    usuario.cadastrar_medicamento(medicamento2)

    # Consulta de medicamentos
    lista_medicamentos = usuario.consultar_medicamentos()
    print("Lista de Medicamentos:", lista_medicamentos)

    # Edição de medicamento
    novo_medicamento = "Aspirina"
    usuario.editar_medicamento(0, novo_medicamento)

    # Consulta de medicamentos após edição
    lista_medicamentos = usuario.consultar_medicamentos()
    print("Lista de Medicamentos após edição:", lista_medicamentos)

    # Login do usuário
    email = "joao@gmail.com"
    senha = "senha123"
    if usuario.fazer_login(email, senha):
        print("Login realizado com sucesso!")
    else:
        print("Falha no login!")

    medicamento = "Ibuprofeno"
    dosagem = "200 mg"
    data = "13/06/2023"
    horario = "10:00"

    Lembrete.criar_alarme(medicamento, dosagem, data, horario)
    
    #teste lembrete
    medicamento1 = Medicamento(1, "Paracetamol")
    lembrete1 = Lembrete("08:00", "13/06/2023", "200 mg", medicamento1)

    lembrete1.ativar_notificacao()
    lembrete1.enviar_notificacao()

    lembrete1.desativar_notificacao()
    lembrete1.enviar_notificacao()


#teste lembrete


if __name__ == "__main__":
    main()