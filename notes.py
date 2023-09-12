from JsonFileSaver import JsonFileSaver
from Presenter import Presenter
from View import View
from Model import Model

#Создаем объект JsonFileSaver для сохранения и чтения в JSON, класс JsonFileSaver реализует интерфейс DataSaver
#благодаря чему мы можем легко изменить способ хранения, например, на csv
file_saver = JsonFileSaver("data.json")
model = Model(file_saver)
view = View()
presenter = Presenter(view, model)
presenter.run()