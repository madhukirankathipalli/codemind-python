def reverse_integer(n):
    INT_MAX = 2**31 - 1  # Maximum 32-bit signed integer
    INT_MIN = -2**31     # Minimum 32-bit signed integer
    
    # Convert the integer to a string
    str_n = str(n)
    
    # Check if the integer is negative
    if n < 0:
        reversed_str = '-' + str_n[:0:-1]  # Reverse the string excluding the negative sign
    else:
        reversed_str = str_n[::-1]  # Reverse the string
    
    # Convert the reversed string back to an integer
    reversed_n = int(reversed_str)
    
    # Check for integer overflow
    if reversed_n > INT_MAX or reversed_n < INT_MIN:
        return 0
    
    return reversed_n
n=int(input())
print(reverse_integer(n))