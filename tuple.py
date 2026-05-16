'''Tuples
(1) What is tuple: tuple vs list
(2) Unpacking arguments
(3) ZIP
'''

print("===== What is tuple: tuple vs list ======")

# literal
nums = [2, 5, 6, 7]
# car_dict = {"brand": "Aventador", "year": 2023}
print(nums)

# constructor
letters = list("Hello World!")
print(letters)


fruits = ["apple", "lemon", "banana", "kiwi"]
print("before fruits: ", fruits)

fruits[2] = "melon"
print("after fruits: ", fruits)  # we can change it when it *list*

animals = ("dog", "cat", "fish", "lion")
tuple_obj = ("MIT", 100, True)
print(animals)

people = "Lincoln", "Masha"
animal = "dog",

print("===== Unpacking arguments ======")
groups = ["MIT", "FLEXY", "DEVEX",]
(x, y, z, a) = groups
(x, y, *z) = groups

print(f"the x is {x} and y is {y}")
print(z)


def calculate(*args):
    print("args >", args)
    total = 1
    for x in args:
        total *= x
    print(f"the type(args) value: {type(args)}")
    print(f"the total value: {total}")


# CALL
calculate(1, 7, 2, 9)
print("--------------")
calculate(0, 9, 4)
print("--------------")
calculate(2, 9)

# **kwargs > dictionary


def introduce(**kwargs):
    print(f"Type of **kwargs {type(kwargs)}")
    print(f"Hi, I am {kwargs["name"]} and I am {kwargs["age"]} years old!")


introduce(name="JackMa", age=86)


def greeting(*args, **kwargs):
    print("*args >", args)
    print("**kwargs >", kwargs)


greeting("hi", True,  10, name="JackMa", age=86)


print("===== zip ======")
tuple1 = (1, 2, 3, 4, 5)
tuple2 = ('a', 'b', 'c', 'd')

zipped = zip(tuple1, tuple2)
print("zipped", zipped)

result = list(zipped)
print(result)
