# Dunder __biiltins__, __init__

message = ("Python: Everything is object!")
print(message)

result = type(message)
print("result:", result)

""" In Python,  there are builtin tools:
(1) Types > int float str list dict
(2) Function > print() len() input()
(3) Constants > True False None
"""

print(dir(__builtins__))
