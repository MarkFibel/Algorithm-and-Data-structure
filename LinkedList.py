class Box:
    def __init__(self, value):
        self.value = value
        self.next_box = None
        self.prev_box = None


class LinkedList:
    def __init__(self, *elements):
        self._start = None
        self._end = None
        self._start_values = elements
        self._size = 0
        for i in self._start_values:
            self.append(i)

    def append(self, *elements):
        __element = elements[0]
        if len(elements) == 1:
            __pos = None
        else:
            __pos = elements[1]
        new_box = Box(__element)
        solution_1 = self._start is None
        solution_2 = self._end is None
        if solution_1 or solution_2:

            if solution_1:
                self._start = new_box
            if solution_2:
                self._end = new_box

            self._size += 1
            return

        lastbox = self._start

        if __pos is None:

            while lastbox.next_box:
                lastbox = lastbox.next_box
            lastbox.next_box = new_box
        else:
            __boxIndex = 0
            while (__boxIndex <= __pos) and lastbox.next_box:
                if __boxIndex == __pos:
                    return lastbox.value
                __boxIndex = __boxIndex + 1
                lastbox = lastbox.next_box
        self._size += 1

    def remove(self, pos: int):
        lastbox = self._start
        additional_box = None
        if pos == 0:
            self._start = lastbox.next_box
            self._size -= 1
        else:
            box_index = 0
            while (box_index <= pos) and lastbox.next_box:
                if box_index == pos:
                    additional_box.next_box = lastbox.next_box
                    self._size -= 1
                    return
                box_index += 1
                additional_box = lastbox
                lastbox = lastbox.next_box

    def remove_last(self):
        '''
        :return: Удалить последний элемент
        '''
        lastbox = self._start

        while lastbox.next_box.next_box:
            lastbox = lastbox.next_box
        lastbox.next_box = None
        self._size -= 1

    def at(self, pos: int):
        '''
        :return: Элемент из позиции pos
        '''
        lastbox = self._start
        __boxIndex = 0
        while (__boxIndex <= pos) and (self._size >= pos):
            if __boxIndex == pos:
                return lastbox.value
            __boxIndex = __boxIndex + 1
            lastbox = lastbox.next_box
        return 'Not enough elements'

    def size(self):
        '''
        :return: Размер листа
        '''
        return self._size

    def remove_from_end_at(self, pos):
        '''
        :return: Удалить n-ый элемент с конца списка
        '''
        pos = self._size - pos - 1
        self.remove(pos)

    def list_show(self):
        return [self.at(i) for i in range(self._size)]
