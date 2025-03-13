# sashinao davaleba 12
#
# davaleba 1
# my_dict = {0: 10, 1: 20}
#
# my_dict.update({2: 30, 3: 40})
#
# print("Updated dictionary:", my_dict)
#
# del my_dict[1]
#
# print("Dictionary after deletion:", my_dict)

# davaleba 2
# dic1 = {1: 10, 2: 20}
# dic2 = {3: 30, 4: 40}
# dic3 = {5: 50, 6: 60}
#
# merged_dict = {}
#
# merged_dict.update(dic1)
# merged_dict.update(dic2)
# merged_dict.update(dic3)
#
# print("Merged dictionary:", merged_dict)

# davaleba 3
# d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
#
# key_to_check = 3
#
# if key_to_check in d:
#     print(f"Key {key_to_check} exists in the dictionary.")
# else:
#     print(f"Key {key_to_check} does not exist in the dictionary.")

# davaleba 4
# d = {'x': 10, 'y': 20, 'z': 30}
# #
# # for key in d:
# #
# #     print(f"{key} -> {d[key]}")

# davaleba 5
# cube_dict = {i: i**3 for i in range(1, 11)}
#
# print("Dictionary of cubes:", cube_dict)

# davaleba 6
# person = {}
#
#
# person["firstName"] = "Jane"
# person["lastName"] = "Doe"
# person["hobbies"] = ["running", "sky diving", "singing"]
# person["age"] = 35
# person["children"] = [
#     {"firstName": "Alice", "age": 6},
#     {"firstName": "Bob", "age": 8}
# ]
# print("Name:", person["firstName"], person["lastName"])
# print("Age:", person["age"])
#
#
# print("Hobbies:", ", ".join(person["hobbies"]))
#
# print("Children:", [child["firstName"] for child in person["children"]])
