#
# Copyright (c) Caiden Sanders and affiliates
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
#

def if_operation(stack, parser):
	"""
	Pops a condition and a code block from the stack. Executes the code
	block if the condition is true.
	
	Args:
        stack (Stack): The stack containing operands.
		parser (func): A function to parse the input.
	"""

	if stack.size() < 2:
		print("not enough operands.")
		return
	
	if not isinstance(stack.peek(), list):
		print("must be a codeblock.")
		return

	proc = stack.pop()
	truth = stack.pop()

	if truth:
		parser(proc)

def ifelse_operation(stack, parser):
	"""
	Pops a condition and two code blocks from the stack. Executes the
	first code block if the condition is true; otherwise, executes the
	second code block.
	
	Args:
        stack (Stack): The stack containing operands.
		parser (func): A function to parse the input.
	"""

	if stack.size() < 3:
		print("not enough operands.")
		return
	
	if not isinstance(stack.peek(), list):
		print("must be a codeblock.")
		return

	proc1 = stack.pop()

	if not isinstance(stack.peek(), list):
		print("must be a codeblock.")
		stack.push(proc1)
		return

	proc2 = stack.pop()
	truth = stack.pop()

	if truth:
		parser(proc2)
	else:
		parser(proc1)

def for_operation(stack, parser):
	"""
	Pops a code block and three numbers (start, increment, end) from the stack.
	Executes the code block in a loop, incrementing from start to end.
	
	Args:
        stack (Stack): The stack containing operands.
		parser (func): A function to parse the input.
	"""

	if stack.size() < 4:
		print("not enough operands.")
		return

	if not isinstance(stack.peek(), list):
		print("must be a codeblock.")
		return

	proc = stack.pop()
	end = stack.pop()
	increment = stack.pop()
	start = stack.pop()
	
	if not all(isinstance(x, (int, float)) for x in [start, increment, end]):
		print("start, increment, and end must be numbers.")
		stack.push(start)
		stack.push(increment)
		stack.push(end)
		stack.push(proc)
		return
	
	if increment > 0:
		condition = lambda i: i <= end
	elif increment < 0:
		condition = lambda i: i >= end
	else:
		print("increment cannot be zero.")
		stack.push(start)
		stack.push(increment)
		stack.push(end)
		stack.push(proc)
		return
	
	i = start
	while condition(i):
		stack.push(i)
		parser(proc)

		i += increment

def repeat_operation(stack, parser):
	"""
	Pops a count and a code block (list) from the stack. Repeats the code block
	count times.
	
	Args:
        stack (Stack): The stack containing operands.
		parser (func): A function to parse the input.
	"""

	if stack.size() < 2:
		print("not enough operands.")
		return

	if not isinstance(stack.peek(), list):
		print("must be a codeblock.")
		return

	proc = stack.pop()
	count = stack.pop()

	if not isinstance(count, int) or count < 0:
		print("count must be a non-negative integer.")
		stack.push(count)
		stack.push(proc)
		return

	for _ in range(count):
		parser(proc)

operations = {
	"if": if_operation,
	"ifelse": ifelse_operation,
	"for": for_operation,
	"repeat": repeat_operation,
}