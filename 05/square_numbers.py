def square_numbers(numbers):
    result = map(lambda x:x**2, numbers)
    result = list(result)
    return result

print(square_numbers([1, -2, 3, 4]))
#lub tak:
#result = square_numbers([1, 2, 3, 4])
#print(result)