import sys
import tokenize
from tokenize_and_compute import current, next

# construct an AST (Abstract Syntax Tree) of a given expression
# get the final value by postorder traversal of the AST -- by function visit()
# print the code of expression
class AddNode():
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def visit(self):
        lval = self.left.visit()
        rval = self.right.visit()
        self.value = lval + rval
        print("BINARY_ADD")
        return self.value


class MulNode():
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def visit(self):
        lval = self.left.visit()
        rval = self.right.visit()
        self.value = lval * rval
        print("BINARY_MULTIPLY")
        return self.value


class SubNode():
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def visit(self):
        lval = self.left.visit()
        rval = self.right.visit()
        self.value = lval - rval
        print("BINARYT_SUBTRACT")
        return self.value


class DivNode():
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def visit(self):
        lval = self.left.visit()
        rval = self.right.visit()
        self.value = lval / rval
        print("BINARY_DIVIDE")
        return self.value

class ConstNode():
    def __init__(self, val):
        self.value = val
    
    def visit(self):
        print("LOAD_CONST %d" % self.value)
        return self.value

global current_token


def expr(tk):
    s1 = term(tk)
    token_num, token_value = current().token_num, current().token_value

    value = s1

    while token_value == "+" or token_value == "-":
        next(tk)

        s2 = term(tk)
        if token_value == "+":
            value = AddNode(value, s2)
        else:
            value = SubNode(value, s2)
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
            value = MulNode(value, s2)
        else:
            value = DivNode(value, s2)
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
        print("FINAL VALUE %d" % expr(tk).visit())