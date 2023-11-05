def countdown(num):
    if num < 0:
        return []
    else:
        return list(range(num, -1, -1))


result = countdown(5)
print(result)  


def print_and_return(numbers):
    if len(numbers) < 2:
        return None
    print(numbers[0])
    return numbers[1]


result = print_and_return([1, 2])
print(result)  


def values_greater_than_second(arr):
    if len(arr) < 2:
        return False

    new_list = [value for value in arr if value > arr[1]]
    print(len(new_list))
    return new_list


result = values_greater_than_second([5, 2, 3, 2, 1, 4])
print(result)  


result = values_greater_than_second([3])
print(result) 

def length_and_value(size, value):
    return [value] * size


result = length_and_value(4, 7)
print(result)  


result = length_and_value(6, 2)
print(result)  
