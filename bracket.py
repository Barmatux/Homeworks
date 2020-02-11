from collections import deque, OrderedDict
import operator

operators = OrderedDict()
operators['*'] = operator.mul
operators['/'] = operator.truediv
operators['+'] = operator.add
operators['-'] = operator.sub

def find_close_bracket(deque_of_token: deque):
    deq = deque_of_token
    item = deq.popleft()
    while item != ')':
        if item == '(':
            item = deq.popleft()
            find_close_bracket(deq)
        else:
            item = deq.popleft()
    return deq


def count(deque_of_token: list):
    for i in operators:
        if i in deque_of_token:
            op_slice = slice(deque_of_token.index(i)-1, deque_of_token.index(i)+2)
            operand = deque_of_token[op_slice]
            deque_of_token[op_slice]= [operators[i](operand[0], operand[2])]
    return deque_of_token







if __name__ == '__main__':
    a = count([4, '+', 5, '-', 3, '*', 2])
    print(a)