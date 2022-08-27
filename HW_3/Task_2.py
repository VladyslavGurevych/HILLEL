# You have 3 groups of people casino_blacklist, poker_blacklist, alcohol_blacklist.
# Names of people in the format "John Dow" first and second name. Find those who are on all blacklists.

casino_blacklist = ["Robin Bobin", "Varvara Dorn", "Olga Vasukova", "Igor Petrov"]
poker_blacklist = ["Alex Bobin", "Vera Dorn", "Olga Lashukova", "Igor Petrov"]
alcohol_blacklist = ["Vanya Rodin", "Klara Bebach", "Ira Vlasova", "Igor Petrov"]

casino_blacklist = set(casino_blacklist)
poker_blacklist = set(poker_blacklist)
alcohol_blacklist = set(alcohol_blacklist)

winner_1 = casino_blacklist.intersection(poker_blacklist)
winner_2 = casino_blacklist.intersection(alcohol_blacklist)
winner_3 = poker_blacklist.intersection(alcohol_blacklist)


print(winner_1, winner_2, winner_3)