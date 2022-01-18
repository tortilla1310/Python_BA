revenue = int(input('please provide profit of the company: '))
expenses = int(input('please provide expenses of the company: '))
print(revenue)
print(expenses)

if revenue > expenses:
    print('Financial result = revenue: ', revenue)
else:
    print('Financial result = expenses: ', expenses)

profit = revenue-expenses
print('profit = ', profit)
profitRatio = round(profit / revenue * 100)
if profit > 0:
    print('Ratio of profit to revenue =', profitRatio)
else:
    print('no profit this time')

amountEmployees = int(input('please provide a number of employees: '))
profitPerEmployee = profit // amountEmployees
print(' profit per employee = ', profitPerEmployee)
