letter = int(input('������� ����� ������� ������: '))
step = letter // 4
count = 0
size = 12
for i in range(letter, 12, - step):
  if size < letter:
    size *= 2
    count += 2
print(count, '��� ��j����� ����� ������� �������')