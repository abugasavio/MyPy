number = input("Cash owed: ");

# convert dollars to cents

cents = float(number) * 100

print(cents)

quarters = 25
dimes = 10
nickles = 5
pennies = 1

coins_used_details = {}

if cents >= quarters:
    quarters_coins_used = cents // quarters
    cents = cents % quarters
    coins_used_details['quarters'] = quarters_coins_used

if cents >= dimes:
    dimes_coins_used = cents // dimes
    cents = cents % dimes
    coins_used_details['dimes'] = dimes_coins_used

if cents >= 5:
    nickles_coins_used = cents // nickles
    cents = cents % nickles
    coins_used_details['nickles'] = nickles_coins_used

coins_used_details['pennies'] = cents


print(coins_used_details)
print("Total Coins used {}".format(sum(coins_used_details.values())))
