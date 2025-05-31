class Stack:
    CAPACITY: int = 10_000_000

    def __init__(self) -> None:
        self._items = []
    
    def __len__(self) -> int:
        return len(self._items)
    
    def is_empty(self) -> bool:
        return len(self) == 0
    
    def is_full(self) -> bool:
        return len(self) == self.CAPACITY
    
    def push(self, item: int) -> None:
        if type(item) != int:
            raise TypeError('The item must be an integer')
        if not self.is_full():
            self._items.append(item)
        else:
            raise OverflowError('Stack overflow error')
    
    def pop(self) -> int:
        if self.is_empty():
            raise IndexError('The stack is empty')
        return self._items.pop()
    
    def top(self) -> int:
        if self.is_empty():
            raise IndexError('The stack is empty')
        return self._items[-1]
    
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}()'
    
    def __str__(self) -> str:
        return f'{self.__class__.__name__}({str(self._items)[1:-1]})'
