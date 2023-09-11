from Presenter import Presenter
from View import View
from Model import Model

model = Model()
view = View()
presenter = Presenter(view, model)
presenter.run()