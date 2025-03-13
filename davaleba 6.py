# mziuri sashinao davaleba 6

# davaleba 1
# def is_prime(num):
#     if num < 2:
#
#         pass
#     else:
#         is_prime_number = True
#         for i in range(2, int(num**0.5) + 1):
#             if num % i == 0:
#                 is_prime_number = False
#                 break
#         if is_prime_number:
#             print(num)  #
#
# for number in range(2, 1001):
#     is_prime(number)

# davaleba 2
# def fibonacci_up_to_100():
#     a, b = 0, 1
#     while a <= 100:
#         print(a)
#         a, b = b, a + b
#
# fibonacci_up_to_100()

# davaleba 3
# def count_digits(num):
#     num = abs(num)
#     count = 0
#
#     if num == 0:
#         count = 1
#
#     while num > 0:
#         num //= 10
#         count += 1
#
#     print(count)
#
# number = int(input("Enter any integer: "))
# count_digits(number)

# davaleba 4
# def sum_of_digits(num):
#     num = abs(num)
#     total = 0
#
#     while num > 0:
#         total += num % 10
#         num //= 10
#
#     print(total)
#
#
# number = int(input("Enter any integer: "))
# sum_of_digits(number)

# davaleba 5
# def first_digit(num):
#     num = abs(num)
#
#     while num >= 10:
#         num //= 10
#
#     print(num)
#
# number = int(input("Enter any integer: "))
# first_digit(number)
