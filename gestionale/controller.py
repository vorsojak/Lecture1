import flet as ft

from gestionale.GestoreOrdini import GestoreOrdine

class Controller:
    def __init__(self, v):
        self._view = v
        self._model = GestoreOrdine()

    def addOrdine(self, e):
        nomeP = self._view.NomeProdotto.value
        if nomeP == "":
            return
        try:
            prezzoP = float(self._view.Prezzo.value)
        except ValueError:
            self._view.lvOut.controls.append(
                ft.Text("Attenzione, il prezzo deve essere un numero", color="red")
            )
            self._view.update_page()
            return
        try:
            quantitaP = int(self._view.Quantita.value)
        except ValueError:
            self._view.lvOut.controls.append(
                ft.Text("Attenzione, la quantità deve essere un numero intero", color="red")
            )
            self._view.update_page()
            return

        nomeC = self._view.NomeCliente.value
        if nomeC == "":
            self._view.lvOut.controls.append(
                ft.Text("Attenzione! Il campo nome Cliente non può essere vuoto")
            )
            self._view.update_page()
            return
        mailC = self._view.Mail.value
        if mailC == "":
            self._view.lvOut.controls.append(
                ft.Text("Attenzione! Il campo mail Cliente non può essere vuoto")
            )
            self._view.update_page()
            return
        categoriaC = self._view.Categoria.value
        if categoriaC == "":
            return

        ordine = self._model.crea_ordine(nomeP, prezzoP, quantitaP, nomeC, mailC, categoriaC)
        self._model.add_ordine(ordine)

        self._view.NomeProdotto.value = ""
        self._view.Prezzo.value = ""
        self._view.Quantita.value = ""
        self._view.NomeCliente.value = ""
        self._view.Mail.value = ""
        self._view.Categoria.value = ""

        self._view.lvOut.controls.append(
            ft.Text("Ordine correttamente aggiunto", color = "green"))
        self._view.lvOut.controls.append(
            ft.Text("Dettagli dell'ordine"))
        self._view.lvOut.controls.append(
            ft.Text(ordine.riepilogo()))
        self._view.update_page()

    def gestisciOrdine(self):
        self._view.lvOut.controls.clear()
        res, ordine = self._model.processa_prossimo_ordine()

        if res:
            self._view.lvOut.controls.append(
                ft.Text("Ordine processato con successo!", color= "green")
            )
            self._view.lvOut.controls.append(
                ft.Text(ordine.riepilogo())
            )
            self._view.update_page()
            return
        else:
            self._view.lvOut.controls.append(
                ft.Text("Non ci sono ordini in coda!", color="blue")
            )
            self._view.update_page()
            return

    def gestisciAllOrdini(self):
        self._view.lvOut.controls.clear()
        lista_ordini = self._model.processa_tutti_gli_ordini()
        if not lista_ordini:
            self._view.lvOut.controls.append(
                ft.Text("Non ci sono ordini in coda!", color="blue")
            )
            self._view.update_page()
            return
        else:
            self._view.lvOut.controls.append(
                ft.Text(f"Ho processato correttamente {len(lista_ordini)} ordini!", color="green")
            )
            for o in lista_ordini:
                self._view.lvOut.controls.append(
                    ft.Text(f"{o.riepilogo()}\n")
                )
            self._view.update_page()
            return


    def stampaSommario(self):
        self._view.lvOut.controls.clear()
        self._view.lvOut.controls.append(
            ft.Text(f"Di seguito il sommario dello stato del business\n", color="orange")
        )
        self._view.lvOut.controls.append(
            ft.Text(self._model.stampa_sommario())
        )
        self._view.update_page()
        return

