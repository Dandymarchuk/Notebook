"""
Module includes __init__, __str__, search, new_note, modify_memo, modify_tags functions.
"""
from note import Note

class Notebook:
    """
    Represents storage for notes with features for creating, modifying and searching.
    """
    def __init__(self: object, notes: list[Note] = []):
        """
        Initializes new notebook object with empty note by default.
        """
        self.notes = notes


    def __str__(self: object) -> str:
        """
        Returns string representation of notebook object, including notes.
        """
        notes = ''

        for note in self.notes:
            notes += f'{note}\n'

        return f'{notes}\n'


    def search(self: object, filter: str) -> list[Note]:
        """
        Search notes by specified filter.
        """
        matched_notes = []

        for note in self.notes:
            if note.match(filter):
                matched_notes.append(note)

        return matched_notes


    def new_note(self: object, memo: str, tags: str = ''):
        """
        Appends note to storage of all notes.
        """
        self.notes.append(Note(memo=memo, tags=tags.split()))


    def modify_memo(self: object, note_id: int, memo: str):
        """
        Modifies note text in storage using note id.
        """
        self.notes[note_id - 1].memo = memo


    def modify_tags(self: object, note_id: int, tags: str):
        """
        Modifies note tags in storage using note id.
        """
        self.notes[note_id - 1].tags = tags.split()
