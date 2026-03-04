from dataclasses import dataclass
from pprint import pprint
from datetime import date
from gestionale.core.clienti import Cliente
from gestionale.core.prodotti import Prodotto, ProdottoRecord
from gestionale.vendite.ordini import Ordine, RigaOrdine


@dataclass
class Fattura:
    ordine: Ordine
    numero_fattura: int
    data: date

    def genera_fattura(self) -> list:
        linee = [
            f"-" * 60,
            f"Fattura  numero: {self.numero_fattura} del {self.data}", #dettagli ordine
            f"-" * 60,

            f"Cliente: {self.ordine.cliente.nome} - Categoria: {self.ordine.cliente.categoria} - Mail: {self.ordine.cliente.mail}"   #dettagli cliente

        ]
        for i, riga in enumerate(self.ordine.righe):
            linee.append(f"Prodotto {i+1}: {riga.prodotto.name}")
            linee.append(f"Prezzo totale: {riga.prodotto.quantity} * {riga.prodotto.prezzo_unitario} = {riga.prodotto.quantity*riga.prodotto.prezzo_unitario}")
        linee.extend([
            f"-" * 60,
            f"Totale netto: {self.ordine.totale_netto()}",
            f"IVA22%: {self.ordine.totale_netto()*0.22}",
            f"Totale lordo: {self.ordine.totale_lordo(0.22)}",
            f"-" * 60
        ])

        return linee

if __name__=="__main__":
    cliente1 = Cliente("Mario Rossi", "mario.rossi@gmail.com", "Gold")
    p1 = ProdottoRecord("Laptop", 1200.0, 2)
    p2 = ProdottoRecord("Mouse", 10, 10)
    ordine1 = Ordine([RigaOrdine(p1,2), RigaOrdine(p2,10)], cliente1)
    fattura1 = Fattura(ordine1, 12345, date(2026,3,4))
    lista = fattura1.genera_fattura()
    for riga in lista:
        print(riga)