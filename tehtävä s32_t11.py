luku1 = int(input("Kerro kokonaisluku ")) #pyytää kaksi kokonaislukua ja tarkistaa ovatko ne yhtäsuuria
luku2 = int(input("Kerro kokonaisluku "))
erisuuria = (luku1 != luku2)
if erisuuria == True: [ #jos numerot eivät ole yhtäsuuria
    print("Numerot eivät ole yhtäsuuria")
]
else: [
    print("Numerot ovat yhtäsuuria")
]
