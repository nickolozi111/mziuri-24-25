# homework n17

# davaleba 1
# tuple_of_cubes = tuple(x**3 for x in range(5, 101, 5))
#
# tuple_length = len(tuple_of_cubes)
# print(tuple_length)

# davaleba 2
# tuple_of_cubes = tuple(x**3 for x in range(5, 101, 5))
#
# iterator = iter(tuple_of_cubes)
#
# try:
#     while True:
#         print(next(iterator))
# except StopIteration:
#     pass

# davaleba 3
# set_of_cubes = {x**3 for x in range(5, 101, 5)}
#
# average = sum(set_of_cubes) / len(set_of_cubes)
# print(f"Arithmetic mean of set elements: {average}")

# davaleba 4
# set_of_cubes = {x**3 for x in range(5, 101, 5)}
#
# iterator = iter(set_of_cubes)
#
# try:
#     while True:
#         print(next(iterator))
# except StopIteration:
#     pass

# davaleba 5
# def number_generator():
#     for i in range(1, 6):
#         yield i
#
# gen_iterator = number_generator()
#
# try:
#     while True:
#         print(next(gen_iterator))
# except StopIteration:
#     pass
