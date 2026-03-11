from dataclasses import dataclass


class Prodotto:
    aliquota_iva = 0.22 #variabile di classe -- ovvero è la stessa per tutte le istanze che verranno create.

    def __init__(self, name: str, price: float, quantity: int, supplier = None):
        self.prezzo_unitario = None
        self.name = name
        self._price = None
        self.price = price
        self.quantity = quantity
        self.supplier = supplier

    def valore_netto(self):
        return self._price*self.quantity

    def valore_lordo(self):
        netto = self.valore_netto()
        lordo = netto*(1+self.aliquota_iva)
        return lordo

    @classmethod
    def costruttore_con_quantita_uno(cls, name: str, price: float, supplier: str):
        cls(name, price, 1, supplier)

    @staticmethod
    def applica_sconto(prezzo, percentuale):
        return prezzo*(1-percentuale)

    @property
    def price(self): # eq. getter
        return self._price
    @price.setter
    def price(self, valore): #eq. setter
        if valore < 0:
            raise ValueError("Attenzione, il prezzo non può essere negativo.")
        self._price = valore

    def __str__(self):
        return f"{self.name} - disponibilità: {self.quantity} pezzi a {self.price} $"

    def __repr__(self):
        return f"Prodotto(nome = {self.name}, price = {self.price}, quantity = {self.quantity}, supplier = {self.supplier})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other,Prodotto):
            return NotImplemented

        return (self.name == other.name and
                self.price == other.price and
                self.quantity == other.quantity
                and self.supplier == other.supplier)

    def prezzo_finale(self) -> float:
        return self.price * (1+self.aliquota_iva)




    def __lt__(self, other: "Prodotto") -> bool:
        return self.price < other.price

class ProdottoScontato(Prodotto):
    def __init__(self, name: str, price: float, quantity: int, supplier: str, sconto_percento: int):
        #Prodotto.__init__(self)
        super().__init__(name, price, quantity, supplier)
        self.sconto_percento = sconto_percento

    def prezzo_finale(self) -> float:
        return self.valore_lordo()*(1-self.sconto_percento/100)

class Servizio(Prodotto):
    def __init__(self, name: str, tariffa: float, ore: int):
        super().__init__(name = name, price = tariffa, quantity = 1, supplier=None)
        self.ore = ore

    def prezzo_finale(self) -> float:
        return self.price*self.ore

#Definire una classe abbonamento che abbia come attributi nome, prezzo mensile, mesi. Deve aver un metodo per calcolare
#il prezzo finale, ottenuto come prezzo_mensile*mesi
class Abbonamento:
    prezzofinale = None
    def __init__(self, name: str, prezzo_mensile: float, mesi: int):
        self.name = name
        self.prezzo_mensile = prezzo_mensile
        self.mesi = mesi
        self.prezzofinale = prezzo_mensile*mesi

    def prezzo_finale(self) -> float:
        return self.prezzofinale

@dataclass
class ProdottoRecord:
    name: str
    prezzo_unitario: float
    quantity: int

    def __hash__(self):
        return hash((self.name, self.prezzo_unitario))

    def __str__(self):
        return f"{self.name} - {self.prezzo_unitario}"

MAX_QUANTITA = 1000

def crea_prodotto_standard(nome: str, prezzo: float):
    return Prodotto(nome,prezzo,1,None)

def test_modulo():
    myproduct1 = Prodotto(name = "Laptop", price = 1200.0, quantity=12, supplier="ABC")

    print(f"Nome prodotto: {myproduct1.name} - prezzo: {myproduct1.price}")

    print(f"Il totale lordo di myproduct1 è {myproduct1.valore_lordo()}") #uso un metodo di istanza
    p3 = Prodotto.costruttore_con_quantita_uno("Auricolari", 200.0, "ABC") #Modo per chiamare un metodo di classe.
    print(f"Prezzo scontato di myproduct1 {Prodotto.applica_sconto(myproduct1.price, 0.15)}")#Modo per chiamare un metodo statico.

    myproduct2 = Prodotto("Mouse", 10, 25, "CDE")
    print(f"Nome prodotto: {myproduct2.name} - prezzo: {myproduct2.price}")

    print(f"Valore lordo di myproduct1: {myproduct1.valore_lordo()}")
    Prodotto.aliquota_iva = 0.24
    print(f"Valore lordo di myproduct1: {myproduct1.valore_lordo()}")


    print(f"****{myproduct1}")

    p_a = Prodotto(name = "Laptop", price = 1200.0, quantity=12, supplier="ABC")
    p_b = Prodotto("Mouse", 10,14,"CDE")

    print(f"myproduct1 = p_a ?", myproduct1 == p_a)  #va a chiamare il metodo __eq__, mi aspetto TRUE
    print("p_a = p_b", p_a == p_b) #mi aspetto FALSE

    mylist = [p_a, p_b, myproduct1]
    mylist.sort(reverse=True)
    print("lista di prodotti ordinata:")
    for p in mylist:
        print(f" - {p}")



    my_product_scontato = ProdottoScontato("Auricolari", 320, 1, "ABC", 10)
    my_service = Servizio("Consulenza", 100, 3)

    mylist.append(my_product_scontato)
    mylist.append(my_service)

    mylist.sort()

    for elem in mylist:
        print(f"{elem.name} -> {elem.prezzo_finale()}")

    print("---------------------------------------------------------------")

    from typing import Protocol


    class HaPrezzoFinale(Protocol):
        def prezzo_finale(self) -> float:
            ...


    def calcola_totale(elementi: list[HaPrezzoFinale]) -> float:
        return sum(e.prezzo_finale() for e in elementi)


    print(f"Il prezzo totale degli elementi che "
          f"hanno sicuramente il metodo 'prezzo_finale' è: {calcola_totale(mylist)}")

    abb = Abbonamento("Software gestionale", 30, 24)
    mylist.append(abb)

    for elem in mylist:
        print(f"{elem.name} -> {elem.prezzo_finale()}")


    def calcola_totale(elementi):
        tot = 0
        for i in elementi:
            tot += i.prezzo_finale()
        return tot


    print(f"Il prezzo totale è: {calcola_totale(mylist)}")

    from typing import Protocol


    class HaPrezzoFinale(Protocol):
        def prezzo_finale(self) -> float:
            ...


    def calcola_totale(elementi: list[HaPrezzoFinale]) -> float:
        return sum(e.prezzo_finale() for e in elementi)


    print(f"Il prezzo totale degli elementi che "
          f"hanno sicuramente il metodo 'prezzo_finale' è: {calcola_totale(mylist)}")

if __name__ == "__main__":
    test_modulo()