class NoteView:
    def viewMainMenu():
        print("Выберите действие:")
        print("\t1. Просмотр всех заметок")
        print("\t2. Поиск заметки по id")
        print("\t3. Добавление заметки")
        print("\t4. Редактировать заметки")
        print("\t5. Удаление заметки")

    def readNumMainMenu():
        while (True):
          readInt = input("Введите необходимый пункт меню: ")
          try:
               readInt = int(readInt)
          except ValueError:
               print("Ошибка ввода!")
               continue
          if readInt > 0 and readInt <= 5:
                return readInt
          else:
              print("Такой номер меню отсутствует!")
