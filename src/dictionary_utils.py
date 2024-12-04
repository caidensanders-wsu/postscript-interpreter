#
# Copyright (c) Caiden Sanders and affiliates
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
#

from functools import partial

from operations.arithmetic import operations as arithmetic_operations
from operations.stack import operations as stack_operations
from operations.string import operations as string_operations
from operations.dictionary import operations as dictionary_operations
from operations.comparison import operations as comparison_operations
from operations.control_flow import operations as control_flow_operations
from operations.io import operations as io_operations
from operations.misc import operations as misc_operations

def load_operations_into_dictionary(dictionary_stack, operand_stack, process_input):
    """
    Loads all operations into the root dictionary of the dictionary stack.

    Args:
        dictionary_stack (Stack): The stack containing dictionaries.
        operand_stack (Stack): The stack for operands.
        process_input (function): Function to process input dynamically.
    """

    # Ensure the root dictionary exists
    if dictionary_stack.size() == 0:
        dictionary_stack.push((0, {}))

    # Get the root dictionary (first dictionary in the stack)
    _, root_dict = dictionary_stack.items[0]

    # Load all categories of operations into the root dictionary
    for name, operation in arithmetic_operations.items():
        root_dict[name] = partial(operation, operand_stack)

    for name, operation in stack_operations.items():
        root_dict[name] = partial(operation, operand_stack)

    for name, operation in string_operations.items():
        root_dict[name] = partial(operation, operand_stack)

    for name, operation in dictionary_operations.items():
        root_dict[name] = partial(operation, operand_stack, dictionary_stack)

    for name, operation in comparison_operations.items():
        root_dict[name] = partial(operation, operand_stack)

    for name, operation in control_flow_operations.items():
        root_dict[name] = partial(operation, operand_stack, process_input)

    for name, operation in io_operations.items():
        root_dict[name] = partial(operation, operand_stack)

    for name, operation in misc_operations.items():
        root_dict[name] = partial(operation, operand_stack)