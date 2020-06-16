class Usuario:
    def __init__(self):
        self._nome = ""
        self._cpf = ""
        self._email = ""

    def getNome(self):
        return self._nome

    def setNome(self, nome):
        self._nome = nome

    def getCpf(self):
        return self._cpf

    def setCpf(self, cpf):
        self._cpf = cpf

    def getEmail(self):
        return self._email

    def setEmail(self, email):
        self._email = email

    def appendNome(self,caracter):
        self._nome += caracter

    def backspaceNome(self):
        self._nome = self._nome[:-1]

    def appendCpf(self,caracter):
        self._cpf += caracter

    def backspaceCpf(self):
        self._cpf = self._cpf[:-1]

    def appendEmail(self,caracter):
        self._email += caracter

    def backspaceEmail(self):
        self._email = self._email[:-1]