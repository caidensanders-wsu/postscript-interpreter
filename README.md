# PostScript Interpreter

A **limited instruction set PostScript interpreter** written in Python, featuring an optional feature to switch between dynamic scoping and static (lexical) scoping. It supports a subset of PostScript commands, including stack manipulation, arithmetic operations, dictionary handling, string operations, boolean logic, flow control, and basic input/output functionalities

## Instruction Subset

- **Stack Manipulation**: `dup`, `pop`, `exch`, `copy`, `clear`, `count`, `get`, `getinterval`, `putinterval`
- **Arithmetic Operations**: `add`, `sub`, `mul`, `div`, `idiv`, `mod`, `abs`, `neg`, `sqrt`
- **Comparison Operations**: `eq`, `ne`, `gt`, `ge`, `lt`, `le`
- **Boolean Operations**: `and`, `or`, `not`
- **Control Flow**: `if`, `ifelse`, `for`, `repeat`, `quit`
- **Dictionary Handling**: `dict`, `maxlength`, `begin`, `end`, `def`
- **String Operations**: `length`, `get`, `getinterval`, `putinterval`
- **Input and Output**: `print`, `=`, `==`, `pstack`

## Installation

### Prerequisites

- **Python**: Make sure that you have Python installed. You can download it online from [python.org](https://www.python.org/downloads/).

### Clone the Repository

```bash
git clone https://github.com/caidensanders-wsu/postscript-interpreter.git
cd postscript-interpreter
```

### Dependencies

This interpreter doesn't rely on any dependencies and therefore it can be ran straight out of the box!

## Usage

This interpreter provides a REPL where you can input PostScript commands.

### Running the Interpreter

```bash
python src/main.py
```

## REPL Commands

- **Constants**: Type in any constant and press Enter to add it to the stack.
- **Execute PostScript Commands**: Type any supported PostScript commands and press Enter to execute.
- **Quit the Interpreter**: Type `quit` to exit the REPL.

## Scoping Behavior

The interpreter supports both **static** and **dynamic** scoping, allowing you to control the name resolution of the interpreter.

### Default Scoping

- **Dynamic Scoping**: By default, the interpreter uses dynamic scoping. This means that the name resolution starts from the most recent dictionary on the stack and moves downwards.

### Enable Static Scoping

To enable static scoping, modify the `use_static_scoping` variable in the `globals.py` file.

```python
# globals.py

use_static_scoping = True # Set to true for static scoping
```