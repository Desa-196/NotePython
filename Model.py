from Note import Note
from datetime import datetime


class Model:
    array_notes = []

    def get_all_note(self):
        return self.array_notes

    def get_note_by_id(self, id):
        note = list(filter(lambda x: x.id == id, self.array_notes))
        if len(note) > 0:
            return note[0]
        else:
            return None
        
    def change_title_note(self, id, title):
        note = self.get_note_by_id(id)
        if note != None:
            note.title = title
            note.date_time = datetime.now()
        
    def change_text_note(self, id, text):
        note = self.get_note_by_id(id)
        if note != None:
            note.text = text
            note.date_time = datetime.now()

    def create_new_note(self, title, text):
        self.array_notes.append(
            Note((self.get_max_id()) + 1, title, text, datetime.now()))
        print(self.array_notes[0])

    def remove_note(self, id):
        self.array_notes = list(filter(lambda x: x.id != id, self.array_notes))

    def get_max_id(self):
        if not self.array_notes:
            return -1
        return max(self.array_notes, key=lambda x: x.id).id
