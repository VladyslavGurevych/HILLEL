# You have 2 companies with people. One of the companies, let it be Eleks, was taken over by Toshiba.

eleks_staff = ["Robin Bobin", "Varvara Dorn", "Olga Vasukova", "Igor Petrov"]
toshiba_staff = ["Ira Soroka", "Oleg Bubno", "Anna Vetrova", "Igor Petrov"]
new_toshiba_staff = eleks_staff + toshiba_staff

print(new_toshiba_staff)

# _________________FOR____________________
eleks_staff = ["Robin Bobin", "Varvara Dorn", "Olga Vasukova", "Igor Petrov"]
toshiba_staff = ["Ira Soroka", "Oleg Bubno", "Anna Vetrova", "Igor Petrov"]

for person in eleks_staff:
    toshiba_staff.append(person)

print(toshiba_staff)