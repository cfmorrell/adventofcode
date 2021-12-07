import re 
def peek(stack):
    return stack[-1] if stack else None

def apply_operator(operators, values):
    operator = operators.pop()
    right = values.pop()
    left = values.pop()
    values.append(eval("{0}{1}{2}".format(left, operator, right)))
  
def greater_precedence(op1, op2):
    precedences = {'+' : 1, '-' : 1, '*' : 0, '/' : 0}
    return precedences[op1] > precedences[op2]

def evaluate(expression):
    tokens = re.findall("[+/*()-]|\d+", expression)
    values = []
    operators = []
    for token in tokens:
        if token.isdigit():
            values.append(int(token))
        elif token == '(':
            operators.append(token)
        elif token == ')':
            top = peek(operators)
            while top is not None and top != '(':
                apply_operator(operators, values)
                top = peek(operators)
            operators.pop() # Discard the '('
        else:
            # Operator
            top = peek(operators)
            while top is not None and top not in "()" and greater_precedence(top, token):
                apply_operator(operators, values)
                top = peek(operators)
            operators.append(token)
    while peek(operators) is not None:
        apply_operator(operators, values) 
    return values[0]


def part1(filename):
    with open(filename) as f:
        problems = f.readlines()
    total = 0
    for problem in problems:
        total += evaluate(problem)
        # print(problem,evaluate(problem))
    print(total)

# part1('smallinput.txt')
part1('input.txt')







        