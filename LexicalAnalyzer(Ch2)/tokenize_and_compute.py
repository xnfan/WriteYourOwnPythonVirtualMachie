import sys
import tokenize

# tk = tokenize.generate_tokens(f.readlin())
# for token_num, token_value, _, _, _ in tk:   example that how to use tokenize

# up-down
# expression = term + term + ... + term
# term = factor * factor * ... * factor
# factor = num | (expression)
# recursive

class Token:
    def __init__(self, token_num, token_value):
        self.token_num = token_num
        self.token_value = token_value

global current_token

def current():
    global current_token
    return current_token

def next(tk):
    token_num, token_value, _, _, _ = tk.__next__()
    global current_token
    current_token = Token(token_num, token_value)

def expr(tk):
    s1 = term(tk)
    token_num, token_value = current().token_num, current().token_value

    value = s1

    while token_value == "+" or token_value == "-":
        print("expr token is %s" % token_value)
        next(tk)

        s2 = term(tk)
        if token_value == "+":
            value += s2
        else:
            value -= s2
        token_num, token_value = current().token_num, current().token_value
    
    print("expr value is %s" % value)
    return value

def term(tk):
    f1 = factor(tk)
    token_num, token_value = current().token_num, current().token_value

    value = f1

    while token_value == "*" or token_value == "/":
        print("term token is %s" % token_value)
        next(tk)

        f2 = term(tk)
        if token_value == '*':
            value *= f2
        else:
            value /= f2
        token_num, token_value = current().token_num, current().token_value
    
    print("term value is %s" % value)
    return value

def factor(tk):
    if current_token.token_num == tokenize.NUMBER:
        value = current_token.token_value
        next(tk)
    elif current_token.token_value == "(":
        next(tk)
        f = expr(tk)
        if current_token.token_value != ")":
            print("parse error! value=%s" % current().token_value)
        value = f
        next(tk)
    return int(value)


if __name__ == '__main__':
    with open(sys.argv[1], "r") as f:
        tk = tokenize.generate_tokens(f.readline)
        next(tk)
        print(expr(tk))