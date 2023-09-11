class Presenter:
    def __init__(self, noteView, noteModel):
        self.noteView = noteView
        self.noteModel = noteModel

    def run(self):
        while True:
            self.noteView.viewMainMenu()
            numMenu = self.noteView.readNumMainMenu()
            if (numMenu == 3):
                array_nate_parameter = self.noteView.get_new_note()
                self.noteModel.create_new_note(array_nate_parameter[0], array_nate_parameter[1])
            elif(numMenu == 6):
                break
            elif(numMenu == 1):
                self.noteView.view_all_note(self.noteModel.get_all_note())
            elif(numMenu == 5):
                id = self.noteView.remove_note()
                self.noteModel.remove_note(id)
