class Usuario:
    def __init__(self, nome, CPF, senha, IdadeUsuario):
        self._nome = nome
        self._CPF = CPF
        self._senha = senha
        self._IdadeUsuario = IdadeUsuario
        self._lista_medicamentos = []

    def cadastrar_medicamento(self, medicamento):
        self._lista_medicamentos.append(medicamento)

    def editar_medicamento(self, indice, medicamento):
        if indice >= 0 and indice < len(self._lista_medicamentos):
            self._lista_medicamentos[indice] = medicamento

    def consultar_medicamentos(self):
        return self._lista_medicamentos

    def fazer_login(self, CPF, senha):
        if CPF == self._CPF and senha == self._senha:
            return True
        else:
            return False

    def calculaIdade(self, idadeUsuario):
        idade_atual = 2023 - idadeUsuario
        return idade_atual
