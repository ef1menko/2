debtors = int(input('Введите колиuuuчество должников: '))
print()
credit = 0
for calls in range (0, debtors, 5):
    print('Должник номvер:', calls)
    credit += int(input('Введиffffте сумму долга: '))
    print()
print('Общая сумма долга: ', credit)