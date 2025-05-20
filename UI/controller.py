import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

        self._listYear = []
        self._listCountry = []

    def fillDD(self):
        for country in self._model.getDifferentCountry():
            self._view.ddcountry.options.append(ft.dropdown.Option(country))

        for year in self._model.anni:
            self._view.ddyear.options.append(ft.dropdown.Option(year))




    def handle_graph(self, e):
        anno = int(self._view.ddyear.value) # controlli sull'intero da fare
        country = self._view.ddcountry.value
        self._view.txt_result.controls.clear()
        self._model.buildGraph(country, anno)
        self._view.txt_result.controls.append(ft.Text(f"grafo creato con {len(self._model._grafo.nodes)} nodi e {len(self._model._grafo.edges)} archi"))
        self._view.update_page()



    def handle_volume(self, e):
        self._view.txtOut2.controls.clear()
        for tupla in self._model.getVolume():
            self._view.txtOut2.controls.append(ft.Text(f"Il volume del retailer {tupla[0]} è {tupla[1]}"))
        self._view.update_page()


    def handle_path(self, e):
        pass
