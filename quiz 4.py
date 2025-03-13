# quiz n4

# question 1
# with open('titanic.txt', 'r') as file:
#     lines = file.readlines()
#
# data = [line.strip().split(',') for line in lines[1:]]
#
# num_females = num_males = num_class_1 = num_class_2 = num_class_3 = 0
# num_females_survived = num_females_died = num_males_survived = num_males_died = 0
# total_fare_class_1 = total_fare_class_2 = total_fare_class_3 = 0
# count_class_1 = count_class_2 = count_class_3 = 0
#
# for row in data:
#     sex = row[4].lower()
#     survived = int(row[1])
#     pclass = int(row[2])
#     fare = row[9] if row[9] else '0'
#     fare = float(fare)
#
#     if sex == 'female':
#         num_females += 1
#         if survived == 1:
#             num_females_survived += 1
#         else:
#             num_females_died += 1
#     elif sex == 'male':
#         num_males += 1
#         if survived == 1:
#             num_males_survived += 1
#         else:
#             num_males_died += 1
#
#     if pclass == 1:
#         num_class_1 += 1
#         total_fare_class_1 += fare
#         count_class_1 += 1
#     elif pclass == 2:
#         num_class_2 += 1
#         total_fare_class_2 += fare
#         count_class_2 += 1
#     elif pclass == 3:
#         num_class_3 += 1
#         total_fare_class_3 += fare
#         count_class_3 += 1
#
# female_percentage = (num_females / len(data)) * 100
# male_percentage = (num_males / len(data)) * 100
# female_survival_percentage = (num_females_survived / num_females) * 100 if num_females else 0
# female_death_percentage = (num_females_died / num_females) * 100 if num_females else 0
# male_survival_percentage = (num_males_survived / num_males) * 100 if num_males else 0
# male_death_percentage = (num_males_died / num_males) * 100 if num_males else 0
# class_1_percentage = (num_class_1 / len(data)) * 100
# class_2_percentage = (num_class_2 / len(data)) * 100
# class_3_percentage = (num_class_3 / len(data)) * 100
#
# average_fare_class_1 = total_fare_class_1 / count_class_1 if count_class_1 else 0
# average_fare_class_2 = total_fare_class_2 / count_class_2 if count_class_2 else 0
# average_fare_class_3 = total_fare_class_3 / count_class_3 if count_class_3 else 0
#
# statistics = {
#     "Number of Females": num_females,
#     "Female Percentage": female_percentage,
#     "Number of Males": num_males,
#     "Male Percentage": male_percentage,
#     "Females Survived": num_females_survived,
#     "Females Died": num_females_died,
#     "Female Survival Percentage": female_survival_percentage,
#     "Female Death Percentage": female_death_percentage,
#     "Males Survived": num_males_survived,
#     "Males Died": num_males_died,
#     "Male Survival Percentage": male_survival_percentage,
#     "Male Death Percentage": male_death_percentage,
#     "Class 1 Passengers": num_class_1,
#     "Class 2 Passengers": num_class_2,
#     "Class 3 Passengers": num_class_3,
#     "Class 1 Percentage": class_1_percentage,
#     "Class 2 Percentage": class_2_percentage,
#     "Class 3 Percentage": class_3_percentage,
#     "Avg Fare Class 1": average_fare_class_1,
#     "Avg Fare Class 2": average_fare_class_2,
#     "Avg Fare Class 3": average_fare_class_3
# }
#
# print("Dictionary of calculated results:")
# print(statistics)

# question 2
class Ticket:
    def __init__(self, title, price, quantity, language="Geo"):
        self.title = title
        self.price = price
        self.quantity = quantity
        self.language = language

    def __str__(self):
        return f"Movie: {self.title}\nPrice: {self.price} GEL\nTickets Available: {self.quantity}\nLanguage: {self.language}"

class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"User: {self.name}\nBalance: {self.balance} GEL"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} GEL. New balance: {self.balance} GEL")
        else:
            print("Deposit amount must be positive!")

ticket1 = Ticket("Avatar", 15, 100)
print(ticket1)

user1 = User("John Doe", 50)
print(user1)

user1.deposit(30)
print(user1)
