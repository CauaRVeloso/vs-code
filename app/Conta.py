class Conta:
    def __init__(self, titular, numero, saldo):
        self.titular=titular
        self.numero=numero
        self.saldo=0

    def saque(self, valor):
        if (self.saldo>=valor):
            self.saldo-=valor
            print("Saque realizado com sucesso")
        else:
            print("Saldo insuficiente")

    def depositar(self, valor):
        self.saldo+=valor

    def extrato(self):
        print("Cliente: ", self.titular, "Saldo atual:", self._saldo)

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        if(saldo < 0):
            print("Saldo invalido, não pode ser negativo")
        else:
            self._saldo = saldo