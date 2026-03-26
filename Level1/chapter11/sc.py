import time
def calclate_tax(income):
     return income*0.15
def calculate_total_salary(base_salary,bonus):
    total_salary=base_salary+bonus
    tax_to_pay=calclate_tax(total_salary)
    return total_salary -calclate_tax(total_salary)
base_salaty=float(input("Enter the base salary: "))
bonus=float(input("How much bons did you get?"))
print('Calculating start...')
time.sleep(3)
print(f"Final salary after tax: {calculate_total_salary(base_salaty,bonus)}")