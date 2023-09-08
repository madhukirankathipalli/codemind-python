def is_self_dividing(num):
    for digit in str(num):
        if digit == '0' or num % int(digit) != 0:
            return False
    return True

def self_dividing_numbers(left, right):
    result = []
    for num in range(left, right + 1):
        if is_self_dividing(num):
            result.append(num)
    return result

# Example usage:
lower_bound = int( input())
upper_bound = int( input())
result = self_dividing_numbers(lower_bound, upper_bound)
output = ' '.join(map(str, result))
print(output)
