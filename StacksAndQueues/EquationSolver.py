from StacksAndQueues import Queue
from StacksAndQueues import Stack


class EquationSolver:
    def solve(self, equation):
        postfix_queue = self.parse_infix_to_postfix(equation)
        result = self.evaluate_postfix(postfix_queue)
        return result

    @staticmethod
    def precedence_of(op):
        if op == '*' or op == '/':
            precedence = 1
        else:
            precedence = 0
        return precedence

    def parse_infix_to_postfix(self, equation):
        postfix = Queue.Queue(50)
        opStack = Stack.Stack(50)
        infix = equation.split()

        for e in infix:
            if e == '(':
                opStack.push('(')
            elif e == ')':
                while opStack.top != '(':
                    postfix.enqueue(opStack.pop())
                opStack.pop()
            elif e == '+' or e == '-' or e == '*' or e == '/':
                while not opStack.is_empty() and opStack.top() != '(' and self.precedence_of(opStack.top()) >= self.precedence_of(e):
                    postfix.enqueue(opStack.pop())
                opStack.push(e)
            else:
                postfix.enqueue(float(e))

        while not opStack.is_empty():
            postfix.enqueue(opStack.pop())
        return postfix

    @staticmethod
    def execute_operation(op, v1, v2):
        result = 0
        if op == '+':
            result = v2 + v1
        elif op == '-':
            result = v2 - v1
        elif op == '*':
            result = v2 * v1
        elif op == '/':
            result = v2 / v1
        return result

    def evaluate_postfix(self, postfix_queue):
        operandStack = Stack.Stack(100)
        count = postfix_queue.get_count()
        for i in range(count):
            term = postfix_queue.dequeue()
            if isinstance(term, float):
                operandStack.push(term)
            elif isinstance(term, str):
                op = term[0]
                v1 = operandStack.pop()
                v2 = operandStack.pop()
                result = self.execute_operation(op, v1, v2)
                operandStack.push(result)
        result = operandStack.pop()
        return result
