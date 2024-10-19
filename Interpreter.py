# Eliron Barel: 209237478
# Daniel Dahan: 318840196
# Or Avital: 207779802
# Oleg Muraviov:321163446
"""
Simple Interpreter

This module implements a basic interpreter for a custom programming language.
It includes a lexer for tokenization, a parser for creating an Abstract Syntax Tree (AST),
and an interpreter for executing the AST.

Supported Features:
- Variable assignment
- Basic arithmetic operations (+, -, *, /, %, **)
- Comparison operators (>, <, ==)
- Logical operators (AND, OR, NOT)
- If-else statements
- While loops

Usage:
- To test the interpreter, run the tests.py file.
- To interact with the interpreter, run this file directly and input expressions.

Example:
> x = 5
> y = x + 3
> if x < y then 10 else 20

The above code will assign 5 to x, 8 to y, and evaluate the if-else expression to 10.

"""

# Constants for digit and letter characters
DIGITS = '0123456789'
LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Token types
TT_INT = 'INT'           # Integer numbers
TT_FLOAT = 'FLOAT'       # Floating-point numbers
TT_IDENTIFIER = 'IDENTIFIER'  # Variable names
TT_KEYWORD = 'KEYWORD'   # Reserved keywords (e.g., IF, ELSE)
TT_PLUS = 'PLUS'         # Addition operator '+'
TT_MINUS = 'MINUS'       # Subtraction operator '-'
TT_MUL = 'MUL'           # Multiplication operator '*'
TT_DIV = 'DIV'           # Division operator '/'
TT_MOD = 'MOD'           # Modulus operator '%'
TT_POW = 'POW'           # Exponentiation operator '**'
TT_LPAREN = 'LPAREN'     # Left parenthesis '('
TT_RPAREN = 'RPAREN'     # Right parenthesis ')'
TT_EQ = 'EQ'             # Assignment operator '='
TT_EE = 'EE'             # Equality operator '=='
TT_GT = 'GT'             # Greater-than operator '>'
TT_LT = 'LT'             # Less-than operator '<'
TT_AND = 'AND'           # Logical AND operator 'AND'
TT_OR = 'OR'             # Logical OR operator 'OR'
TT_NOT = 'NOT'           # Logical NOT operator 'NOT'
TT_EOF = 'EOF'           # End of file/input marker

# List of reserved keywords
KEYWORDS = ['IF', 'ELSE', 'WHILE', 'THEN', 'AND', 'OR', 'NOT']



class Token:
    """
      A token represents the smallest unit in the source code, such as a number,
      operator, or keyword. Each token has a type and may have a value.
      """
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'

    def matches(self, type_, value):
        """Check if the token matches a given type and value."""
        return self.type == type_ and self.value == value


class Lexer:
    """
       The lexer is responsible for converting the input string into a list of tokens.
       It scans through the input character by character and creates tokens based on
       predefined rules for numbers, operators, keywords, etc.
       """
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.current_char = None
        self.advance()

    def advance(self):
        """Advance to the next character in the input string."""
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def make_tokens(self):
        """Convert the entire input string into a list of tokens."""
        tokens = []

        while self.current_char is not None:
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char in DIGITS:
                tokens.append(self.make_number())
            elif self.current_char in LETTERS:
                tokens.append(self.make_identifier())
            elif self.current_char == '+':
                tokens.append(Token(TT_PLUS))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token(TT_MINUS))
                self.advance()
            elif self.current_char == '*':
                if self.pos + 1 < len(self.text) and self.text[self.pos + 1] == '*':
                    tokens.append(Token(TT_POW))
                    self.advance()
                    self.advance()
                else:
                    tokens.append(Token(TT_MUL))
                    self.advance()
            elif self.current_char == '/':
                tokens.append(Token(TT_DIV))
                self.advance()
            elif self.current_char == '%':
                tokens.append(Token(TT_MOD))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Token(TT_LPAREN))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(TT_RPAREN))
                self.advance()
            elif self.current_char == '=':
                if self.pos + 1 < len(self.text) and self.text[self.pos + 1] == '=':
                    tokens.append(Token(TT_EE))
                    self.advance()
                    self.advance()
                else:
                    tokens.append(Token(TT_EQ))
                    self.advance()
            elif self.current_char == '>':
                tokens.append(Token(TT_GT))
                self.advance()
            elif self.current_char == '<':
                tokens.append(Token(TT_LT))
                self.advance()
            elif self.current_char == 'O':
                if self.pos + 1 < len(self.text) and self.text[self.pos + 1] == 'R':
                    tokens.append(Token(TT_OR))
                    self.advance()
                    self.advance()
                else:
                    return [], f"Illegal character '{self.current_char}'"
            elif self.current_char == 'A':
                if self.pos + 2 < len(self.text) and self.text[self.pos + 2] == 'N' and self.text[self.pos + 3] == 'D':
                    tokens.append(Token(TT_AND))
                    self.advance()
                    self.advance()
                    self.advance()
                    self.advance()
                else:
                    return [], f"Illegal character '{self.current_char}'"
            elif self.current_char == 'N':
                if self.pos + 2 < len(self.text) and self.text[self.pos + 2] == 'O' and self.text[self.pos + 3] == 'T':
                    tokens.append(Token(TT_NOT))
                    self.advance()
                    self.advance()
                    self.advance()
                    self.advance()
                else:
                    return [], f"Illegal character '{self.current_char}'"
            else:
                return [], f"Illegal character '{self.current_char}'"

        tokens.append(Token(TT_EOF))
        return tokens, None

    def make_number(self):
        """ Create a number token, which could be either an integer or a floating-point number. """
        num_str = ''
        dot_count = 0

        while self.current_char is not None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                if dot_count == 1:
                    break
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_char
            self.advance()

        if dot_count == 0:
            return Token(TT_INT, int(num_str))
        else:
            return Token(TT_FLOAT, float(num_str))

    def make_identifier(self):
        """ Create an identifier token, which could either be a variable name or a keyword. """
        id_str = ''

        while self.current_char is not None and self.current_char in LETTERS + DIGITS + '_':
            id_str += self.current_char
            self.advance()

        tok_type = TT_KEYWORD if id_str in KEYWORDS else TT_IDENTIFIER
        return Token(tok_type, id_str)


class NumberNode:
    """ Represents a number in the AST (either integer or float)."""
    def __init__(self, tok):
        self.tok = tok

    def __repr__(self):
        return f'{self.tok}'


class BinOpNode:
    """ Represents a binary operation (e.g., addition, multiplication) in the AST."""
    def __init__(self, left_node, op_tok, right_node):
        self.left_node = left_node
        self.op_tok = op_tok
        self.right_node = right_node

    def __repr__(self):
        return f'({self.left_node}, {self.op_tok}, {self.right_node})'


class UnaryOpNode:
    def __init__(self, op_tok, node):
        self.op_tok = op_tok
        self.node = node

    def __repr__(self):
        return f'({self.op_tok}, {self.node})'


class VarAssignNode:
    """Represents a variable assignment in the AST."""
    def __init__(self, var_name, value_node):
        self.var_name = var_name
        self.value_node = value_node

    def __repr__(self):
        return f'({self.var_name} = {self.value_node})'


class VarAccessNode:
    """Represents a variable access in the AST."""
    def __init__(self, var_name):
        self.var_name = var_name

    def __repr__(self):
        return f'({self.var_name})'


class IfNode:
    """ Represents an if-else statement in the AST."""
    def __init__(self, condition, body, else_body):
        self.condition = condition
        self.body = body
        self.else_body = else_body

    def __repr__(self):
        return f'(IF {self.condition} THEN {self.body} ELSE {self.else_body})'


class WhileNode:
    """ Represents an while loop statement in the AST."""
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

    def __repr__(self):
        return f'(WHILE {self.condition} DO {self.body})'


class Parser:
    """The parser takes a list of tokens from the lexer and builds an AST."""
    def __init__(self, tokens):
        self.tokens = tokens
        self.tok_idx = -1
        self.advance()

    def advance(self):
        """Move to the next token in the list."""
        self.tok_idx += 1
        if self.tok_idx < len(self.tokens):
            self.current_tok = self.tokens[self.tok_idx]
        return self.current_tok

    def parse(self):
        """Parse the tokens and return the root of the AST."""
        res = self.expr()
        if not res:
            return None, "Invalid Syntax"
        if self.current_tok.type != TT_EOF:
            return None, f"Expected end of expression, got {self.current_tok.type}"
        return res

    def expr(self):
        """ Parse an expression, which could be a binary operation or a variable assignment."""
        # Handle logical operators and arithmetic expressions
        return self.bin_op(self.comp_expr, [(TT_PLUS, TT_MINUS)])

    def comp_expr(self):
        # Handle comparison operators
        node = self.bin_op(self.arith_expr, [(TT_EE, TT_LT, TT_GT)])

        while self.current_tok.type in (TT_AND, TT_OR):
            op_tok = self.current_tok
            self.advance()
            node = BinOpNode(node, op_tok, self.comp_expr())

        return node

    def arith_expr(self):
        # Handle arithmetic operators
        return self.bin_op(self.term, [(TT_PLUS, TT_MINUS)])

    def term(self):
        # Handle multiplication and division operators
        return self.bin_op(self.factor, [(TT_MUL, TT_DIV, TT_MOD)])

    def factor(self):
        # Handle unary operators and power operations
        return self.power()

    def power(self):
        # Handle exponentiation operator
        return self.bin_op(self.atom, [(TT_POW,)], self.factor)

    def atom(self):
        tok = self.current_tok

        if tok.type in (TT_INT, TT_FLOAT):
            self.advance()
            return NumberNode(tok)
        elif tok.type == TT_IDENTIFIER:
            self.advance()
            if self.current_tok.type == TT_EQ:
                self.advance()
                expr = self.expr()
                return VarAssignNode(tok.value, expr)
            return VarAccessNode(tok.value)
        elif tok.type == TT_LPAREN:
            self.advance()
            expr = self.expr()
            if self.current_tok.type == TT_RPAREN:
                self.advance()
                return expr
            else:
                return None  # Unmatched parenthesis
        elif tok.type == TT_KEYWORD and tok.value in ['IF', 'WHILE']:
            self.advance()
            if tok.value == 'IF':
                return self.if_expr()
            elif tok.value == 'WHILE':
                return self.while_expr()

        return None

    def bin_op(self, func_a, ops, func_b=None):
        if func_b is None:
            func_b = func_a

        left = func_a()
        if not left:
            return None

        while self.current_tok.type in [op for op_pair in ops for op in op_pair]:
            op_tok = self.current_tok
            self.advance()
            right = func_b()
            if not right:
                return None
            left = BinOpNode(left, op_tok, right)

        return left

    def if_expr(self):
        condition = self.expr()
        if not condition:
            return None, "Invalid condition in IF statement"

        if not self.current_tok.matches(TT_KEYWORD, 'THEN'):
            return None, "Expected 'THEN' after IF condition"

        self.advance()  # Skip the 'THEN' token

        if_body = self.expr()
        if not if_body:
            return None, "Invalid body in IF statement"

        if self.current_tok.matches(TT_KEYWORD, 'ELSE'):
            self.advance()  # Skip the 'ELSE' token
            else_body = self.expr()
            if not else_body:
                return None, "Invalid body in ELSE statement"
        else:
            else_body = None

        return IfNode(condition, if_body, else_body)

    def while_expr(self):
        condition = self.expr()
        if not condition:
            return None, "Invalid condition in WHILE loop"

        if not self.current_tok.matches(TT_KEYWORD, 'THEN'):
            return None, "Expected 'THEN' after WHILE condition"

        self.advance()  # Skip the 'THEN' token

        body = self.expr()
        if not body:
            return None, "Invalid body in WHILE loop"

        return WhileNode(condition, body)


class Interpreter:
    """
        The interpreter walks through the AST and evaluates the expressions.
        It maintains a symbol table for variable assignments.
     """
    def __init__(self):
        self.variables = {}

    def visit(self, node):
        """Visit a node in the AST and perform the corresponding operation."""
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name, self.no_visit_method)
        return method(node)

    def no_visit_method(self, node):
        """Raise an exception if a visit method is not implemented."""
        raise Exception(f'No visit_{type(node).__name__} method defined')

    def visit_NumberNode(self, node):
        return node.tok.value

    def visit_BinOpNode(self, node):
        left = self.visit(node.left_node)
        right = self.visit(node.right_node)

        if node.op_tok.type == TT_PLUS:
            return left + right
        elif node.op_tok.type == TT_MINUS:
            return left - right
        elif node.op_tok.type == TT_MUL:
            return left * right
        elif node.op_tok.type == TT_DIV:
            if right == 0:
                raise Exception("Division by zero")
            return left / right
        elif node.op_tok.type == TT_MOD:
            if right == 0:
                raise Exception("Modulo by zero")
            return left % right
        elif node.op_tok.type == TT_POW:
            return left ** right
        elif node.op_tok.type == TT_EE:
            return left == right
        elif node.op_tok.type == TT_LT:
            return left < right
        elif node.op_tok.type == TT_GT:
            return left > right
        elif node.op_tok.type == TT_AND:
            return left and right
        elif node.op_tok.type == TT_OR:
            return left or right

    def visit_UnaryOpNode(self, node):
        value = self.visit(node.node)
        if node.op_tok.type == TT_MINUS:
            return -value
        elif node.op_tok.type == TT_NOT:
            return not value
        return value

    def visit_VarAssignNode(self, node):
        var_name = node.var_name
        value = self.visit(node.value_node)
        self.variables[var_name] = value
        return value

    def visit_VarAccessNode(self, node):
        var_name = node.var_name
        value = self.variables.get(var_name)
        if value is None:
            raise Exception(f"Variable '{var_name}' is not defined")
        return value

    def visit_IfNode(self, node):
        condition = self.visit(node.condition)
        if condition:
            return self.visit(node.body)
        elif node.else_body:
            return self.visit(node.else_body)

    def visit_WhileNode(self, node):
        while self.visit(node.condition):
            self.visit(node.body)
        return None


def run(text, interpreter):
    """
       The main function to run the interpreter.
       It first tokenizes the input, then parses the tokens into an AST, and finally
       interprets the AST.
       """
    lexer = Lexer(text)
    tokens, error = lexer.make_tokens()
    if error:
        return None, error

    parser = Parser(tokens)
    ast = parser.parse()
    if isinstance(ast, tuple):
        return None, ast[1]  # Return the error message

    try:
        result = interpreter.visit(ast)
        return result, None
    except Exception as e:
        return None, str(e)


if __name__ == "__main__":
    interpreter = Interpreter()
    print("Simple Interpreter - Type 'exit' to quit")


    while True:
        text = input('calc > ')
        if text.lower() == 'exit':
            break
        result, error = run(text, interpreter)
        if error:
            print("Error:", error)
        elif result is not None:
            print("Result:", result)
    print("Goodbye!")