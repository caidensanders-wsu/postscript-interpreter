#
# Copyright (c) Caiden Sanders and affiliates
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
#

import math

def add_operation(stack):
    """
    Adds the top two values from the stack and pushes the result back.
    
    Args:
        stack (Stack): The stack containing operands.
    """

    if stack.size() < 2:
        print("not enough operands.")
        return
    
    op1 = stack.pop()
    op2 = stack.pop()
    res = op1 + op2
    stack.push(res)

def div_operation(stack):
	"""
	Pops the top two items from the stack (divisor and dividend), performs
	division, and pushes the result.
      
    Args:
        stack (Stack): The stack containing operands.
	"""

	if stack.size() < 2:
		print("not enough operands.")
		return

	divisor = stack.pop()
	dividend = stack.pop()
	quotient = dividend / divisor
	stack.push(quotient)
      
def sub_operation(stack):
	"""
	Pops the top two items from the stack (subtrahend and minuend), subtracts
	them, and pushes the result.
	
	Args:
        stack (Stack): The stack containing operands.
	"""

	if stack.size() < 2:
		print("not enough operands.")
		return
	
	subtrahend = stack.pop()
	minuend = stack.pop()
	difference = minuend - subtrahend
	stack.push(difference)

def idiv_operation(stack):
	"""
	Pops the top two items from the stack, performs integer division (floor),
	and pushes the result.
	
	Args:
        stack (Stack): The stack containing operands.
	"""

	if stack.size() < 2:
		print("not enough operands.")
		return

	divisor = stack.pop()
	dividend = stack.pop()

	if divisor == 0:
		print("integer division by zero error.")
		stack.push(dividend)
		stack.push(divisor)
		return

	quotient = dividend / divisor
	stack.push(math.floor(quotient))

def mul_operation(stack):
	"""
	Pops the top two items from the stack, multiplies them, and pushes the
	result.
	
	Args:
        stack (Stack): The stack containing operands.
	"""

	if stack.size() < 2:
		print("not enough operands.")
		return

	op1 = stack.pop()
	op2 = stack.pop()
	res = op1 * op2
	stack.push(res)

def mod_operation(stack):
	"""
	Pops the top two items from the stack, performs modulo operation, and
	pushes the result.
	
	Args:
        stack (Stack): The stack containing operands.
	"""

	if stack.size() < 2:
		print("not enough operands.")
		return

	divisor = stack.pop()
	dividend = stack.pop()

	if divisor == 0:
		print("modulo by zero error.")
		stack.push(dividend)
		stack.push(divisor)
		return

	remainder = dividend % divisor
	stack.push(remainder)

def abs_operation(stack):
	"""
	Pops the top item from the stack, computes its absolute value, and pushes
	the result.
	
	Args:
        stack (Stack): The stack containing operands.
	"""

	if stack.size() < 1:
		print("not enough operands.")
		return

	op = stack.pop()
	res = abs(op)
	stack.push(res)

def neg_operation(stack):
	"""
	Pops the top item from the stack, negates it, and pushes the result.
	
	Args:
        stack (Stack): The stack containing operands.
	"""

	if stack.size() < 1:
		print("not enough operands.")
		return
	
	op = stack.pop()
	res = -op
	stack.push(res)

def ceiling_operation(stack):
	"""
	Pops the top item from the stack, computes its ceiling, and pushes the
	result.
	
	Args:
        stack (Stack): The stack containing operands.
	"""

	if stack.size() < 1:
		print("not enough operands.")
		return

	op = stack.pop()
	res = math.ceil(op)
	stack.push(res)

def floor_operation(stack):
	"""
	Pops the top item from the stack, computes its floor, and pushes the
	result.
	
	Args:
        stack (Stack): The stack containing operands.
	"""

	if stack.size() < 1:
		print("not enough operands.")
		return

	op = stack.pop()
	res = math.floor(op)
	stack.push(res)

def round_operation(stack):
	"""
	Pops the top item from the stack, rounds it to the nearest integer, and
	pushes the result.
	
	Args:
        stack (Stack): The stack containing operands.
	"""

	if stack.size() < 1:
		print("not enough operands.")
		return

	op = stack.pop()
	res = round(op)
	stack.push(res)

def sqrt_operation(stack):
	"""
	Pops the top item from the stack, computes its square root, and pushes the
	result.
	
	Args:
        stack (Stack): The stack containing operands.
	"""

	if stack.size() < 1:
		print("not enough operands.")
		return

	op = stack.pop()
	
	if op < 0:
		print("square root of negative number error.")
		stack.push(op)
		return

	res = math.sqrt(op)
	stack.push(res)


operations = {
    "add": add_operation,
    "div": div_operation,
    "sub": sub_operation,
    "idiv": idiv_operation,
    "mul": mul_operation,
    "mod": mod_operation,
    "abs": abs_operation,
    "neg": neg_operation,
    "ceiling": ceiling_operation,
    "floor": floor_operation,
    "round": round_operation,
    "sqrt": sqrt_operation,
}