#file gestionale con le seguenti funzionalità:
#supportare l'arrivo e la gestione di ordini
#quando arriva un nuovo ordine lo aggiungo alla coda, assicurandomi che sia eseguito solo dopo gli altri
#fornire statistiche sulla distribuzione di ordine per categoria di clienti
import random
from collections import deque, Counter, defaultdict

from dao.dao import DAO
from gestionale.core.cliente import ClienteRecord
from gestionale.core.prodotto import ProdottoRecord
from gestionale.vendite.ordini import Ordine, RigaOrdine


class GestoreOrdine:

    def __init__(self):
        self._ordini_da_processare = deque()
        self._ordini_processati = []
        self._statistiche_prodotti = Counter()
        self._ordini_per_categoria = defaultdict(list)
        self._dao = DAO()
        self._allP = []
        self._allC = []
        self._fill_data()

    def crea_ordine(self, nomeP: str, prezzo: float, quantita: int,
                    nomeC: str, mail: str, categoria: str):

        prod = ProdottoRecord(nomeP, prezzo, quantita)
        cliente = ClienteRecord(nomeC, mail, categoria)
        self.update_DB(prod, cliente)
        return Ordine([RigaOrdine(prod, quantita)],
                      cliente)


    def update_DB(self, prod, cliente):
        if not self._dao.hasProdotto(prod):
            self._dao.add_prodotto(prod)

        if not self._dao.hasCliente(cliente):
            self._dao.add_cliente(cliente)

    def _fill_data(self):
        """Leggo prodotti e clienti dal db e creo ordini randomici per testare l'app"""
        self._allP.extend(self._dao.getAllProdotti())
        self._allC.extend(self._dao.getAllClienti())
        for i in range(10):
            indexP = random.randint(0, len(self._allP)-1)
            indexC = random.randint(0, len(self._allC)-1)
            ordine = Ordine([RigaOrdine(self._allP[indexP], random.randint(1,5))
                ], self._allC[indexC])
            self.add_ordine(ordine)

    def add_prodotto(self, nome, prezzo, quantita):
        prodotto = ProdottoRecord(nome,prezzo,quantita)
        print(prodotto)
        self._dao.add_prodotto(prodotto)

    def add_cliente(self, nome, mail, categoria):
        cliente = ClienteRecord(nome, mail, categoria)
        self._dao.add_cliente(cliente)

    def add_ordine(self, ordine: Ordine):
        """Aggiunge un nuovo ordine a quelli da gestire"""
        self._ordini_da_processare.append(ordine)
        print(f"Ricevuto un nuovo ordine da parte di {ordine.cliente}")
        print(f"ordini ancora da evadere: {len(self._ordini_da_processare)}")

    def processa_prossimo_ordine(self):
        """Legge il prossimo ordine in coda e lo gestisce"""

        #controlliamo che l'ordine esista
        if not self._ordini_da_processare:
            print("Non ci son ordini da processare")
            return False, Ordine([], ClienteRecord("","",""))

        ordine =self._ordini_da_processare.popleft()
        print(f"Sto processando l'ordine da parte di {ordine.cliente}")
        print(ordine.riepilogo())

        #aggiornare statistiche sui prodotti venduti
        for riga in ordine.righe:
            self._statistiche_prodotti[riga.prodotto.name] += riga.quantita

        #raggruppare gli ordini per categoria
        self._ordini_per_categoria[ordine.cliente.categoria].append(ordine)

        #ordine processato
        self._ordini_processati.append(ordine)

        print(f"Ordine correttamente processato.")
        return True, ordine

    def processa_tutti_gli_ordini(self):
        """Processa tutti gli ordini attualmente in coda"""
        print(f"Sto processando tutti gli {len(self._ordini_da_processare)} ordini...")
        lista_ordini = []
        while self._ordini_da_processare:
            _,ordine = self.processa_prossimo_ordine()
            lista_ordini.append(ordine)
        print("Tutti gli ordini sono stati processati.")
        return lista_ordini

    def get_statistiche_prodotti(self, top_n: int = 5):
        """Restituisce info sui prodotti più venduti"""
        valori = []
        for prodotto, quantita in self._statistiche_prodotti.most_common(top_n):
            valori.append([prodotto, quantita])
        return valori

    def get_distribuzione_categorie(self):
        """Restituisce info su totale fatturato per ogni categoria presente"""
        valori = []
        for cat in self._ordini_per_categoria.keys():
            ordini = self._ordini_per_categoria[cat]
            totale_fatturato = sum( [o.totale_lordo(0.22) for o in ordini])
            valori.append((cat, totale_fatturato))
        return valori

    def stampa_riepilogo(self):
        """Stampa info di massimo"""
        print("==============================")
        print("stato_attuale_del_business")
        print(f"ordini correttamente gestiti: {len(self._ordini_processati)}")
        print(f"ordini in coda: {self._ordini_da_processare}")

        print("Prodotti più venduti:")
        for prod, quantita in self.get_statistiche_prodotti():
            print(f"{prod}: {quantita}")

        print("Fatturato per categoria")
        for valori in self.get_statistiche_prodotti():
            print(f"{valori[0]}: {valori[1]}")

    def stampa_sommario(self):
        """Restituisce una stringa con le info di massimo"""
        sommario = ""
        sommario+= "=============================="
        print("\nstato_attuale_del_business")
        sommario+= f"\nordini correttamente gestiti: {len(self._ordini_processati)}"
        sommario+= f"\nordini in coda: {len(self._ordini_da_processare)}"

        sommario+= "\nProdotti più venduti:"
        for prod, quantita in self.get_statistiche_prodotti():
            sommario+= f"\n-{prod}: {quantita}"

        sommario+= "\nFatturato per categoria"
        for cat, fatturato in self.get_distribuzione_categorie():
            sommario+= f"\n-{cat}: {fatturato}"
        sommario += "\n=============================="
        return sommario

def test_modulo():
    sistema = GestoreOrdine()
    p1 = ProdottoRecord("Laptop", 1200, 1)
    p2 = ProdottoRecord("Mouse", 20, 1)
    p3 = ProdottoRecord("Auricolari", 250, 1)

    ordini = [
        Ordine([RigaOrdine(p1, 1),
        RigaOrdine(p2, 2),
        RigaOrdine(p3, 5)],ClienteRecord("Mario Rossi", "mario@polito.it", "Gold")),

        Ordine([RigaOrdine(p1, 1),
        RigaOrdine(p2, 2),
        RigaOrdine(p3, 5)], ClienteRecord("Mario Bianchi", "bianchi@polito.it", "Silver")),

        Ordine([RigaOrdine(p1, 1),
        RigaOrdine(p2, 2),
        RigaOrdine(p3, 5)], ClienteRecord("Fulvio Rossi", "fulvio@polito.it", "Bronze")),

        Ordine([RigaOrdine(p1, 1),
        RigaOrdine(p2, 2),
        RigaOrdine(p3, 5)], ClienteRecord("Carlo Masone", "carlo@polito.it", "Gold")),

        Ordine([RigaOrdine(p1, 1),
        RigaOrdine(p2, 2),
        RigaOrdine(p3, 5)], ClienteRecord("Mario Bianchi", "mario@polito.it", "Gold"))
    ]
    for o in ordini:
        sistema.add_ordine(o)

    sistema.processa_tutti_gli_ordini()
    sistema.stampa_riepilogo()

if __name__=="__main__":
    test_modulo()
