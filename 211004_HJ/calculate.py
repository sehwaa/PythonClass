def account_book(*pay):
    profit = 0
    for p in pay:
        profit += p
    return profit - 100

print(account_book(50, 3000, 100, 200))
print(account_book(500))
