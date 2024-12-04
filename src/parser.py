#
# Copyright (c) Caiden Sanders and affiliates
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
#

def parse(tokens):
    """
    Parses a list of tokens into a nested structure of code blocks.

    Args:
        tokens (list): List of tokens to be parsed.

    Returns:
        list: Parsed tokens, including nested code blocks.
    """

    return group(iter(tokens))

def group(iterator):
    """
    Groups tokens into code blocks recursively.

    Args:
        iterator (iterator): Iterator over the tokens.

    Returns:
        list: Grouped tokens with code blocks represented as nested lists.
    """

    result = []

    for token in iterator:
        if token == '}':
            return result
        elif token == '{':
            # Start a new code block
            result.append(group(iterator))
        else:
            result.append(token)

    return result