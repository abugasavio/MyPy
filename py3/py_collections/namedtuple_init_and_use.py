from collections import namedtuple

Account = namedtuple('Account', ['name', 'amount'])

account = Account('checking', 20000)

name, amount = account

print(account.name)
print(account.amount)
