#
# Copyright (c) Caiden Sanders and affiliates
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
#

def eq_operation(stack):
	"""
	Compare the top two items for equality. Pushes True if they are equal,
	otherwise False.
	
	Args:
        stack (Stack): The stack containing operands.
	"""

	if stack.size() < 2:
		print("not enough operands.")
		return
	
	op1 = stack.pop()
	op2 = stack.pop()
	res = op1 == op2
	stack.push(res)

def ne_operation(stack):
	"""
	Compares the top two items on the stack for inequality. Pushes True if they
	are not equal, otherwise False.
	
	Args:
        stack (Stack): The stack containing operands.
	"""

	if stack.size() < 2:
		print("not enough operands.")
		return

	op1 = stack.pop()
	op2 = stack.pop()
	res = not (op1 == op2)
	stack.push(res)

def ge_operation(stack):
	"""
	Checks if the second-to-top item is greater than or equal to the top item
	on the stack. Pushes True if it is, otherwise False.
	
	Args:
        stack (Stack): The stack containing operands.
	"""

	if stack.size() < 2:
		print("not enough operands.")
		return

	op1 = stack.pop()
	op2 = stack.pop()
	res = op2 >= op1
	stack.push(res)

def gt_operation(stack):
	"""
	Checks if the second-to-top item is greater than the top items on the
	stack. Pushes True if it is, otherwise False.
	
	Args:
        stack (Stack): The stack containing operands.
	"""

	if stack.size() < 2:
		print("not enough operands.")
		return

	op1 = stack.pop()
	op2 = stack.pop()
	res = op2 > op1
	stack.push(res)

def le_operation(stack):
	"""
	Checks if the second-to-top item is less than or equal to the top item on
	the stack. Pushes True if it is, otherwise False.
	
	Args:
        stack (Stack): The stack containing operands.
	"""

	if stack.size() < 2:
		print("not enough operands.")
		return

	op1 = stack.pop()
	op2 = stack.pop()
	res = op2 <= op1
	stack.push(res)

def lt_operation(stack):
	"""
	Checks if the second-to-top item is less than the top item on the stack.
	Pushes True if it is, otherwise False.
	
	Args:
        stack (Stack): The stack containing operands.
	"""

	if stack.size() < 2:
		print("not enough operands.")
		return

	op1 = stack.pop()
	op2 = stack.pop()
	res = op2 < op1
	stack.push(res)

def and_operation(stack):
	"""
	Performs a logical AND operation on the top two items on the stack. Pushes
	the result (True or False).
	
	Args:
        stack (Stack): The stack containing operands.
	"""

	if stack.size() < 2:
		print("not enough operands.")
		return

	op1 = stack.pop()
	op2 = stack.pop()
	res = bool(op1) and bool(op2)
	stack.push(res)

def not_operation(stack):
	"""
	Performs a logical NOT operation on the top item on the stack. Pushes the
	result (True or False).
	
	Args:
		stack (Stack): The stack containing oeprands.
	"""

	if stack.size() < 1:
		print("not enough operands.")
		return
	
	op = stack.pop()
	res = not bool(op)
	stack.push(res)

def or_operation(stack):
	"""
	Performs a lgoical OR operation on the top two items on the stack. Pushes
	the result (True or False)
	
	Args:
        stack (Stack): The stack containing operands.
	"""

	if stack.size() < 2:
		print("not enough operands.")
		return

	op1 = stack.pop()
	op2 = stack.pop()
	res = bool(op1) or bool(op2)
	stack.push(res)

operations = {
	"eq": eq_operation,
	"ne": ne_operation,
	"ge": ge_operation,
	"gt": gt_operation,
	"le": le_operation,
	"lt": lt_operation,
	"and": and_operation,
	"not": not_oepration,
	"or": or_operation,
}