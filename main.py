# This is a sample payroll program in python

# This line helps to import time
from time import*

# The code below prompts the user to enter their weekly,monthly and annual pay
salary_input = int(input('enter your weekly pay : '))
salary_input_2 = int(input('enter your monthly pay : '))
salary_input_3 = int(input('enter your annual pay : '))

# This block of code takes what the user entered and divide it by 5
weekly_pay_result = salary_input/5
monthly_pay_result = salary_input_2/5
annual_pay_result = salary_input_3/5

# The code below is a number of if and elif statements that
# helps to calculate the user's weekly, monthly and annual pay
if salary_input >= 1:
    print('calculating.....')
    sleep_time = ''
    sleep(5)
    print('your weekly salary is : ', weekly_pay_result)
elif salary_input <= 0:
    print('ERROR : that is an invalid input!. Weekly pay cannot be 0')

if salary_input_2 >= 1:
    print('calculating....')
    sleep_time = ''
    sleep(4)
    print('your monthly salary is : ', monthly_pay_result)
elif salary_input_2 <= 0:
    print('ERROR : invalid input!. Monthly pay cannot be 0')

if salary_input_3 >= 1:
    print('calculating....')
    sleep_time = ''
    sleep(3)
    print('your annual salary is : ', annual_pay_result)
elif salary_input_3 <= 0:
    print('ERROR : invalid input!. Annual pay cannot be 0')
