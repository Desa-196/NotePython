class Presenter:
    def __init__(self, noteView, noteModel):
        self.View = noteView
        self.Model = noteModel

    def run(self):
        while True:
            self.View.view_main_menu()
            numMenu = self.View.read_num_main_menu()
            if (numMenu == 2):
                array_nate_parameter = self.View.get_new_note()
                self.Model.create_new_note(array_nate_parameter[0], array_nate_parameter[1])
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
            elif(numMenu == 5):
                break
            elif(numMenu == 1):
                self.View.view_all_note(self.Model.get_all_note())
            elif(numMenu == 4):
                id = self.View.remove_note()
                self.Model.remove_note(id)
