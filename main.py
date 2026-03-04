# Scriviamo un codice python che modelli un semplice
# gestionale aziendale. Dovremo prevedere la possibilità di
# definire entità che modellano i prodotti, i clienti,
# offrire interfacce per calcolare i prezzi, eventualmente
# scontati, ...
from gestionale.vendite.ordini import Ordine, RigaOrdine, OrdineConSconto
from gestionale.core.prodotti import Prodotto, crea_prodotto_standard, ProdottoRecord
from gestionale.core.clienti import Cliente, ClienteRecord
import networkx as fix
import flet

print("========================")
p1 = Prodotto("Ebook reader", 120, 1, "AAA")
p2 = crea_prodotto_standard("Tablet",750)
print(p1)
print(p2)

"""
#modi per importare
#1)
from prodotti import ProdottoScontato
p3 = ProdottoScontato("Auricolari", 230,1,"ABC",10)

#2)
from prodotti import ProdottoScontato as ps
p4 = ps("Auricolari", 230,1,"ABC",10)

#3)
import prodotti
p5 = prodotti.ProdottoScontato("Auricolari", 230,1,"ABC",10)

#4)
import prodotti as p
p6 = p.ProdottoScontato("Auricolari", 230,1,"ABC",10)
print("========================")
"""

c1 = Cliente("Mario Bianchi", "mario.bianchi@polito.it", "Gold")

cliente1 = ClienteRecord("Mario Rossi", "mario.rossi@gmail.com", "Gold")
p1 = ProdottoRecord("Laptop", 1200)
p2 = ProdottoRecord("Mouse", 20)

ordine = Ordine([RigaOrdine(p1,2), RigaOrdine(p2,10)],cliente1)
ordine_scontato = OrdineConSconto([RigaOrdine(p1,2), RigaOrdine(p2,10)],cliente1, 0.1)

print(ordine)
print(f"Numero di righe nell'ordine: ", ordine.numero_ordini())
print(f"Totale netto: {ordine.totale_netto()}")
print(f"Totale lordo (IVA 22%): {ordine.totale_lordo(0.22)}")
print("\n")

print(ordine_scontato)
print(f"Numero di righe nell'ordine: ", ordine_scontato.numero_ordini())
print(f"Totale netto: {ordine_scontato.totale_netto()}")
print(f"Totale lordo (IVA 22%): {ordine_scontato.totale_lordo(0.22)}")
print("\n")



print("====================================================\n")
