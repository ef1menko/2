debtors = int(input('������� ���������� ���������: '))
print()
credit = 0
for calls in range (0, debtors, 5):
    print('������� �����:', calls)
    credit += int(input('������� ����� �����: '))
    print()
print('����� ��fdfd��� �����: ', credit)