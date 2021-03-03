"""
Module includes __init__, __str__, match functions.
"""
import datetime

class Note:
    """
    Represents note in Notebook class.
    """
    def __init__(self: object, memo: str, tags: list[str] = []):
        """
        Initializes note object with given memo, creation date (by default) and tags (optional).
        """
        self.memo = memo
        self.creation_date = datetime.datetime.now().ctime()
        self.tags = tags


    def __str__(self: object) -> str:
        """
        Returns string representation of note object.
        """
        tag_text = 'empty' if len(self.tags) == 0 else self.tags
        return f'Text: {self.memo}\nCreation date: {self.creation_date}\nTags: {tag_text}'


    def match(self: object, search_filter: str) -> bool:
        """
        Returns all notes that matches certain search filter.
        >>> Note('123').match('123')
        True
        """
        if search_filter.startswith('#'):
            for tag in self.tags:
                if search_filter in tag:
                    return True
            return False
        else:
            return search_filter in self.memo
