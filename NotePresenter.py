class NotePresenter:
    def __init__(self, noteView, noteModel):
        self.noteView = noteView
        self.noteModel = noteModel
    def run(self):
        self.noteView.viewMainMenu()
        numMenu = self.noteView.readNumMainMenu()