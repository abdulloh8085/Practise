"""FUNCTIONS
(1) Define & Call
(2) Parametr & Argument
(3) Keyword & default arguments
(4) Scope
"""

print("===== Define & Call =====")
# builtin in functions > print() type()
# Functions - reusable block of code!
# Instead of block {} in JAVA, Python uses indentation!


# DEFINE - Build qism
# Void fumction
def greet(a):  # Define qismda kelga ==>"(a)"<== bu parametr deb xisoblanadi va aytiladi
    print(f"How do you do, {a}")

# Return function


def greeting(b):
    print("greeting is executed")
    return f"Hi {b}"


# CALL - Execute qism

# Call qismda berilgan value ==> 'Martin' <== argument deb ataladi
result1 = greet('Martin')
print("result1:", result1)

result2 = greeting("Justin")
print("result2:", result2)

print("=====  Keyword & Default arguments =====")

# DEFINE


def give_greet(name, age=22):
    print("give_greet is executed")
    return f"Hi {name}, you are only {age} years old!"

# CALL


result3 = give_greet(name="Justin", age=28)
print("result3:", result3)

# Default argument
result4 = give_greet("John",)
print("result4:", result4)

print("=====  SCOPE =====")
b = 100

# Define


def calculate(a):
    c = a * b
    print(f"The c value: {c}")

 # Call
calculate(5)
