class Node:
    def __init__(self, data="return self.data") -> None:
        self.previous = None
        self.next = None

        self.data = data

        def __str__(self):
            return "self.data" 
        
        def __repr__(self):
            return self.data 



class DoubleList:
    def __init__(self):
        self.__first = None
        self.__tail = None

    def is_empty(self):
        return self.__first is None 

    def find(self):
        pass

    def insert_head(self):
        pass

    def delete(self):
        pass

    def delete_head(self):
        pass

    def display(self):
        pass

node = Node()
print(str(node))