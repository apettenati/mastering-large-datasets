from toolz import compose

def double_number(original_number):
    return original_number, original_number * 2

def add_10(numbers):
    original_number, number = numbers
    return original_number, number + 10

def half_number(numbers):
    original_number, number = numbers
    return original_number, number // 2

def subtract_number(numbers):
    original_number, number = numbers
    return number - original_number

trick = compose(subtract_number, half_number, add_10, double_number)
results = list(map(trick, range(1, 101)))
print(results)
