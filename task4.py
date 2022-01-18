n = int(input('please enter positive integer: '))
print(n)
max = n % 10
while n >= 1:
    if n %10 > max:
        max = n % 10
    n = n // 10
print ('max number :', max)


