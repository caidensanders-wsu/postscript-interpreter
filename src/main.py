#
# Copyright (c) Caiden Sanders and affiliates
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
#

from structures.stack import Stack

from parser import parse
from tokenizer import tokenize
from process import process_constants

from dictionary_utils import load_operations_into_dictionary

from globals import use_static_scoping

operand_stack = Stack()
dictionary_stack = Stack()

def interpret(tokens):
    """
    Interpret a list of parsed tokens by processing constants or executing operations.

    Args:
        tokens (list): A list of tokens to interpret.
    """

    for token in tokens:
        # Attempt to process the token as a constant
        is_constant, processed_value = process_constants(token, dictionary_stack)
        
        if is_constant:
            operand_stack.push(processed_value)
            continue  # Move to the next token

        # Lookup the token in the dictionary stack
        operation = lookup(token)
        
        if callable(operation):
            operation()  # Execute the operation
        elif isinstance(operation, tuple):
            # Assuming a tuple represents a procedure with a static link
            procedure, static_link = operation
            execute_procedure(procedure, static_link)
        elif isinstance(operation, list):
            # If the operation is a code block, interpret it recursively
            interpret(operation)
        elif operation is not None:
            operand_stack.push(operation)
        else:
            raise ValueError(f"Undefined name: {token}")
        
def execute_procedure(procedure, static_link):
    """
    Execute a procedure with a given static link.

    Args:
        procedure (list): The list of tokens representing the procedure.
        static_link (int): The index or reference to the static link in the dictionary stack.
    """
    
    dictionary_stack.push((static_link, {}))
    interpret(procedure)
    dictionary_stack.pop()

load_operations_into_dictionary(dictionary_stack, operand_stack, interpret)

def lookup(name):
    """
    Look up a name in the dictionary stack using static or dynamic scoping.

    Args:
        name (str): The name to look up.

    Returns:
        The value associated with the name.

    Raises:
        ValueError: If the name is not a string.
        ValueError: If the name is not found in the dictionary stack.
    """

    if not isinstance(name, str):
        raise ValueError(f"Invalid name: {name}")

    # Search for both with and without /
    search_names = [name, f"/{name}"]

    for search_name in search_names:
        result = search_dictionary_stack(search_name)
        if result is not None:
            return result

    raise ValueError(f"Undefined name: {name}")

def search_dictionary_stack(name):
    """
    Search for a name in the dictionary stack based on the current scoping rules.

    Args:
        name (str): The name to search for.

    Returns:
        The associated value if found; otherwise, None.
    """

    current_index = dictionary_stack.size() - 1

    while current_index >= 0:
        static_link, current_dict = dictionary_stack.items[current_index]
        if name in current_dict:
            return current_dict[name]
        if use_static_scoping:
            current_index = static_link
        else:
            current_index -= 1

    return None

# For debugging purposes
# Displays the operand stack & dictionary stack

# def stack():
#     """
#     Print the operand and dictionary stacks for debugging.
#     """
#     print("Operand Stack:")
#     for item in reversed(operand_stack.items):
#         print(item)
#     print("\nDictionary Stack:")
#     for i, (static_link, d) in enumerate(dictionary_stack.items):
#         print(f"Dict {i} (static link: {static_link}): {d}")
#     print("\n")

def repl():
    while user_input := input("REPL> "):
        try:
            if user_input == "quit":
                break

            tokens = parse(tokenize(user_input))

            interpret(tokens)

            print(f"Operand Stack: {operand_stack}")
        except Exception as e:
            print(f"Error: {e}")

repl()