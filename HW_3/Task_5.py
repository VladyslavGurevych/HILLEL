# You have a group of people with non-unique names.
# Generate a list of non-duplicate names (you cannot use set for this task.
# If there are 2 johns in the list, you need to take only one of them.
# "John Dow", "John Dow", "Marta Dow" => "John Dow", "Marta Dow ")

list = ["Alex Bobin", "Vera Dorn", "Olga Lashukova", "Igor Petrov", "Vanya Rodin", "Ira Vlasova", "Igor Petrov"]

non_duplicate = []

for item in list:
    if item in non_duplicate:
        continue
    else:
        non_duplicate.append(item)

print(non_duplicate)

