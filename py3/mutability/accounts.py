accounts = {
    'checking': 1958.00,
    'savings': 3695.50
}


def add_balance(amount: float, name: str = 'checking') -> float:
    accounts[name] += amount
    return accounts[name]


add_balance(500.00, 'savings')

print(accounts)
