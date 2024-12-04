#
# Copyright (c) Caiden Sanders and affiliates
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
#

def length_operation(operand_stack):
    """
    Pops the top item from the operand stack and pushes its length. The operand
    must be a string, dictionary, or any other object that supports `len()`.

    Args:
        stack (Stack): The stack containing operands.
    """
    
    if operand_stack.size() < 1:
        print("not enough operands.")
        return
    
    op = operand_stack.pop()

    if isinstance(op, str):
        operand_stack.push(len(op))
    elif isinstance(op, dict):
        operand_stack.push(len(op))
    elif hasattr(op, "__len__"):
        operand_stack.push(len(op))
    else:
        print("operand does not support length.")
        operand_stack.push(op)

operations = {
    "length": length_operation
}