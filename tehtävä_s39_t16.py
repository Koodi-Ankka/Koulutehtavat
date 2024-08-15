kokonaisluku1 = int(input("Kirjoita kokonaisluku "))
kokonaisluku2 = int(input("Kirjoita kokonaisluku "))
osamäärä = kokonaisluku1 / kokonaisluku2
jakojäännös = kokonaisluku1 % kokonaisluku2
if jakojäännös == 0: [
    print("Osamäärä on ", osamäärä)
]
else: [
    print("Osamäärä on ", osamäärä, "ja jakojäännös on ", jakojäännös)
]