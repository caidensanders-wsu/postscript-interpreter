#
# Copyright (c) Caiden Sanders and affiliates
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
#

def exch_operation(stack):
	"""
	Swaps the top two items on the stack.
	
	Args:
        stack (Stack): The stack containing operands.
	"""

	if stack.size() < 2:
		print("not enough operands.")
		return

	op1 = stack.pop()
	op2 = stack.pop()

	stack.push(op1)
	stack.push(op2)

def pop_operation(stack):
	"""
	Removes the top item from the stack.
	
	Args:
        stack (Stack): The stack containing operands.
	"""

	if stack.size() < 1:
		print("not enough operands.")
		return

	stack.pop()

def copy_operation(stack):
	"""
	Pops an integer n from the stack and duplicates the top n items, preserving
	their orders.
	
	Args:
        stack (Stack): The stack containing operands.
	"""

	if stack.size() < 1:
		print("not enough operands.")
		return

	num_to_copy = stack.pop()

	if not isinstance(num_to_copy, int) or num_to_copy < 0:
		print("operand must be a non-negative integer.")
		stack.push(num_to_copy)
		return

	if stack.size() < num_to_copy:
		print("not enough operands.")
		stack.push(num_to_copy)
		return

	items = []
	for _ in range(num_to_copy):
		items.append(stack.pop())

	# Push the original items back into the stack with order preserved.
	for item in reversed(items):
		stack.push(item)

	# Now push a duplicate batch of those items, also wtih order preserved.
	for item in reversed(items):
		stack.push(item)
		

def dup_operation(stack):
	"""
	Duplicates the top item on the stack.
	
	Args:
        stack (Stack): The stack containing operands.
	"""

	if stack.size() < 1:
		print("not enough operands.")
		return

	op = stack.peek()
	stack.push(op)

def clear_operation(stack):
	"""
	Clears all items from the stack.
	
	Args:
        stack (Stack): The stack containing operands.
	"""

	while not stack.is_empty():
		stack.pop()
	
def count_operation(stack):
	"""
	Counts the number of items in the stack and pushes the count onto the
	stack.
	
	Args:
        stack (Stack): The stack containing operands.
	"""

	count = stack.size()
	stack.push(count)
	
operations = {
	"exch": exch_operation,
	"pop": pop_operation,
	"copy": copy_operation,
	"dup": dup_operation,
	"clear": clear_operation,
	"count": count_operation
}