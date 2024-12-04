#
# Copyright (c) Caiden Sanders and affiliates
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
#

import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'config')))

from structures.limiteddict import LimitedDict

def dict_operation(operand_stack, dictionary_stack):
    """
    Created a new LimitedDict with a maximum size defined by the top of the
    operand stack. Pushes the created dictionary onto the operand stack.
    
    Args:
        operand_stack (Stack): The stack containing operands.
        dictionary_stack (func): The stack containing dictionaries.
    """

    if operand_stack.size() < 1:
        print("not enough operands.")
        return

    max_length = operand_stack.pop()

    if not isinstance(max_length, int) or max_length <= 0:
        print("max_length must be a positive integer.")
        operand_stack.push(max_length)
        return

    operand_stack.push(LimitedDict(max_length))

def maxlength_operation(operand_stack, dictionary_stack):
    """
    Pops a dictionary from the operand stack and pushes its max length.
    
    Args:
        operand_stack (Stack): The stack containing operands.
        dictionary_stack (func): The stack containing dictionaries.
    """

    if operand_stack.size() < 1:
        print("not enough operands.")
        return
    
    op = operand_stack.pop()

    if not isinstance(op, LimitedDict):
        print("operand must be a dictionary.")
        operand_stack.push(op)
        return

    max_length = op.get_max_length()
    operand_stack.push(max_length)

def begin_operation(operand_stack, dictionary_stack):
    """
    Pops a dictionary from the operand stack and pushes it onto the dictionary
    stack.
    
    Args:
        operand_stack (Stack): The stack containing operands.
        dictionary_stack (func): The stack containing dictionaries.
    """

    if operand_stack.size() < 1:
        print("not enough operands.")
        return

    dictionary = operand_stack.pop()

    if not isinstance(dictionary, LimitedDict):
        print("operand must be a dictionary.")
        operand_stack.push(dictionary)
        return

    # Use the current top dictionary's static link or root link if empty
    static_link = dictionary_stack.items[-1][0] if dictionary_stack.size() > 0 else 0
    dictionary_stack.push((static_link, dictionary))

def end_operation(operand_stack, dictionary_stack):
    """
    Pops the top dictionary from the dictionary stack.
    
    Args:
        operand_stack (Stack): The stack containing operands.
        dictionary_stack (func): The stack containing dictionaries.
    """

    if dictionary_stack.size() < 1:
        print("no dictionary to add.")
        return
    
    dictionary_stack.pop()

def def_operation(operand_stack, dictionary_stack):
    """
    Implements the 'def' operation for defining a variable or procedure
    in the dictionary stack.
    
    Args:
        operand_stack (Stack): The stack containing operands.
        dictionary_stack (Stack): The stack containing dictionaries.
    """
    if operand_stack.size() < 2:
        print("Error: 'def' requires two operands.")
        return

    value = operand_stack.pop()
    name = operand_stack.pop()

    if not isinstance(name, str) or not name.startswith("/"):
        print("Error: Name must start with '/'.")
        operand_stack.push(name)
        operand_stack.push(value)
        return

    key = name[1:]  # Remove the leading '/'

    # Add to the top dictionary in the dictionary stack
    static_link, current_dict = dictionary_stack.peek()

    # If the value is a code block (list), store it with the current static link
    if isinstance(value, list):
        current_dict[key] = (value, dictionary_stack.size() - 1)
    else:
        current_dict[key] = value

operations = {
    "dict": dict_operation,
    "maxlength": maxlength_operation,
    "begin": begin_operation,
    "end": end_operation,
    "def": def_operation
}
