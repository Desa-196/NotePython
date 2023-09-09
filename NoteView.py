class NoteView():
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
            if isinstance(readInt, int) and readInt > 0 and readInt <= 5:
                return readInt
