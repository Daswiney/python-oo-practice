"""Word Finder: finds random words from a dictionary."""


import random

class WordFinder:
    """A class for reading and retrieving random words from a file.

    Example:
    
    >>> wf = WordFinder("test.txt")
    5 words read

    >>> word = wf.random()
    >>> isinstance(word, str)
    True

    >>> word in wf.words
    True
    """

    def __init__(self, filepath):
        """Initialize the WordFinder with words from the given file."""
        self.words = self.read_words(filepath)
        self.num_words = len(self.words)
        print(f"{self.num_words} words read")

    def read_words(self, filepath):
        """Read words from the file and return them as a list."""
        with open(filepath, 'r') as file:
            return [line.strip() for line in file]

    def random(self):
        """Return a random word from the list of words."""
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    """A subclass of WordFinder that excludes blank lines and comments.

    Example:

    >>> wf = SpecialWordFinder("word.txt")
    9 words read

    >>> word = wf.random()
    >>> isinstance(word, str)
    True

    >>> word in wf.words
    True

    >>> '#' not in word
    True

    >>> '' not in wf.words
    True
    """

    def read_words(self, filepath):
        """Read and filter words from the file, excluding blank lines and comments."""
        words = super().read_words(filepath)  
        return [word for word in words if word and not word.startswith("#")]

if __name__ == "__main__":
    import doctest
    doctest.testmod()