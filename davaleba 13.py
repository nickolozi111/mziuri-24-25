# sashinao davaleba

#  davaleba 1
# numbers = [1, 2, 3, 4, 5]
#
# with open("numbers.txt", "w") as file:
#     for number in numbers:
#         file.write(f"{number}\n")
#
# def square_numbers_and_print(input_filename):
#
#     with open(input_filename, 'r') as input_file:
#         numbers = input_file.readlines()
#
#     for number in numbers:
#         num = int(number.strip())
#         squared = num ** 2
#         print(f"The square of {num} is {squared}")
# square_numbers_and_print("numbers.txt")

# davaleba 2
# oscars_data = [
#     "2020,F,30,Renée Zellweger,Judy",
#     "2020,M,38,Joaquin Phoenix,Joker",
#     "2019,F,33,Olivia Colman,The Favourite",
#     "2019,M,44,Rami Malek,Bohemian Rhapsody"
# ]
#
# with open("oscars.txt", "w") as file:
#     for line in oscars_data:
#         file.write(f"{line}\n")
#
# def find_oscar_winners_by_year(input_filename, year):
#
#     with open(input_filename, 'r') as file:
#         lines = file.readlines()
#
#     winners = []
#
#
#     for line in lines:
#         fields = line.strip().split(',')
#         file_year = fields[0]
#
#         if file_year == str(year):
#             name = fields[3]
#             winners.append(name)
#
#
#     if winners:
#         print(f"Oscar winners for {year}:")
#         for winner in winners:
#             print(winner)
#     else:
#         print(f"No Oscar winners found for the year {year}.")
#
# year = input("Enter a year to search for Oscar winners: ")
# find_oscar_winners_by_year("oscars.txt", year)
