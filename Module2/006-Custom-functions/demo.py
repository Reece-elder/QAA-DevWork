# Python function
def greeting(name):
    # f String within python lets you insert a variable directly in
    print(f"Hello {name} how are you?")

greeting("Reece")

# Generally Functions should do ONE thing, the above is creating a string AND printing it
# We should just return the string so another function can print it

def greetReturn(name):
    text = f"Hello {name} how are you?"
    return text

print(greetReturn("cool reece"))

# the variable we pass into a function can be anything, when passing a function into another it is called a 'callback'
def greetCallback(function):
    return f"Hello {function}, how are you?"

def nameFunc(name):
    return name

print(greetCallback(nameFunc("reece")))

# Scope - Variables declared INSIDE of a function cannot be accessed outside of it
def sum(x, y):
    total = x + y
    text = "Hello"
    return total

# print(total) 
# print(text)
print(sum(12,8))