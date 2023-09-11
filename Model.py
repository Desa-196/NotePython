from Note import Note
from datetime import datetime


class Model:
    array_notes = []

    def get_all_note(self):
        return self.array_notes

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
