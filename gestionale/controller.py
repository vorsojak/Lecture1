import flet as ft

from gestionale.GestoreOrdini import GestoreOrdine
from gestionale.core.prodotti import Prodotto, ProdottoRecord


class Controller:
    def __init__(self, v):
        self._view = v
        self._model = GestoreOrdine()

    def addOrdine(self, e):
        nomeP = self._view._NomeProdotto.value
        if nomeP == "":
            return
        try:
            prezzoP = float(self._view._Prezzo.value)
        except ValueError:
            self._view._lvOut.controls.append(
                ft.Text("Attenzione, il prezzo deve essere un numero", color="red")
            )
            self._view.update_page()
            return
        try:
            quantitaP = int(self._view._Quantita.value)
        except ValueError:
            self._view._lvOut.controls.append(
                ft.Text("Attenzione, la quantità deve essere un numero intero", color="red")
            )
            self._view.update_page()
            return

        #prodotto = ProdottoRecord()

        nomeC = self._view._NomeCliente.value
        mailC = self._view._Mail.value
        categoriaC = self._view._Categoria.value

        ordine = self._model.crea_ordine(nomeP, prezzoP, quantitaP, nomeC, mailC, categoriaC)
        self._model.add_ordine(ordine)

        self._view._NomeProdotto.value = ""
        self._view._Prezzo.value = ""
        self._view._Quantita.value = ""
        self._view._NomeCliente.value = ""
        self._view._Mail.value = ""
        self._view._Categoria.value = ""

        self._view._lvOut.controls.append(
            ft.Text("Ordine correttamente aggiunto", color = "green"))
        self._view._lvOut.controls.append(
            ft.Text("Dettagli dell'ordine"))
        self._view._lvOut.controls.append(
            ft.Text(ordine.riepilogo()))
        self._view.update_page()

    def gestisciOrdine(self):
        pass

    def gestisciAllOrdini(self):
        pass

    def stampaSommario(self):
        pass
