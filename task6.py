day1 = int(input('how many kilometers a sportsman runs first day: '))
distance = int(input('what is the distance: '))
day = 1
while day1 <= distance:
    day1 = 1.1 * day1
    day +=1
print('Спортсмен достигнет результата на %.d' % day, 'день')