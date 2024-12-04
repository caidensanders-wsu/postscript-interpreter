#
# Copyright (c) Caiden Sanders and affiliates
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
#

import re

def tokenize(s):
    pattern = r"""
        ==                      # Matches '=='
        | \(.*?\)               # Match parentheses and their content
        | /?[a-zA-Z()][a-zA-Z0-9_()]*  # Match identifiers and keywords
        | [-]?[0-9]*\.?[0-9]+   # Match integers or floats (e.g., 42, -42, 3.14, -3.14)
        | [}{]+                 # Match braces
        | %.*                   # Match comments
        | [^ \t\n]              # Match single non-whitespace characters
    """

    return re.findall(pattern, s, re.VERBOSE)