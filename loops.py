'''LOOOP
(1) FOR LOOP
(2) BREAK, ELSE
(3) WHILE LOOP
'''

print("===== for =====")

text = "MIT"
nums = [1, 4, 6, 7]
car_obj = dict(name="Aventador", year=2023)
range_obj = range(5)

for letter in text:
    print(letter)

print("--------------")
for number in nums:
    print(number)

print("--------------")
for ele in range_obj:
    print(ele)

print("--------------")
for key in car_obj:
    print(f"the key {key} => value {car_obj.get(key)}")

print("--------------")

for x in range(1, 20, 4):
    print(x)


print("===== break/else =====")
for x in range(1, 20, 2):
    print(x)
    if x > 10:
        print("reached to break point")
        break
else:
    print("Looped Successfully")  # Agar break bulmasa ishga tushaveradi

numb = 40

while numb > 0:
    numb -= 10
    print("numbers:", numb)

print("--------------")
count = 0
while True:
    count += 1
    x = int(input("Enter number: "))

    if x == 41:
        print(f"You found number! Total attempts {count}")
        break
    else:
        print("Something went wrong plz Try again!")
