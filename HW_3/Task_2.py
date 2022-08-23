# You have 3 groups of people casino_blacklist, poker_blacklist, alcohol_blacklist.
# Names of people in the format "John Dow" first and second name. Find those who are on all blacklists.

casino_blacklist = ["Robin Bobin", "Varvara Dorn", "Olga Vasukova", "Igor Petrov"]
poker_blacklist = ["Alex Bobin", "Vera Dorn", "Olga Lashukova", "Igor Petrov"]
alcohol_blacklist = ["Vanya Rodin", "Klara Bebach", "Ira Vlasova", "Igor Petrov"]

casino_poker = set(casino_blacklist + poker_blacklist)
alcohol_blacklist = set(alcohol_blacklist)
winner = casino_poker.intersection(alcohol_blacklist)

print("The winner is " + str(winner))