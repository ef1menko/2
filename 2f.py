debtors = int(input('Введите количество должников: '))
print()
credit = 0
for calls in range (0, debtors, 5):
    print('Должник номер:', calls)
    credit += int(input('Введите сумму долга: '))
    print()
print('Общая сумма долга: ', credit)