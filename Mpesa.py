import time

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
        message = f"Saldo atua: {self.balance}"
        return message

class Transition:
    def __init__(self, sender, recipient, ammount):
        self.sender = sender
        self.recipient = recipient
        self.ammount = ammount
        self.data = time.strftime("%Y-%m-%d %H:%M:%S")

    def show_details(self):
        print(f"Remetente: {self.sender.name.title()}")
        print(f"Destinatário: {self.recipient.name.title()}")
        print(f"Valor da transição: {self.ammount} Meticais")
        print(f"Data da transição: {self.data}")

class Mpesa:
    def __init__(self):
        self.users = []

    def register_user(self, name, phone_number):
        user = User(name, phone_number)
        self.users.append(user)

    def find_user(self,phone_number):
        for user in self.users:
            if user.phone_number == phone_number:
                return user
        return none

    def transfer(self, sender_phone, recipient_phone, ammount):
        sender =  self.find_user(sender_phone)
        recipient = self.find_user(recipient_phone)
        if sender and recipient:
            if sender.balance >= ammount:
                sender.balance -= ammount
                recipient.balance += ammount
                transaction = Transition(sender, recipient, ammount)
                transaction.show_details()
            else:
                print("Saldo insuficiente para a transferência")
        else:
            print("Usuário remetemte ou destinatário não encontrado")




# Example
mpesa = Mpesa()
mpesa.register_user("teddy", 847725920)
mpesa.register_user("ian", 857725920)

teddy = mpesa.find_user(847725920)
teddy.deposit(1000)
teddy.withdraw(500)
mpesa.transfer(847725920, 857725920, 300)
print(teddy.consult())
print("=============================================================================================")

ian = mpesa.find_user(857725920)
print(felicina.consult())
ian.withdraw(1000)