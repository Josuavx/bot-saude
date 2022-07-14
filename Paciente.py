class Paciente():
    def __init__(self, id, nome, email):
        self.id = id
        self.nome = nome
        self.email = email

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id
    
    def getNome(self):
        return self.nome
    
    def setNome(self, nome):
        self.nome = nome
    
    def getEmail(self):
        return self.email
    
    def setEmail(self, email):
        self.email = email
