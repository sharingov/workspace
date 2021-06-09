def arithmetic_operation(operation):
    def op(a, b):
        return eval(str(a) + operation + str(b))

    return op
