class Buffer:
    """
    Class for a rotating character buffer.
    """

    buffer_size = 4
    buffer: list[str]

    def __init__(self, size: int = 4) -> None:
        """
        Create the class.
        """
        self.buffer = []
        self.buffer_size = size

    def add(self, input_str: str) -> bool:
        """
        Add to the buffer and return True if marker is found.
        """
        found_marker = False
        for c in input_str:
            self.buffer.append(c)
            if len(self.buffer) > self.buffer_size:
                self.buffer.pop(0)
            found_marker = self.find_marker()
            if found_marker:
                break

        return found_marker

    def find_marker(self) -> bool:
        """
        Find the marker pattern.
        """
        if len(self.buffer) < self.buffer_size:
            return False

        for c in self.buffer:
            tmp = [i for i in self.buffer if i != c]
            if len(tmp) < self.buffer_size - 1:
                return False
        return True
