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
