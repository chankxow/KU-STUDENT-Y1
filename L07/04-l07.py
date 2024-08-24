class Coin:
  def __init__(self, value = 1):
    self.value = value

  def __str__(self):
    return f'{self.value} Baht Coin'

class BankNote:
  def __init__(self, value = 20):
    self.value = value

  def __str__(self):
    return f'{self.value} Baht Banknote'


amount = int(input('Input amount : '))

banks_stock = [
    BankNote(1000),
    BankNote(500),           
    BankNote(100),
    BankNote(50),
    BankNote(20)
]

coins_stock = [
    Coin(10),
    Coin(5),
    Coin(2),
    Coin(1)
]


for i in range(len(banks_stock)):
    if banks_stock[i].value <= amount:
        total = amount//banks_stock[i].value
        amount = amount%banks_stock[i].value
        print(f'You get {total} of {banks_stock[i]}')
        
for i in range(len(coins_stock)):
    if coins_stock[i].value <= amount:
        total = amount//coins_stock[i].value
        amount = amount%coins_stock[i].value
        print(f'You get {total} of {coins_stock[i]}')
        