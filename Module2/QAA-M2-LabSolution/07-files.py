companies = []
sales = []

with open("carSale.csv", "r") as file:
    tempfile = file.read().splitlines()
    index = 0
    for line in tempfile:
        if index % 2 == 0: 
            companies.append(line)
        else: 
            sales.append(line)
        index += 1

print(companies)
print(sales)

# Sum of cars sold per month 
print(f"All sales from Ford {sales[0]}") # Will print all sales from Ford Motor Company
print(f"First month sales from Ford{sales[0].split(',')[0]}") # Print the number for all sales 

# Only for the first month
monthlySales = 0
for entry in sales:
    entry = entry.split(",")
    monthlySales = monthlySales + int(entry[0])
    
print(monthlySales)