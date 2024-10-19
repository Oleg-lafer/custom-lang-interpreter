# Eliron Barel: 209237478
# Daniel Dahan: 318840196
# Or Avital: 207779802
# Oleg Muraviov:321163446
from Interpreter import Interpreter, run

# Initialize the interpreter
interpreter = Interpreter()


# Helper function to run expressions and print results
def test_expression(expression):
    print(f"Expression: {expression}")
    result, error = run(expression, interpreter)
    if error:
        print(f"Error: {error}")
    else:
        print(f"Result: {result}")
    print()


# 1. Basic arithmetic operations
test_expression("2 + 3 * 4")
test_expression("10 / 2 - 3")
test_expression("2 ** 3 + 1")
test_expression("17 % 5")

# 2. Variable assignment and access
test_expression("x = 10")
test_expression("y = 5")
test_expression("x + y")

# 3. Comparison operators
test_expression("x > y")
test_expression("x == 2 * y")
test_expression("x < y")

# 4. If-else statements
test_expression("IF x % 2 == 0 THEN 0 ELSE 1")
test_expression("IF x > y THEN 100 ELSE 0")

# 5. While loops
test_expression("counter = 0")
test_expression("WHILE counter < 5 THEN (counter = counter + 1)")
test_expression("counter")

# 6. Complex expressions
test_expression("result = 0")
test_expression("WHILE result < 100 THEN (result = result + (result + 1))")
test_expression("result")

# 7. Error cases
test_expression("10 / 0")  # Division by zero
test_expression("undefinedVariable")  # Undefined variable
test_expression("1 + ")  # Incomplete expression

