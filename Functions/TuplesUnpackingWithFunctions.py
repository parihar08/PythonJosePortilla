stock_prices = [('AAPL',126.97),('TSLA',407),('FB',295.90),('UBER',34.36)]

for item in stock_prices:
    print(item)

#Tuple Unpacking
for ticker,price in stock_prices:
    print(ticker)
    print(price+(0.15*price))
    print('******************************')

#Tuple unpacking with function
#Find employee of the month who worked maximum hours

work_hours = [('Abby',2000),('Billy',1000),('Cassie',800)]

def employee_check(work_hours):

    current_max =0
    employee_of_month = ''

    for employee,hours in work_hours:
        if hours > current_max:
            current_max =hours
            employee_of_month =employee
        else:
            pass
    #Return
    return(employee_of_month,current_max)

print(employee_check(work_hours))
result=employee_check(work_hours)
print(result)

name,hours=employee_check(work_hours)
print(name,hours)