"""中缀转后缀

(3 + 4) * 5 - 6 中缀表达式
- * + 3 4 5 6   前缀表达式
3 4 + 5 * 6 -   后缀表达式
"""
opr_value = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
}
def cmp_opr(opr1, opr2):
    return opr_value[opr1] - opr_value[opr2]

def to_post(text):
    opr = []
    factor = []
    for char in text:
        if char in " \t\n":
            continue
        if char == "(":
            opr.append("(")
        elif char == ")":
            while True:
                c = opr.pop()
                if c != "(":
                    factor.append(c)
                else:
                    break
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
    return " ".join(factor)


def to_prefix(text):
    stack = []
    result = []
    for char in text:
        if char in " \t\n":
            continue
        if char == "(":
            stack.append(char)
        elif char == ")":
            result.append(stack.pop())


if __name__ == "__main__":
    print(to_post("3+4*5"))


