class View():
     def viewMainMenu(self):
        print("Выберите действие:")
        print("\t1. Просмотр всех заметок")
        print("\t2. Поиск заметки по id")
        print("\t3. Добавление заметки")
        print("\t4. Редактировать заметки")
        print("\t5. Удаление заметки")
        print("\t6. Закрыть программу")

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
