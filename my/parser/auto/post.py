"""中缀转后缀

(3 + 4) * 5 - 6 中缀表达式 infix expression
- * + 3 4 5 6   前缀表达式 prefix
3 4 + 5 * 6 -   后缀表达式 postfix
"""


bracket = None

opr_value = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
}
def cmp_opr(opr1, opr2):
    return opr_value[opr1] - opr_value[opr2]

def infix_to_postfix(text):
    opr = []
    factor = []
    for char in text:
        # 跳过空白符
        if char in " \t\n":
            continue
        # 括号处理
        if char == "(":
            opr.append("(")
        elif char == ")":
            while True:
                c = opr.pop()
                if c == "(":
                    break
                factor.append(c)
        elif char in "+-*/":
            while True:
                if not opr or opr[-1] == "(" or cmp_opr(char, opr[-1]) > 0:
                    opr.append(char)
                    break
                else:
                    factor.append(opr.pop())
        else:
            factor.append(char)
    # print(opr, factor)
    if opr:
        opr.reverse()
        factor.extend(opr)
    return "".join(factor)


def infix_to_prefix(text):
    opr = []
    factor = []
    for char in text[::-1]:
        if char in " \t\n":
            continue
        if char == ")":
            opr.append(char)
        elif char == "(":
            while True:
                c = opr.pop()
                if c == "(":
                    break
                factor.append(c)
        elif char in "+-*/":
            while True:
                if not opr or opr[-1] == ")" or cmp_opr(char, opr[-1]) >= 0:
                    opr.append(char)
                    break
                else:
                    factor.append(opr.pop())
        else:
            factor.append(char)
    if opr:
        opr.reverse()
        factor.extend(opr)
    factor.reverse()
    return "".join(factor)



if __name__ == "__main__":
    infix = "3+4*5"
    prefix = infix_to_prefix(infix)
    postfix = infix_to_postfix(infix)
    print(prefix)
    print(postfix)
    assert prefix == "+3*45"
    assert postfix == "345*+"



