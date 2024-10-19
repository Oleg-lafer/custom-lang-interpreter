
---

# Simple Interpreter

## Overview
This project implements a simple interpreter for a custom programming language. The interpreter supports:
- Variable assignment
- Basic arithmetic operations (`+`, `-`, `*`, `/`, `%`, `**`)
- Comparison operators (`>`, `<`, `==`)
- Logical operators (`AND`, `OR`, `NOT`)
- Conditional statements (`if-else`)
- Loops (`while`)

The interpreter consists of a **Lexer** for tokenization, a **Parser** that builds an Abstract Syntax Tree (AST), and an **Interpreter** that evaluates the AST.

## Features
- **Arithmetic Expressions**: You can use basic math operations like addition, subtraction, multiplication, division, and more.
- **Conditional Statements**: The interpreter supports if-else conditions.
- **Loops**: Use `while` loops for repeated execution of code blocks.
- **Variables**: Assign values to variables and use them in expressions.

## Example Usage
```bash
> x = 5
> y = x + 3
> if x < y then 10 else 20
Result: 10
```

## File Structure
- `interpreter.py`: The core interpreter containing the lexer, parser, and interpreter logic.
- `tests.py`: A test suite for verifying the correctness of the interpreter with predefined cases.

## Getting Started

### Prerequisites
Make sure you have Python installed (version 3.6 or later). You can check this by running:
```bash
python --version
```

### Installation
1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/your-repo/simple-interpreter.git
    ```
2. Navigate to the project directory:
    ```bash
    cd simple-interpreter
    ```

### Running the Interpreter
You can run the interpreter interactively by executing the `interpreter.py` file:
```bash
python interpreter.py
```
This will open a simple command-line interface where you can type in expressions to evaluate them. Type `exit` to quit.

Example session:
```bash
calc > x = 5
calc > y = x + 3
calc > if x < y then 10 else 20
Result: 10
calc > exit
Goodbye!
```

### Running Tests
To ensure everything is working correctly, you can run the tests by executing:
```bash
python tests.py
```

### Usage and Examples
#### Variable Assignment
You can assign values to variables:
```bash
> x = 10
> y = 20
```

#### Arithmetic Operations
The interpreter supports basic arithmetic:
```bash
> z = x + y * 2
Result: 50
```

#### If-Else Statements
You can use `if-else` for conditional logic:
```bash
> if x < y then 100 else 200
Result: 100
```

#### Loops
The `while` loop can be used for repeated execution:
```bash
> x = 1
> while x < 5 then x = x + 1
```

## Code Structure

### Lexer
The lexer splits the input text into tokens that represent the smallest meaningful elements, such as numbers, operators, and keywords.

### Parser
The parser takes tokens from the lexer and builds an **Abstract Syntax Tree (AST)**, which represents the structure of the program.

### Interpreter
The interpreter traverses the AST and evaluates the expressions based on the rules of the language.

## Contributing
Feel free to contribute to this project by submitting pull requests or opening issues for bugs and feature requests.

### License
This project is licensed under the MIT License.

---

This README should give a clear overview of how the interpreter works, guide the user on how to set up and run it, and provide example usage for testing and interacting with the interpreter.
