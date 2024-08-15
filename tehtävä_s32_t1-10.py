# class color:
# t2 PURPLE = '\033[95m'
# t3 CYAN = '\033[96m'
# t4 BLUE = '\033[94m'
# t5 GREEN = '\033[92m'
# t6 YELLOW = '\033[93m'
# t7 RED = '\033[91m'
# BOLD = '\033[1m'
# UNDERLINE = '\033[4m'
# END = '\033[0m'

# print(color.BOLD + 'Hello, World!' + color.END)

# tehtävä 1
print("")
print("Lauri")

# tehtävä 2
print("")
print('\033[95m'"It doesnt matter how beautiful your theory is,")
print("it doesn't matter how smart you are.")
print("If it doesn't agree with the experiment, it's wrong."'\033[0m')

# tehtävä 3
print("")
print('\033[96m'"")
print(12 - 2 * 9)
print(126 / (30 - 24))
print('\033[0m')

# tehtävä 4
print('\033[94m'"")
x = 9
y = 14
z = 20

print(x + y - z)
print(x * y / z)
print('\033[0m')

# tehtävä 5
print('\033[92m')
print("pää tiellä (erikseen)")
print("päätiellä (yhteen)")
print('\033[0m')

# tehtävä 6
nimi = input("Mika on sun nimi? ")
osoite = input("Mika on sun osote? ")
print('\033[93m')
print("nimesi on")
print(nimi)
print("ja osoitteesi on")
print(osoite)
print('\033[0m')

# tehtävä 7
print()
kokonaisluku1 = int(input("Kerro kokonaisluku "))
kokonaisluku2 = int(input("Kerro toinen kokonaisluku "))
print("")
print("Vastauksesi on:")
print(kokonaisluku1 + kokonaisluku2)
print('\033[0m')

# tehtävä 8
desimaali1 = float(input("Kerro desimaali "))
desimaali2 = float(input("Kerro toinen desimaali "))
osamäärä = round(desimaali1 / desimaali2)
print(osamäärä)

# tehtävä 9
summa = desimaali1 + desimaali2
erotus = desimaali1 - desimaali2
print(summa)
print(erotus)

# tehtävä 10
kokonaisluku3 = int(input("Kerro kokonaisluku ")) #10
kokonaisluku4 = kokonaisluku3 - 5 #5
vastaus = kokonaisluku4 * 2
print(vastaus)