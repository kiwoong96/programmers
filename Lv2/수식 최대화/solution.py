def calc(prior, n, expression):
    if n == 2:
        return str(eval(expression))

    if prior[n] == '*':
        res = eval('*'.join([calc(prior, n + 1, e) for e in expression.split('*')]))
    if prior[n] == '+':
        res = eval('+'.join([calc(prior, n + 1, e) for e in expression.split('+')]))
    if prior[n] == '-':
        res = eval('-'.join([calc(prior, n + 1, e) for e in expression.split('-')]))
    return str(res)


def solution(expression):
    answer = 0
    list_data = []
    prior = [['*', '-', '+'],
             ['*', '+', '-'],
             ['+', '*', '-'],
             ['+', '-', '*'],
             ['-', '*', '+'],
             ['-', '+', '*']]

    for priority in prior:
        answer = max(answer, abs(int(calc(priority, 0, expression))))
    return answer