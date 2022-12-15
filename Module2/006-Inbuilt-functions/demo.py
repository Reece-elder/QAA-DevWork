numbers = [19,63,51,7,99,11,23,15,17,8]

# Standard numeric functions
print(min(numbers))
print(max(numbers))
print((numbers))
print(pow(2,3))
# (or 2**3)
print(abs(-123))

# Rounding Floats
print(round(5.671))
print(round(5.671,1))
print(round(5.671,2))
print(int(5.671))

# Formatting Strings
str = "hello"
print(str.lower())
print(str.upper())
print(str.title())
print(str.replace('e', 'a'))
print(str.center(14, '*'))
print(len(str))
print(f"{str.ljust(5)} World")

task = "5"
print(task.zfill(3))

# Split Function 
cities = "london,birmingham,leeds,manchester,bristol"
cityList = cities.split(',')
print(cities)
print(cityList)

# Checking data types
number = "12"
print(number.isdigit())

# String Formats
drink="mocha"
size="large"
extras="whipped cream"
order = "{} ordered at size {}. With {} added".format(drink, size, extras)
print(order) 


