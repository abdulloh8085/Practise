def getHighestIndex(numbers):

    highest = numbers[0]
    highest_index = 0

    for i in range(len(numbers)):

        if numbers[i] > highest:
            highest = numbers[i]
            highest_index = i

    return highest_index


numbers1 = [5, 21, 12, 21, 8]
result1 = getHighestIndex(numbers1)
print(result1)

numbers2 = [1, 2, 3, 4, 5]
result2 = getHighestIndex(numbers2)
print(result2)

numbers3 = [99, 12, 45, 67]
result3 = getHighestIndex(numbers3)
print(result3)

numbers4 = [7, 7, 7, 7]
result4 = getHighestIndex(numbers4)
print(result4)

numbers5 = [-5, -1, -9, -3]
result5 = getHighestIndex(numbers5)
print(result5)
