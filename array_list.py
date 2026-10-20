from abstract_list import AbstractList

class ArrayList(AbstractList):

    def __init__(self):
        self._array = [None] * 100
        self._size = 0


    def add(self, element):

        if  self._size < 100:
            self._array[self._size] = element
            self._size += 1


        else:
              raise OverflowError



    def remove(self, index):
        if index < self._size and index >= 0:
            target = self._array[index]

            for i in range(index, self._size - 1):
                self._array[i] = self._array[i + 1]

            self._array[self._size - 1] = None
            self._size -= 1
            return target

        else:
            raise IndexError




    def get(self, index):
        if index < self._size and index >= 0:
            return self._array[index]
        else:
            raise IndexError

    def set(self, index, element):
        if index < self._size and index >= 0:
            self._array[index] = element
        else:
            raise IndexError


    def getIndex(self, element):
        for i in range(self._size):
            if element == self._array[i]:
                return i

        return -1




    def size(self):
        return self._size

























