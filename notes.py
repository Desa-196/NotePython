from Presenter import Presenter
from View import View
from Model import Model

noteModel = Model()
noteView = View()
notePresenter = Presenter(noteView, noteModel)
notePresenter.run()