# mziuri sashinao davaleba 5

# davaleba 1
# number = int(input("Enter a number: "))
# divisors = [i for i in range(1, number + 1) if number % i == 0]
# print("Divisors of", number, "are:", divisors)

# davaleba 2
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# common_divisors = [i for i in range(1, min(num1, num2) + 1) if num1 % i == 0 and num2 % i == 0]
# print("Common divisors of", num1, "and", num2, "are:", common_divisors)

# davaleba 3
# num1 = int(input("Enter the first positive integer: "))
# num2 = int(input("Enter the second positive integer: "))
# gcd = 1
# for i in range(1, min(num1, num2) + 1):
#     if num1 % i == 0 and num2 % i == 0:
#         gcd = i
#
# print("The greatest common divisor of", num1, "and", num2, "is:", gcd)

# davaleba 4
# num1 = int(input("Enter the first positive integer: "))
# num2 = int(input("Enter the second positive integer: "))
# if num1 > num2:
#     lcm = num1
# else:
#     lcm = num2
# while True:
#     if lcm % num1 == 0 and lcm % num2 == 0:
#         break
#     lcm += 1
# print("The least common multiple of", num1, "and", num2, "is:", lcm)

# davaleba 5
# largest_odd = 0  # Start with 0, assuming there are no odd numbers
# for _ in range(10):
#     number = int(input("Enter a number: "))
#     if number % 2 != 0:
#
#         if number > largest_odd:
#             largest_odd = number
# if largest_odd > 0:
#     print("The largest odd number is:", largest_odd)
# else:
#     print("No odd number was entered.")
