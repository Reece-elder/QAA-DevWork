# Part 1 - Simple Tax

# Personal allowance:		£11,850	 
# 0 to 34,500 			taxed at 20%		
# 34,501 to 150,000 		taxed at 40%		
# Over 150,000 			taxed at 45%		


def getIncomeTax(salary):
    taxAmount = 0

    if salary < 11850:
        return f"Starting salary is {salary} which is within personal allowance 18,500, no tax is paid"
    elif salary < 34500:
        taxAmount = 20
    elif salary < 150000:
        taxAmount = 40
    else:
        taxAmount = 45

    taxableAmount = salary * (taxAmount / 100)
    return f"Starting salary is {salary}, taxable amount is {taxableAmount}, net money is {salary - taxableAmount}"

print(getIncomeTax(72000)) 


# Part 2 - Complex Tax
def getIncomeTaxComplex(salary):
    smallTax = 0
    mediumTax = 0
    largeTax = 0

    # 0 - 18500 is not taxed 
    # Leftover between 18500 and 34500 is taxed at 20% - need to work out how much of pay is between these values
    # leftover between 34501 and 150000 taxed at 40% - need to work out pay is between these values
    # Any money leftover is taxed at 45%

    if salary < 18500:
        return f"{Salary} less than allowance, no tax paid "
    
    if salary >= 18500:
        smallTax = (salary - 18500) * 0.2

    if salary > 34500: 
        mediumTax = (salary - 34500) * 0.4

    if salary > 150000:
        largeTax = (salary - 150000) * 0.45

    finalTax = smallTax + mediumTax + largeTax
    print (f"{salary} has total tax of {finalTax}, take home money is {salary - finalTax}")

    
    # if salary < 18500:
    #     return f"Starting salary is {salary} which is within personal allowance 18,500, no tax is paid"
    # elif salary < 34500:
    #     leftover -= 18500
    #     tax = leftover * 0.2

getIncomeTaxComplex(95000)

import random

def rollSix():
    return random.randint(1, 6)


