# sashinao davaleba

# davaleba 1
# students = {
#     "Alice": {"Math": 85, "Science": 90},
#     "Bob": {"Math": 75, "History": 80},
#     "Charlie": {"Math": 88, "English": 92}
# }
#
# def add_student(students, name, grades):
#     students[name] = grades
#     print(f"{name} added successfully.")
#
# def update_grade(students, name, subject, grade):
#     if name in students:
#         students[name][subject] = grade
#         print(f"Grade for {subject} updated to {grade}.")
#     else:
#         print(f"{name} not found in the student list.")
#
# def calculate_average(students, name):
#     if name in students:
#         grades = students[name].values()
#         average = sum(grades) / len(grades)
#         print(f"Average grade for {name}: {average}")
#     else:
#         print(f"{name} not found in the student list.")
#
# def display_student(students, name):
#     if name in students:
#         print(f"Student: {name}")
#         for subject, grade in students[name].items():
#             print(f"{subject}: {grade}")
#     else:
#         print(f"{name} not found in the student list.")
#
# add_student(students, "David", {"Math": 92, "History": 84})
# update_grade(students, "Alice", "Math", 95)
# calculate_average(students, "Bob")
# display_student(students, "Charlie")

# davaleba 2
# person = {
#     "name": "John Doe",
#     "age": 30,
#     "city": "New York",
#     "occupation": "Software Engineer"
# }
#
# print(person)

# davaleba 3
# person = {
#     "name": "John",
#     "age": 30,
#     "city": "New York",
#     "occupation": "Engineer"
# }
#
# person["hobby"] = "Eating and sleeping"
#
# del person["occupation"]
#
# print(person)
#

# davaleba 4
# dict1 = {"a": 1, "b": 2}
# dict2 = {"c": 3, "d": 4}
#
# def merge_dictionaries(dict1, dict2):
#     merged = dict1.copy()
#     merged.update(dict2)
#     return merged
#
# result = merge_dictionaries(dict1, dict2)
# print(result)

# davaleba 5
# sample_dict = {"a": 5, "b": 15, "c": 20, "d": 8}
#
# def filter_dictionary(d):
#     return {key: value for key, value in d.items() if isinstance(value, (int, float)) and value > 10}
#
# filtered_dict = filter_dictionary(sample_dict)
# print(filtered_dict)

# davaleba 6
# numbers = [1, 2, 3, 4, 5]
#
# cubed_dict = {num: num**3 for num in numbers}
# print(cubed_dict)

# davaleba 7
# sample_list = [1, 2, 2, 3, 3, 3, 4]
#
# def frequency_counter(lst):
#     frequency = {}
#     for item in lst:
#         frequency[item] = frequency.get(item, 0) + 1
#     return frequency
#
# print(frequency_counter(sample_list))

# davaleba 8
# sample_dict = {"a": 1, "b": 2, "c": 2, "d": 3}
#
# def invert_dictionary(d):
#     inverted = {}
#     for key, value in d.items():
#         if value in inverted:
#             inverted[value].append(key)
#         else:
#             inverted[value] = [key]
#     return inverted
#
# inverted_dict = invert_dictionary(sample_dict)
# print(inverted_dict)
