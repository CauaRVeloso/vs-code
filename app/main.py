class Main:
    pass

from Cliente import Cliente
from Conta import Conta

c1= Cliente("Jonas", "61 99962-1234", "825.575.731-49")
conta=Conta(c1._nome,2313,0)

conta.depositar(400)
conta.saque(200)
conta.extrato()



