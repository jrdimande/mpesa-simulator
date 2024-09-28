class Contabancaria():
    def __init__(self, num_cont, titular, saldo):
        self.num_cont = num_cont
        self.titular = titular
        self.saldo = saldo

    def depositar(self, quantia):
        self.saldo += quantia
        print(f"Deposito na conta corrente: {quantia} MTS")

    def levantar(self, quantia):
        if self.saldo >= quantia:
            self.saldo -= quantia
        else:
            print("Saldo insuficiente!")

    def exibir_saldo(self):

        print(f"O saldo atual é de {self.saldo} MTS")

class ContaCorrente(Contabancaria):
    def __init__(self, num_cont, titular, saldo, limite_cheque_especial):
        super().__init__(num_cont, titular)
        self.limite_cheque_especial = limite_cheque_especial

    def levantar(self, quantia):

        if quantia <= self.saldo + self.limite_cheque_especial:
            self.saldo -= quantia
        else:
            print(f"Saldo insuficiente, mesmo com cheque especial.")

        self.exibir_saldo()


