class Cliente:
    def  __init__(self, n, cel, cpf):
        self._nome = n
        self._telefone = cel
        self._cpf = cpf


    #metodo get
    def get_nome(self):
        return self._nome

    #metodo set
    def set_nome(self, nome):
        self._nome = nome
