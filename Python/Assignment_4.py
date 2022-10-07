#4. Write functions to calculate and display grosssalary and netsalary of an employee after getting input as basicsalary
#Write separate functions for allowances and deductions to calculate them respectively

"""
netsalary = grosssalary - deductions
grosssalary = basicsalary + allowances

allowances = hra(22% of basicsalary) + da(18% of basicsalary) +ta(10% of basicsalary)

deductions = proftax(if basicsalary > 8000 the 200 else 150) + pf(12% of basicsalary) + insurance(8% of basicsalary)

"""

#code


def allowances(basic_salary):
    return ((0.22*basic_salary+0.18*basic_salary+0.10*basic_salary))
def deduction(basic_salary):
    if basic_salary > 8000:
        proftax = 200
    else :
        proftax = 150
    return ((proftax+0.12*basic_salary+0.08*basic_salary))
def salary(basic_salary):
    gross_salary= basic_salary+allowances(basic_salary)
    net_salary= gross_salary - deduction(basic_salary)
    print("\n Gross salary = ", gross_salary)
    print("\n Net salary =", net_salary)
basic_salary = float(input("Enter the Basic Salary\n"))
salary(basic_salary)

