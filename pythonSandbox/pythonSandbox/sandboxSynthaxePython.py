"""
la liste des personnes dont le salaire est 3000 euros ou plus.
la liste des personnes dont la prime est de 250 euros ou plus.
la liste des personnes dont la prime fait au moins 6% du salaire.
Vous devez écrire une fonction statistiques_salaires qui prends dans l'ordre les paramètres 
personnes, salaires, primes et qui renvoie dans l'ordre les 3 listes de personnes.
"""

personnes = ["Stallman", "Torvalds", "Perlis", "Turing", "VomNeumann",
             "Iverson", "Boole", "Hamming", "Knuth", "Ritchie", "Thompson"]
salaires = [1500, 4700, 1500, 3800, 890, 4200, 480, 395, 1710, 1300, 3900]
primes = [190, 0, 117, 100, 500, 60, 0, 150, 0, 100, 180]

SALARYMAX = 3000

class Person:
    def __init__(self, nom, salaire, prime):
        self.nom = nom
        self.salaire = salaire
        self.prime = prime

    def __str__(self):
        return f"{self.nom}, {self.salaire}, {self.prime}"
    
    def isSalarySup3000(self):
        return self.salaire > SALARYMAX
    
    def __bool__(self):
        return self.isSalarySup3000()

def statistiques_salaires(personnes, salaires, primes):
    p1 = Person(personnes[0], salaires[0], primes[0])
    print(bool(p1))

    listPerson = [Person(personnes[i], salaires[i], primes[i]) for i in range(len(personnes))]
    listPersonSupSalMax = filter(lambda e: e.isSalarySup3000(), listPerson)
    listPersonSupSalMax = list(listPersonSupSalMax)
    return listPersonSupSalMax

"""
    dictionnary = {}
    listeSalaireSup3000 = []
    listePrimeSup250 = []
    for i in range(len(personnes)):
        dictionnary[personnes[i]]= [salaires[i], primes[i]]
    listeSalaireSup3000 = filter(lambda e: e[1][0] >= 3000, dictionnary.items())
    listeSalaireSup3000 = dict(listeSalaireSup3000)
    listeSalaireSup3000 = list(listeSalaireSup3000)

    listePrimeSup250 = filter(lambda e: e[1][1] >= 250, dictionnary.items())
    listePrimeSup250 = dict(listePrimeSup250)
    listePrimeSup250 = list(listePrimeSup250)
    return listeSalaireSup3000, listePrimeSup250, []
"""

print(statistiques_salaires(personnes, salaires, primes)[0])

#date
#type()
#exceptions