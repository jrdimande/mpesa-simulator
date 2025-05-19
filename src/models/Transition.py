import time

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