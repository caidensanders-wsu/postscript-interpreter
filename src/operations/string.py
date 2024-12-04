#
# Copyright (c) Caiden Sanders and affiliates
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
#

def get_operation(stack):
	"""
	Pops an index and a string from the stack. Pushes the character at the
	specified index of the string back onto the stack.
	
	Args:
        dictionary_stack (Stack): The stack containing dictionaries.
	"""

	if stack.size() < 2:
		print("not enough operands.")
		return

	index = stack.pop()
	op = stack.pop()

	if not isinstance(op, str):
		print("operand must be a string.")
		stack.push(op)
		stack.push(index)
		return
	
	if not isinstance(index, int):
		print("index must be an integer.")
		stack.push(op)
		stack.push(index)
		return

	if index < 0 or index >= len(op):
		print("index out of bounds.")
		stack.push(op)
		stack.push(index)
		return

	stack.push(op[index])

def get_interval_operation(stack):
	"""
	Pops a count, an index, and a string from the stack. Pushes a substring
	(interval) of the string back onto the stack.
	
	Args:
        dictionary_stack (Stack): The stack containing dictionaries.
	"""

	if stack.size() < 3:
		print("not enough operands.")
		return

	count = stack.pop()
	index = stack.pop()
	op = stack.pop()

	if not isinstance(op, str):
		print("operand must be a string.")
		stack.push(op)
		stack.push(index)
		stack.push(count)
		return

	if not (isinstance(index, int) and isinstance(count, int)):
		print("index and count must be integers.")
		stack.push(op)
		stack.push(index)
		stack.push(count)
		return

	if index < 0 or index + count > len(op) or count < 0:
		print("index or count out of bounds.")
		stack.push(op)
		stack.push(index)
		stack.push(count)
		return

	stack.push(op[index : index + count])

def put_interval_operation(stack):
	"""
	Pops two strings (string1 and string2) and an index from the stack. Inserts
	string2 into string1 at the specified index and pushes the result back onto
	the stack.
	
	Args:
        dictionary_stack (Stack): The stack containing dictionaries.
	"""

	if stack.size() < 3:
		print("not enough operands.")
		return

	string2 = stack.pop()
	index = stack.pop()
	string1 = stack.pop()

	if not (isinstance(string1, str) or isinstance(string2, str)):
		print("both operands must be strings.")
		stack.push(string1)
		stack.push(index)
		stack.push(string2)
		return

	if not isinstance(index, int):
		print("index must be an integer.")
		stack.push(string1)
		stack.push(index)
		stack.push(string2)
		return

	if index < 0 or index > len(string1):
		print("index out of bounds.")
		stack.push(string1)
		stack.push(index)
		stack.push(string2)
		return

	stack.push(string1[:index] + string2 + string1[index:])
	
operations = {
	"get": get_operation,
	"getinterval": get_interval_operation,
	"putinterval": put_interval_operation,
}