from collections import deque, OrderedDict
import operator

operators = OrderedDict()
operators['*'] = operator.mul
operators['/'] = operator.truediv
operators['+'] = operator.add
operators['-'] = operator.sub

def evaluate_in_bracket(deque_of_token: list):
    for i in deque_of_token:
        if i == '(':
            slc_deq = deque_of_token[deque_of_token.index(i)+1:]
            a = find_close_bracket(slc_deq)
            # index = a + len(deque_of_token[:deque_of_token.index(i)+1])
            slice_deq = slice(deque_of_token.index(i)+1, index)
            b = count_operators(deque_of_token[slice_deq])
            deque_of_token[deque_of_token.index(i): index+1] = b
            return count_operators(deque_of_token)
    return None


def find_close_bracket(slice_deque: list):
    for i in slice_deque:
        if i == ')':
            return slice_deque.index(i)
        elif i == '(':
             evaluate_in_bracket(slice_deque[slice_deque.index(i)+1:])
    return None



def count_operators(deque_of_token: list):
    for i in operators:
        if i in deque_of_token:
            op_slice = slice(deque_of_token.index(i)-1, deque_of_token.index(i)+2)
            operand = deque_of_token[op_slice]
            deque_of_token[op_slice]= [operators[i](operand[0], operand[2])]
    return deque_of_token







if __name__ == '__main__':
    a = evaluate_in_bracket([4, '+', '(', 5, '-', 3,')', '*', '(', 2, '-', 1, ')'])
    print(a)
