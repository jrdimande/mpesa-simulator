from models.Transition import Transition
from models.Mpesa import Mpesa
from models.User import User




# Example
mpesa = Mpesa()
mpesa.register_user("george", 100)
mpesa.register_user("zuck", 200)

george = mpesa.find_user(100)
george.deposit(100)
george.withdraw(50)
mpesa.transfer(100, 200, 10)
print(george.consult())
print("=" * 50)

zuck = mpesa.find_user(200)
zuck.withdraw(10)
mpesa.transfer(200, 100, 10)
print(zuck.consult())