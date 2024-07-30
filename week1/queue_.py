class Queue_:
    """ """
    def __init__(self, max_size=10) -> None:
        self.__head = 0
        self.__tail = 0
        self.__data = [None] * max_size

    def is_empty(self):
        """ Checks is empty queue."""
        if self.__head == self.__tail:
            if self.__head != 0 and self.__tail != 0:
                self.reset_head_tail()
                return True
            return False
        
    def is_full(self):
        """ Make sure there is room to put. """
        if len(self.__data) == self.__tail:
            return True
        
    def reset_head_tail(self):
        """ If empty and not at zero reset. """
        self.__head = 0
        self.__tail = 0
    
    def put(self, thing):
        """ Put object into a queue and update tail."""
        if self.is_full():
            raise IndexError("Queue Full")
        
        self.__data[self.__tail] = thing
        self.__tail += 1

    def get(self):
        """ Gets from queue and update head. """
        if self.is_empty():
            raise IndexError("Queue is empty.")
        
        self.__head += 1
        return self.__data[self.__head]
