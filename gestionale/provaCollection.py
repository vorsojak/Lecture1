import copy
from collections import Counter, deque

from gestionale.core.clienti import ClienteRecord
from gestionale.core.prodotti import ProdottoRecord
from gestionale.vendite.ordini import Ordine, RigaOrdine

p1 = ProdottoRecord("Laptop", 1200,1)
p2 = ProdottoRecord("Mouse",20,1)
p3 = ProdottoRecord("Auricolari", 250,1)

carrello = [p1, p2, p3, ProdottoRecord("Tablet", 700,1)]

print(f"prodotti nel carrello:")
for i, p in enumerate(carrello):
    print(f"{i}) {p.name} - {p.prezzo_unitario}")

carrello.append(ProdottoRecord("Monitor", 150.0,1))

carrello.sort(key = lambda x: x.prezzo_unitario, reverse=True)

print(f"prodotti nel carrello, ordinati per prezzo unitario:")
for i, p in enumerate(carrello):
    print(f"{i}) {p.name} - {p.prezzo_unitario}")

prezzo_totale = sum( i.prezzo_unitario for i in carrello)

carrello.append(ProdottoRecord("prod",100.0,1))
carrello.extend([ProdottoRecord("aaa",50,1), ProdottoRecord("bbb", 40,1)])
carrello.insert(2, ProdottoRecord("ccc", 30,1))

carrello.pop()
carrello.pop(2)
carrello.remove(p3)
#carrello.clear()

#carrello.sort()
#carrello.sort(reverse=True)
#carrello.sort(key= function)
#carrello_ordinato = sorted(carrello)

carrello.reverse()
carrello_copia = carrello.copy()
carrello_copia2 = copy.deepcopy(carrello)

#TUPLE
sede_principale = (45,8) #lat e long sede di torino
sede_milano = (45, 9) #lat e long sede di Milano

print(f"Sede principale ha lat. {sede_principale[0]} e long. {sede_principale[1]}")

aliquoteIVA = (
    ("Standard", 0.22),
    ("Ridotta", 0.10),
    ("Alimentari", 0.04),
    ("EsentiIVA", 0)
)

for descr, valore in aliquoteIVA:
    print(f"{descr}: {valore*100}%")

def calcola_statistiche_carrello(carrello):
    """Restituisce prezzo totale, prezzo medio, massimo e minimo"""
    prezzi = [p.prezzo_unitario for p in carrello]
    return sum(prezzi), sum(prezzi) / len(prezzi), max(prezzi), min(prezzi)

tupla = calcola_statistiche_carrello(carrello)
tot, media, massimo, minimo = calcola_statistiche_carrello(carrello) #unpacking,
tot2, *altricampi = calcola_statistiche_carrello(carrello)

#SET
categorie = {"Gold", "Silver", "Bronze", "Gold"}
print(categorie, len(categorie))
categorie2 = {"Platinum", "Elite", "Gold"}
#categoria_all = categorie.union(categorie2)
categorie_all = categorie | categorie2
categorie_comuni = categorie & categorie2
print(categorie_comuni)
categorie_esclusive = categorie - categorie2 #solo categorie presenti in categorie e non in categorie2
print(categorie_esclusive)
categorie_esclusive_simmetrica = categorie ^ categorie2 # solo categorie presenti in una collez ma non nell'altra
print(categorie_esclusive_simmetrica)

prodotti_ordine_A = {p1,p2,p3}
prodotti_ordine_B = {ProdottoRecord("aaa",50,1), ProdottoRecord("bbb", 40,1), ProdottoRecord("ccc",20,1)}
s = set()
s1 = set()
s.add(p1)
s.update([p2,p3]) #update() per aggiungere più elementi
s.remove(p3) #se non esiste scatena un keyError
s.discard(p3) # rimuove un elemento senza scatenare l'eccezione se non esiste
s.pop() #rimuove e restituisce un elemento
s.clear()

s.union(s1) #unisce i set
s.intersection(s1) #solo elem in comune
s.difference(s1) # elem di s non contenuti in s1
s.symmetric_difference(s1)

s1.issubset(s)
s1.issuperset(s)
s1.isdisjoint(s)

#DIZIONARIO
catalogo = {
    "LAP001": p1,
    "LAP002": ProdottoRecord("Laptop",1500,1),
    "MAU001": p2,
    "AUR001": p3
}

cod = "LAP001"
prod = catalogo[cod]
print(f"Il prodotto con codice {cod} è {prod}")
print(f"Cerco un altro oggetto: {catalogo.get("PrdotottoInesistente")}") #restituisce None

prod2 = catalogo.get("sdvsd", ProdottoRecord("Sconosciuto",0,1))
print(prod2)

keys = catalogo.keys()
valori = catalogo.values() #restituiscono un oggetto setlike

for k in keys:
    print(k)
for v in valori:
    print(v)
for k, v in catalogo.items():
    print(f"Codice: {k} - Prodotto: {v}")

rimosso = catalogo.pop("LAP002")
print(rimosso)

#dict comprehension
prezzi = {codice: prod.prezzo_unitario for codice,prod in catalogo.items()}

"""Esercizio
   Per ognuno dei seguenti casi decidere quale struttura usare.
1) Memorizzare un elenco di ordini che dovranno essere processati in ordine di arrivo
2) Memorizzare i CF dei clienti univoci
3) Creare un database di prodotti che posso cercare con un codice univoco
4) Memorizzare le coordinate GPS della nuova sede di roma
5) Tenere traccia delle categorie di clienti che hanno fatto un ordine in un certo range temporale
"""
ordini = [] #lista
elencoCF = set() #set
prodotti = {} #dizionario
coordinate_roma = () #tupla
categoriee = {"Gold", "Silver", "Bronze"} #set

ordini_da_processare = []
o1 = Ordine([], ClienteRecord("Mario Rossi", "mario@polito.it", "Gold"))
o2 = Ordine([], ClienteRecord("Mario Bianchi", "bianchi@polito.it", "Silver"))
o3 = Ordine([], ClienteRecord("Fulvio Rossi", "fulvio@polito.it", "Bronze"))
o4 = Ordine([], ClienteRecord("Carlo Masone", "carlo@polito.it", "Gold"))

ordini_da_processare.append((o1, 0))
ordini_da_processare.append((o2, 10))
ordini_da_processare.append((o3, 3))
ordini_da_processare.append((o4, 45))

codici_fiscali = {"ajnfkefioe231", "ajnsow241", "njknaskm1094", "ajnsow241"}
print(codici_fiscali)

listino_prodotti = {"LAP0001" : ProdottoRecord("Laptop", 1200.0,1),
                    "KEY001" : ProdottoRecord("Keyboard", 20.0,1)}

magazzino_roma = (45, 6)

categorie_periodo = set()
categorie_periodo.add("Gold")
categorie_periodo.add("Bronze")

print("=============================Counter=============================")
#COUNTER
lista_clienti = [
    ClienteRecord("Mario Rossi", "mario@polito.it", "Gold"),
    ClienteRecord("Mario Bianchi", "bianchi@polito.it", "Silver"),
    ClienteRecord("Fulvio Rossi", "fulvio@polito.it", "Bronze"),
    ClienteRecord("Carlo Masone", "carlo@polito.it", "Gold"),
    ClienteRecord("Mario Bianchi", "mario@polito.it", "Gold"),
    ClienteRecord("Giuseppe Averta", "bianchi@polito.it", "Silver"),
    ClienteRecord("Francesca Pistilli", "fulvio@polito.it", "Bronze"),
    ClienteRecord("Carlo Masone", "carlo@polito.it", "Gold"),
    ClienteRecord("Fulvio Corno", "carlo@polito.it", "Silver")
]

categorie = [c.categoria for c in lista_clienti]
categorie_counter = Counter(categorie)

print("Distribuzione categorie clienti")
print(categorie_counter)

print("2 Categorie più frequent1")
print(categorie_counter.most_common(2))

print("totale:")
print(categorie_counter.total())

vendite_gennaio = Counter(
    {"Laptop": 13, "Tablet": 15}
)

vendite_febbraio = Counter(
    {"Laptop": 3, "Stampante": 1}
)

vendite_bimestre = vendite_gennaio+vendite_febbraio

#Aggregare informazione
print(f"Vendite Gennaio: {vendite_gennaio}")
print(f"Vendite Febbraio: {vendite_febbraio}")
print(f"Vendite bimestre: {vendite_bimestre}")

# Fare la differenza
print(f"Differenza di vendite: {vendite_gennaio-vendite_febbraio}")


#modificare i valore in the fly

vendite_gennaio["Laptop"] += 4
print(f"Vendite Gennaio: {vendite_gennaio}")

# metodi da ricordare
# c.most_common(n) #restituisce gli n elementi più frequenti
# c.total() # somma dei conteggi

#Defaultdicts


#deque
coda_ordini = deque()
for i in range(1,10):
    cliente = ClienteRecord(f"Cliente {i}: ", f"cliente{i}@polito.it","Gold")
    prodotto = ProdottoRecord(f"Prodotto{i}",100,1)
    ordine = Ordine([RigaOrdine(prodotto,1),cliente],cliente)
    coda_ordini.append(ordine)

print(f"Ordini in coda: {len(coda_ordini)}")


while coda_ordini:
    ordine_corrente = coda_ordini.popleft()
    print("Sto gestendo l'ordine: ", ordine_corrente)



