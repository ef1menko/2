reverser_time = int(input('�� ������� c��. ��������� �����?: '))
print()
for time in range (reverser_time, 0, -1):
    print('�������� �������: ', time, '���.')
    button = int(input('�������� (�� -1, ��� -0): '))
    print()
    if button == 1:
        print('���� ��� ������, ������ ������� ', '\n����������: ', time, '���.')
        break
    elif button ==0:
        continue
print('��������� �����o!')