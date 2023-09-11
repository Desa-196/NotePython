from JsonFileSaver import JsonFileSaver
from Presenter import Presenter
from View import View
from Model import Model

file_saver = JsonFileSaver("data.json")
model = Model(file_saver)
view = View()
presenter = Presenter(view, model)
presenter.run()