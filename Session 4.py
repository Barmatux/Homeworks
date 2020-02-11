import operator

ops = {'+': operator.add, '-': operator.sub, '*': operator.mul,'/': operator.truediv}


class Stack:
    def __init__(self):
        self.mylist = []

    def isempty(self):
        return True if len(self.mylist) == 0 \
            else False

    def top(self):
        if self.isempty():
            print("Stack is Empty")
            return 0
        else:
            return self.mylist[-1]

    def push(self,item):
        print("Pushing : %s" %item)
        self.mylist.append(item)

    def pop(self):
        if not self.isempty():
            print("popping: %s" %self.top())
            return self.mylist.pop()
        else:
            print("Stack is Empty")
        return None


def do_infix_evaluation(items):
    print ("****Evaluating the preceding items****",items)
    items = list(map(lambda x: x if not isinstance(x,str) else int(x),items))
    print (items)
    firstitem = items.pop()
    prevresult = firstitem
    while firstitem:
        try:
            if hasattr(firstitem,'__call__'):
                prevresult = firstitem(prevresult,items.pop())

            firstitem = items.pop()
        except IndexError:
            return prevresult



    print ("****** Evaluated Result is : %s" %prevresult)
    return prevresult


def pop_until_openbrace(stack):
    tlist = []
    item = stack.pop()
    eres = 0
    while item != '(':
        if item:
            tlist.append(item)
            item = stack.pop()
        else:
            print("Insufficient items in stack")
            return None

    return do_infix_evaluation(tlist) if tlist else eres


def infix(expression):
    print(expression)
    stack = Stack()
    for i in list(expression):
        if i == ')':
            stack.push(pop_until_openbrace(stack))
        elif i in ops:
            stack.push(ops[i])
        else:
            stack.push(i)
    print ("Result is :", stack.mylist)
    return stack


if __name__ == '__main__':

    print ("Enter expre:")
    expr = input()
    a = infix(expr)
