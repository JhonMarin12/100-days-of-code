# Subcripting
print("Hello"[0]) # H
print("Hello"[-1]) # o

# String concactenation
print("123" + "345")

# Integer
print(123 + 567)

# Large integer
print(321_123_987)

# Float = Floating point number
print(3.1415)

# Boolean
print(True)
print(False)

# Len function
# print(len(123)) -> Error
print(len("123"))

# Type function
print(type("123")) # <class 'str'>
print(type(12)) # <class 'int'>

# Type casting
print(type(str(123)))

# Addition
print(5 + 3)  # 8

# Subtraction
print(10 - 4)  # 6

# Multiplication
print(6 * 7)  # 42

# Division (always returns a float)
print(10 / 3)  # 3.3333333333333335

# Floor Division (integer division)
print(10 // 3)  # 3

# Modulus (remainder)
print(10 % 3)  # 1

# Exponentiation (power)
print(2 ** 3)  # 8

# Order of operations (PEMDAS)
print(2 + 3 * 4)  # 14 (Multiplication first)
print((2 + 3) * 4)  # 20 (Parentheses first)
