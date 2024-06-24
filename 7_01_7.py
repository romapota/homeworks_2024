def integer_params_decorated(value):
    def func(*args):
        lst = list(args)[1:]
        for i in lst:
            if not isinstance(i, int):
                raise TypeError("Аргументы должны быть целыми числами")
    return func
