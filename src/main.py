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
    Interpret a list of parsed tokens.
    """
    for token in tokens:
        result = process_constants(token, dictionary_stack)

        if result:
            _, processed_value = result
            operand_stack.push(processed_value)
        else:
            val = lookup(token)
            if callable(val):
                val()
            elif isinstance(val, tuple) and len(val) == 2:  
                # Procedure with a static link
                proc, static_link = val
                dictionary_stack.push((static_link, {}))
                interpret(proc)
                dictionary_stack.pop()
            elif isinstance(val, list):
                # Execute a code block
                interpret(val)
            elif val is not None:
                operand_stack.push(val)
            else:
                raise ValueError(f"Undefined name: {token}")

load_operations_into_dictionary(dictionary_stack, operand_stack, interpret)

def lookup(name):
    """
    Look up a name using static or dynamic scoping.
    """
    if not isinstance(name, str):
        raise ValueError(f"Invalid name: {name}")

    # First, try looking up the name directly (for operators)
    current_index = dictionary_stack.size() - 1
    while current_index >= 0:
        static_link, current_dict = dictionary_stack.items[current_index]
        if name in current_dict:
            return current_dict[name]
        if use_static_scoping:
            # Follow the static link
            current_index = static_link
        else:
            # Dynamic scoping: go to the previous dictionary
            current_index -= 1

    # If not found, add a '/' prefix and try again (for variables/procedures)
    name = "/" + name
    current_index = dictionary_stack.size() - 1
    while current_index >= 0:
        static_link, current_dict = dictionary_stack.items[current_index]
        if name in current_dict:
            return current_dict[name]
        if use_static_scoping:
            # Follow the static link
            current_index = static_link
        else:
            # Dynamic scoping: go to the previous dictionary
            current_index -= 1

    raise ValueError(f"Undefined name: {name}")

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