"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=0):
        """Initialize the generator with a starting number."""
        self.start = start
        self.next_num = start

    def __repr__(self):
        """Provide representation."""
        return f"<SerialGenerator start={self.start} next={self.next_num}>"

    def generate(self):
        """Generate the next sequential number."""
        result = self.next_num
        self.next_num += 1
        return result

    def reset(self):
        """Reset the generator back to the original starting number."""
        self.next_num = self.start
