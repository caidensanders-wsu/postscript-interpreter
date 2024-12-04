#
# Copyright (c) Caiden Sanders and affiliates
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
#

class LimitedDict:
	"""
	A dictionary with a maximum capacity.
	Allows setting and retrieving items up to the defined max length.
	"""

	def __init__(self, max_length):
		"""
		Initializes the LimitedDict with a maximum length.
		"""

		if not isinstance(max_length, int) or max_length <= 0:
			raise ValueError("max_length must be a positive integer.")
		self.max_length = max_length
		self.dict = {}

	def set_max_length(self, max_length):
		"""
		Sets a new maximum length for the dictionary.
		"""

		if not isinstance(max_length, int) or max_length <= 0:
			raise ValueError("max_length must be a positive integer.")
		self.max_length = max_length

	def get_max_length(self):
		"""
		Returns the maximum length of the dictionary.
		"""

		return self.max_length

	def __setitem__(self, key, value):
		"""
		Adds a key-value pair to the dictionary.
		Raises a ValueError if the dictionary is full.
		"""

		if len(self.dict) < self.max_length:
			self.dict[key] = value
		else:
			raise ValueError("Dictionary is full.")

	def __getitem__(self, key):
		"""
		Retrieves the value associated with a key.
		Raises a KeyError if the key is not found.
		"""

		return self.dict[key]

	def __iter__(self):
		"""
		Returns an iterator over the dictionary keys.
		"""

		return iter(self.dict)
	
	def __len__(self):
		"""
		Returns the current number of items in the dictionary.
		"""
		
		return len(self.dict)
