from .Transition import Transition
from .User import User

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


