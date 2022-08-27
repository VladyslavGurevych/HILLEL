# You have two groups of people. One group consists of omnivores, the other only vegetarians.
# An omnivore is a vegetarian but a vegetarian is not an omnivore.
# Display a list of guests who can eat vegetables and herbs.

omnivore = ["Robin Bobin", "Varvara Dorn", "Olga Vasukova", "Igor Petrov"]
vegetarians = ["Vanya Rodin", "Klara Bebach", "Ira Vlasova", "Vlad Dzan"]

who_can_eat_vegetables_herbs = omnivore + vegetarians

print('List of guests who can eat vegetables and herbs:')

for people in who_can_eat_vegetables_herbs:
    print(people)