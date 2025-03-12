creer un venv
python -m venv ./

activer env

pour utiliser l'env virtuel et installer des package dessus
C:\dev\projects\python-sandbox\venv\Scripts\activate.bat

install dépendances
pip install django

creer un projet django
python -m django startproject pythonSandbox

manage.py // lance serv, fait mig ...

lance serv
python manage.py runserver

un projet a plusieurs app (ie module) qui a une feature (chaque app a une url)

creer une app
python manage.py startapp helloWorld

pour les mig, on lance une commande qui génére un fichier qu'on executera pour effectuer reelement la mig

une vue peut etre une fonction ou un classe

dans settings.py je rajoute au tableau INSTALLED_APPS le fichier de conf de ma nouvelle app pour pouvoir faire les migrations

creer la mig
python manage.py makemigrations helloWorld

verifier la requete qui sera exec
python manage.py sqlmigrate helloWorld 0001

applique la mig
python manage.py migrate


list = [1,2]
for val in list:
    ...

for i in range(0,10):
    ...

for index, val in enumerate(list):
    ...
    
dict = {"Pierre": 2500, "Marie": 5000, "Julien": 1200}
sum = 0
for item in dict.item(): #ou item.values() / keys()
    sum += item.value()
resultat = sum(employes.values())

print("abc")

ma_liste = [1, 2, 3]
ma_liste = ma_liste + [4, 5, 6] # concat listes
ma_liste.append(1)
ma_liste.remove(1) // supprime la premiere itération de la val dans le tab
ma_liste.pop(index) // supprime à l'index et return la val delete
ma_liste[-1] // dernier el
list[:indexFin]
list[::step] // si step = 2 par 2 --> listInversed = list[::-1]
liste = filter(lambda element : element%2==1 , liste)   // filtre
filter(test, dict) // fait appel a la meth test et lui passe en argt automatiquement l'élément du dict

list = map(lambda element : element % 2 == 0, list)     // fait une op sur chaque val
liste = list(liste) // cast en list
list3 = [x for x in list2 if x!= 1]                     // list comprehension / append x à la liste en parcourant avec un for sur la list2 et filtre avec un if
if bool(liste): OU if liste: // renvoie false si vide --> def dans une methode de classe __bool__

a=2
toto=f"Ma variable est égale à {a}" # fstring / {a=} afficherais le nom de la var avec sa val
print(toto) # fstring
print(f"Ma variable est égale à {a=}")

dict={}
dict["makey"]="maval"
dict.pop("makey") // 2nd argt pour catch l'erreur (return ce 2nd argt)
list = list(dict) // return la liste des clés

""" pour bloc de comm






------------------------------



python manage.py createsuperuser # backoffice pour accéder à la bdd


Model est une classe qui permet de récup des data en bdd avec 
.objects.filter(user=req.user)
.objects.all()
le res est un querySet, une liste <MaTable: monObjet>

Model serializer
- map un model en objet python
serial = TaskSerializer(tasksRetrieved, many=True)
tasksSerialized = serial.data
- map un dictionnaire (body http) en objet python
serializer = TaskSerializer(data=dictionnary, partial=True)
- valide un model
if serializer.is_valid():
    - save un model
    serializer.save(user=req.user)
- maj un model
taskRetrieved = TaskSerializer(taskRetrieved, data=body, partial=True)
