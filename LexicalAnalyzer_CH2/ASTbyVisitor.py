import sys, tokenize
from tokenize_and_compute import current, next

# like AST.py by using the Visitor Pattern
class ConstNode():
    def __init__(self, value):
        self.value = value

    def accept(self, visitor):
        return visitor.visitConst(self)
class BinaryOpNode():
    ADD = 0
    SUB = 1
    MUL = 2
    DIV = 3
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

    def accept(self, visitor):
        return visitor.visitBinaryOP(self)


class Visitor():
    def visit(self, node):
        return node.accept(self)

    def visitConst(self, constNode):
        print("LOAD_CONST: %d" % constNode.value)
        return constNode.value
    
    def visitBinaryOP(self, binaryOpNode):
        left = binaryOpNode.left.accept(self)
        right = binaryOpNode.right.accept(self)


        if binaryOpNode.op == BinaryOpNode.ADD:
            print("BINARY_ADD")
            return left + right
        elif binaryOpNode.op == BinaryOpNode.SUB:
            print("BINARY_SUBTRACT")
            return left - right
        elif binaryOpNode.op == BinaryOpNode.MUL:
            print("BINARY_MULTIPLY")
            return left * right
        elif binaryOpNode.op == BinaryOpNode.DIV:
            print("BINARY_DIVIDE")
            return left / right


global current_token

def expr(tk):
    s1 = term(tk)
    token_num, token_value = current().token_num, current().token_value

    value = s1

    while token_value == "+" or token_value == "-":
        next(tk)

        s2 = term(tk)
        if token_value == "+":
            value = BinaryOpNode(0, value, s2)
        else:
            value = BinaryOpNode(1, value, s2)
        token_num, token_value = current().token_num, current().token_value
    
    return value


def term(tk):
    s1 = factor(tk)
    token_num, token_value = current().token_num, current().token_value

    value = s1

    while token_value == "*" or token_value == "/":
        next(tk)

        s2 = term(tk)
        if token_value == "*":
            value = BinaryOpNode(2, value, s2)
        else:
            value = BinaryOpNode(3, value, s2)
        token_num, token_value = current().token_num, current().token_value
    
    return value


def factor(tk):
    if current().token_num == tokenize.NUMBER:
        value = current().token_value
        next(tk)
        return ConstNode(int(value))
    elif current().token_value == "(":
        next(tk)
        f = expr(tk)
        if current().token_value != ")":
            print("parse error! value = %s" % current().token_value)
        value = f
        next(tk)
        return value


if __name__ == '__main__':
    with open(sys.argv[1], "r") as f:
        tk = tokenize.generate_tokens(f.readline)
        next(tk)
        vs = Visitor()
        AST = expr(tk)
        print("FINAL VALUE %d" % vs.visit(AST))
        

                

    