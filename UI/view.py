
import flet as ft

class View:

    def __init__(self, page):
        self._page = page
        self._controller = None
        self._page.title = "TdP_2026 - Software Gestionale"
        self._page.horizontal_aligment = ft.CrossAxisAlignment.CENTER
        self._page.theme_mode = ft.ThemeMode.LIGHT
        self.update_page()


    def carica_interfaccia(self):
        titolo = ft.Text("Software Gestionale", color="red")
        row_title = ft.Row(controls=[titolo],  alignment=ft.MainAxisAlignment.CENTER)

        # Prodotto
        self._NomeProdotto = ft.TextField(label="Nome del prodotto", width=200)
        self._Prezzo = ft.TextField(label="Prezzo del prodotto", width=200)
        self._Quantita = ft.TextField(label="Quantita del prodotto", width=200)
        self._btnAddProdotto = ft.ElevatedButton(content="Aggiungi prodotto al db", on_click=self._controller.aggiungiProdotto, width=250)


        row1 = ft.Row(controls = [self._NomeProdotto, self._Prezzo, self._Quantita, self._btnAddProdotto],
                      alignment=ft.MainAxisAlignment.CENTER)

        # Cliente
        self._NomeCliente = ft.TextField(label="Nome del cliente", width=200)
        self._Mail = ft.TextField(label="Mail del cliente", width=200)
        self._Categoria = ft.TextField(label="Categoria del cliente", width=200)
        self._btnAddCliente = ft.ElevatedButton(content="Aggiungi cliente al db", on_click=self._controller.aggiungiCliente, width=250)

        row2 = ft.Row(controls=[self._NomeCliente, self._Mail, self._Categoria, self._btnAddCliente],
                      alignment=ft.MainAxisAlignment.CENTER)

        # Buttons
        self._btnAdd = ft.ElevatedButton(content="Aggiungi ordine", on_click=self._controller.addOrdine, width=200)
        self._btnGestisciOrdine = ft.ElevatedButton(content="Gestisci prossimo ordine", on_click=self._controller.gestisciOrdine, width=250)
        self._btnGestisciAllOrdini = ft.ElevatedButton(content="Gestisci tutti gli ordini", on_click=self._controller.gestisciAllOrdini, width=200)
        self._btnStampaInfo = ft.ElevatedButton(content="Stampa sommario", on_click=self._controller.stampaSommario, width=200)

        row3 = ft.Row(controls=[self._btnAdd, self._btnGestisciOrdine, self._btnGestisciAllOrdini, self._btnStampaInfo],
                      alignment=ft.MainAxisAlignment.CENTER)

        self._lvOut = ft.ListView(expand=True)

        self._page.add(row_title, row1, row2, row3, self._lvOut)
        self.update_page()

    def set_controller(self, c):
        self._controller = c

    def update_page(self):
        self._page.update()

    @property
    def NomeProdotto(self):
        return self._NomeProdotto

    @property
    def Prezzo(self):
        return self._Prezzo

    @property
    def Quantita(self):
        return self._Quantita

    @property
    def NomeCliente(self):
        return self._NomeCliente

    @property
    def Mail(self):
        return self._Mail

    @property
    def Categoria(self):
        return self._Categoria

    @property
    def lvOut(self):
        return self._lvOut