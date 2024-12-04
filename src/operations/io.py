#
# Copyright (c) Caiden Sanders and affiliates
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
#

def print_operation(stack):
	"""
	Prints the top item on the stack if it is a string. Removes the item from
	the stack.
	
	Args:
        stack (Stack): The stack containing operands.
	"""

	if stack.size() < 1:
		print("not enough operands")
		return

	if isinstance(stack.peek(), str):
		print(stack.pop())
	else:
		print("operand is not a string.")

def equals_print_operation(stack):
	"""
	Prints the top item on the stack, regardless of its type. Removes the item
	from the stack.
	
	Args:
        stack (Stack): The stack containing operands.
	"""

	if stack.size() < 1:
		print("not enough operands.")
		return

	print(stack.pop())

def double_equals_print_operation(stack):
	"""
	Prints the top item on the stack. If the item is a string, wrap it in
	parentheses. Removes item from the stack.
	
	Args:
        stack (Stack): The stack containing operands.
	"""

	if stack.size() < 1:
		print("not enough operands.")
		return

	op = stack.pop()

	if isinstance(op, str):
		print('(' + op + ')')
	else:
		print(op)

def pstack_operation(stack):
	"""
	Prints all items in the stack without modifying their order or removing
	them. Strings are wrapped in parentheses.
	
	Args:
        stack (Stack): The stack containing operands.
	"""
	
	if stack.size() < 1:
		print("not enough operands.")
		return

	items = []

	try:
		# Pop all items from stack and store them in a list.
		while True:
			items.append(stack.pop())
	except IndexError:
		# Once stack is empty, print and restore the items in the list.
		for item in items:
			if isinstance(item, str):
				print('(' + item + ')')
			else:
				print(item)
		for item in reversed(items):
			stack.push(item)
			
operations = {
	"print": print_operation,
	"=": equals_print_operation,
	"==": double_equals_print_operation,
	"pstack": pstack_operation,
}