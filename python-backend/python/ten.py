def is_polynomial_equal(x, k, expression):
    return eval(expression) == k

# Input
x, k = map(int, raw_input().split())
polynomial_expression = raw_input().strip()

# Output
result = is_polynomial_equal(x, k, polynomial_expression)
print(result)
