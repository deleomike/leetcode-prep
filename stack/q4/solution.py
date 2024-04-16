class Solution:
    def divide(self, a, b):
        val = a/b

        return floor(val) if val > 0 else ceil(val)
    def subtract(self, a, b):
        return a-b
    def multiply(self, a, b):
        return a*b
    def add(self, a, b):
        return a+b

    def solution(self, tokens: List[str]) -> int:
        stack = []
        operators = {
            "+": self.add,
            "-": self.subtract,
            "*": self.multiply,
            "/": self.divide
        }
        for token in tokens:
            if token in operators:
                b = stack.pop()
                a = stack.pop()
                c = operators[token](a,b)

                stack.append(c)

            else:
                stack.append(int(token))

        return stack[0]

    def evalRPN(self, tokens: List[str]) -> int:
        return self.solution(tokens)
        