leveys = int(input("Anna leveys "))
pituus = int(input("Anna pituus "))
piiri = leveys * 2 + pituus * 2
pintaala = leveys * pituus
piiriVaiPintaala = int(input("1 = piiri 2 = pinta-ala ")) # jos piiriVaiPintaala = 1 lasketaan piiri, jos piiriVaiPintaala = 2, lasketaan pinta-ala
if piiriVaiPintaala == 1: [
    
    print("Piiri on", piiri)
]
else: [  
    print("Pinta-ala on", pintaala)
    ]