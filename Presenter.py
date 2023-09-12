class Presenter:
    def __init__(self, noteView, noteModel):
        self.View = noteView
        self.Model = noteModel

    def run(self):
        while True:
            #Выводим меню
            self.View.view_main_menu()
            #запрашиваем пользователя выбрать необходимый пункт меню
            numMenu = self.View.read_num_main_menu()
            #В зависимости от выбора выполняем действие
            #Если выбрали 1-й пункт, запрашиваем у модели список всех заметок и отдаем его представлению для отображения
            if(numMenu == 1):
                self.View.view_all_note(self.Model.get_all_note())

            #Если 2-й - запрашиваем через представление у пользователя параметры для создания поной заметки и передаем их модели
            elif (numMenu == 2):
                array_nate_parameter = self.View.get_new_note()
                self.Model.create_new_note(array_nate_parameter[0], array_nate_parameter[1])

            #Запрашиваем у пользователя id заметки для редактирования, передем его модели и если есть такая заметка
            #просим ввести данные для редактирования, если нет, сообщаем об этом
            elif(numMenu == 3):
                id = self.View.read_id_note()
                note = self.Model.get_note_by_id(id)
                if note != None:
                    new_parameter_note = self.View.edit_note(note.title, note.text)
                    if(note.title != new_parameter_note[0]):
                        self.Model.change_title_note(id, new_parameter_note[0])
                    if(note.text != new_parameter_note[1]):
                        self.Model.change_text_note(id, new_parameter_note[1])
                else:
                    self.View.error_message(f"Заметка с id = {id} отсутствует")
            #Если 4-й пункт меню, запрашиваем id заметки которую необходимо удалить и удаляем если такая есть, если нет, ничего не делаем
            elif(numMenu == 4):
                id = self.View.remove_note()
                self.Model.remove_note(id)
            #Если 5 то выходим из цикла while, что приведет к выходу из программы
            elif(numMenu == 5):
                break
