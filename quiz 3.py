# mziuris quiz n3

# question 1
# def string_lengths(str_list):
#     return [len(s) for s in str_list]
#
# strings = ["apple", "banana", "cherry", ""]
# lengths = string_lengths(strings)
#
# print(lengths)

# question 2
# def unique_elements(list1, list2):
#
#     set1 = set(list1)
#     set2 = set(list2)
#
#     return list(set1 ^ set2)
#
# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]
#
# unique = unique_elements(list1, list2)
#
# print(unique)

# question 3
# def create_dict_and_print(people_list):
#
#     people_dict = dict(people_list)
#
#
#     for name, age in people_dict.items():
#         print(f"Name: {name}, Age: {age}")
#
# people = [("Jasur", 90), ("Beki", 25)]
# create_dict_and_print(people)

# # question 4
# def check_product_availability(products_dict):
#     result = []
#
#     for product, quantity in products_dict.items():
#         if quantity > 5:
#             result.append((product, "Enough"))
#         else:
#             result.append((product, "Not enough"))
#
#     return result
#
# products = {'eggplant': 3, 'onion': 6, 'cabbage': 2}
# availability = check_product_availability(products)
#
# print(availability)

# question 5
# def words_starting_with_a(words_list):
#     result_dict = {}
#
#     for word in words_list:
#         if word.lower().startswith('a'):
#             result_dict[word] = len(word)
#
#     return result_dict
#
# words = ["apple", "banana", "avocado", "grape", "apricot", "berry"]
# result = words_starting_with_a(words)
#
# print(result)

# question 6
# remove(): წაშლის პირველი ნაპოვნი ელემენტი სიმრავლეში, რომელიც შეესაბამება მოცემულ მნიშვნელობას.
# pop(): წაშლის ელემენტს ინდექსით და აბრუნებს წაშლილ მნიშვნელობას.
# clear(): ამოიღებს ყველა ელემენტს სიიდან.

# question 7
# ტუპლი: ელემენტების მოწესრიგებული, უცვლელი კოლექცია. მისი შექმნის შემდეგ, ელემენტების შეცვლა, დამატება ან ამოღება შეუძლებელია.
# სია: ელემენტების მოწესრიგებული, ცვალებადი კოლექცია. მისი შექმნის შემდეგ, ელემენტების შეცვლა, დამატება ან წაშლა შესაძლებელია.

# question 8
# union(): აერთიანებს ორი სიმრავლე.
# intersection(): დააბრუნებს მხოლოდ საერთო ელემენტებს ორი სიმრავლიდან.
# difference(): დააბრუნებს ელემენტებს, რომლებიც მხოლოდ პირველ სიმრავალში არსებობენ.
# symmetric_difference(): დააბრუნებს ელემენტებს, რომლებიც მხოლოდ ერთ-ერთი სიმრავლეში არიან, მაგრამ არა ორივეში.

# question 9
# my_dict[key] = value

# question 10
# my_dict.items()

# question 11
# თუ არ ხართ დარწმუნებული, რამდენი არგუმენტი გადაეცემა ფუნქციას, გამოიყენეთ *args ცვლადი რაოდენობის პოზიციური არგუმენტებისთვის ან **kwargs საკვანძო სიტყვების არგუმენტების ცვლადი რაოდენობისთვის.

