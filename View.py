class View():
    def viewMainMenu(self):
        print("Выберите действие:")
        print("\t1. Просмотр всех заметок")
        print("\t2. Добавление заметки")
        print("\t3. Редактировать заметки")
        print("\t4. Удаление заметки")
        print("\t5. Закрыть программу")

    def read_id_note(self):
        print("Введите id заметки для редактирования: ")
        return self.read_int()
     
    def edit_note(self, title, text):
        array_note_parameter = []
        print(f"Введите новый заголовок или оставьте поле пустым для сохранения старого({title})", end=None)
        array_note_parameter.append (input() or title)
        print(f"Введите новый текст или оставьте поле пустым для сохранения старого({text})", end=None)
        array_note_parameter.append(input() or text)
        return array_note_parameter
    
    def error_message(self, text):
        print(text)

    def readNumMainMenu(self):
        while (True):
            print("Введите необходимый пункт меню: ", end=None)
            readInt = self.read_int()
            if readInt > 0 and readInt <= 6:
                return readInt
            else:
                print("Такой номер меню отсутствует!")

    def read_int(self):
        while (True):
            readInt = input()
            try:
                readInt = int(readInt)
                return readInt
            except ValueError:
                print("Ошибка ввода!")
                continue

    def get_new_note(self):
        array_note_parameter = []
        array_note_parameter.append(input("Введите название заметки: "))
        array_note_parameter.append(input("Введите текст заметки: "))
        return array_note_parameter

    def remove_note(self):
        print("Введите id заметки для удаления: ", end=None)
        return self.read_int()

    def view_all_note(self, array_notes):
        for note in array_notes:
            print(note)
