reverser_time = int(input('На сколько cек. поставить блюдо?: '))
print()
for time in range (reverser_time, 0, -1):
    print('Осталось греться: ', time, 'сек.')
    button = int(input('Прервать (Да -1, Нет -0): '))
    print()
    if button == 1:
        print('Ваша еда готова, можете забрать ', '\nОставалось: ', time, 'сек.')
        break
    elif button ==0:
        continue
print('Осторожно горячo!')