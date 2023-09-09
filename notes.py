from NotePresenter import NotePresenter
from NoteView import NoteView
from NoteModel import NoteModel

noteModel = NoteModel
noteView = NoteView
notePresenter = NotePresenter(noteView, noteModel)
notePresenter.run()