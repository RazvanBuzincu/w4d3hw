# https://www.codewars.com/kata/5769b3802ae6f8e4890009d2/python
# ive used the following solution which is linear in time and space O(n)
def remove_every_other(my_list):
    return my_list[::2]


# https://www.codewars.com/kata/554b4ac871d6813a03000035/python
# ive used the following solution which is linear in time and space O(n)
def high_and_low(numbers):
    
    numbers_list = [int(num) for num in numbers.split()]

    
    highest = max(numbers_list)
    lowest = min(numbers_list)

    
    return f"{highest} {lowest}"

# https://www.codewars.com/kata/57356c55867b9b7a60000bd7/python
# # ive used the following solution which is constant time and space O(1)
def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        if value2 != 0:  
            return value1 / value2
        else:
            return "Cannot divide by zero"
    else:
        return "Invalid operator"