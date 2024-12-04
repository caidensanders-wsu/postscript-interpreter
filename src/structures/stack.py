#
# Copyright (c) Caiden Sanders and affiliates
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
#

class Stack:
    """
    A class representing a stack data structure.
    """

    def __init__(self):
        """
        Initializes an empty stack.
        """

        self.items = []

    def push(self, item):
        """
        Adds an item to the top of the stack.
        
        Args:
            item: The item to be added to the stack.
        """

        self.items.append(item)

    def pop(self):
        """
        Removes and returns the item at the top of the stack.
        
        Returns:
            The item at the top of the stack.

        Raises:
            IndexError: If the stack is empty.
        """

        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Pop from an empty stack")
        
    def peek(self):
        """
        Returns the item at the top of the stack without removing it.
        
        Returns:
            The item at the top of the stack.
            
        Raises:
            IndexError: If the stack is empty.
        """

        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Peek from an empty stack")
        
    def is_empty(self):
        """
        Checks if the stack is empty.

        Returns:
            True if te stack is empty, False otherwise.
        """

        return len(self.items) == 0
    
    def size(self):
        """
        Returns the number of items in the stack.
        
        Returns:
            The size of the stack as an integer.
        """

        return len(self.items)
    
    def __iter__(self):
        """
        Returns an iterable of the inner list.
        
        Returns:
            Iterable of the inner list
        """

        return iter(self.items)
    
    def __repr__(self):
        """
        Returns a string representation of the stack.
        
        Returns:
            A string representation of the stack's contents.
        """
        
        return str(self.items)