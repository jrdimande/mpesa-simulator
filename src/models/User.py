class User:
    def __init__(self, name, phone_number, balance = 0):
        self.name = name
        self.phone_number = phone_number
        self.balance = balance



    def show_balance(self):
        print(f"Saldo atual: {self.balance} Meticais")

    def deposit(self, ammount):
        if ammount > 0:
            self.balance += ammount
            print(f"Valor Depositado: {ammount}")
        else:
            print("O Valor depositado é inválido!")

    def withdraw(self, ammount):
        if self.balance >= ammount:
            self.balance -= ammount
            print(f"Efectuou o levantamento de {ammount} Meticais")
        else:
            print("Saldo insuficiente!")
            print(f"Saldo disponível {self.balance} Meticais")

    def consult(self):
        message = f"Saldo atual: {self.balance} Meticais"
        return message