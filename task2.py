time = int(input('print time in seconds: '))
print(time)

hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = time - (hours * 3600 + minutes * 60)
print('time in "чч:мм:сс" =', hours, ":", minutes, ":", seconds)