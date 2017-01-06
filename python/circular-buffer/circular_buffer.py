class BufferFullException(Exception):
    pass

class BufferEmptyException(Exception):
    pass

class CircularBuffer(object):

    def __init__(self, length):
        self._len = length
        self._buffer = [None for _ in range(length)]
        self._current = 0
        self._oldest = 0

    def clear(self):
        self.__init__(self._len)

    def write(self, datum):
        if self._buffer[self._current] is not None:
            raise BufferFullException('Buffer is full')
        else:
            self._buffer[self._current] = datum
            self._current = (self._current + 1) % self._len

    def read(self):
        if self._buffer[self._oldest] is None:
            raise BufferEmptyException('Buffer is empty')
        else:
            od, self._buffer[self._oldest] = self._buffer[self._oldest], None
            self._oldest = (self._oldest + 1) % self._len
            return od

    def overwrite(self, datum):
        self._buffer[self._oldest] = datum
        self._oldest = (self._oldest + 1) % self._len
