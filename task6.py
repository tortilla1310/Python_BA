current_day_distance = int(input('how many kilometers a sportsman runs first day: '))
distance = int(input('what is the distance: '))
day = 1
while current_day_distance <= distance:
    current_day_distance = 1.1 * current_day_distance
    print( day, 'day', round(current_day_distance,2))
    day +=1
print('Спортсмен достигнет результата на %.d' % day, 'день')
