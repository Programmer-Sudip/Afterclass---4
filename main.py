class ExpressionEvaluator:
    def __init__(self, expression):
        self.expression = expression

    def evaluate(self):
        try:
            result = self._evaluate_expression(self.expression)
            return result
        except Exception as e:
            return str(e)

    def _evaluate_expression(self, expression):
        # This method uses Python's eval function safely by restricting the available functions and variables.
        allowed_names = {
            'abs': abs,
            'round': round,
            'pow': pow,
            'sqrt': lambda x: x ** 0.5,
            'exp': lambda x: x ** 2.71828,  # Approximation of e
            'pi': 3.14159,
            'e': 2.71828
        }

        code = compile(expression, "<string>", "eval")

        for name in code.co_names:
            if name not in allowed_names:
                raise NameError(f"Use of '{name}' not allowed")

        return eval(code, {"__builtins__": {}}, allowed_names)

class ExpressionPrinter:
    @staticmethod
    def print_result(result):
        print(f"The result of the expression is: {result}")

if __name__ == "__main__":
    expression = input("Enter a mathematical expression to evaluate: ")
    evaluator = ExpressionEvaluator(expression)
    result = evaluator.evaluate()
    ExpressionPrinter.print_result(result)
