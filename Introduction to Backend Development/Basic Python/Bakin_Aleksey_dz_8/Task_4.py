def val_checker(func_lambda):
    def _val_checker(func):
        def logger(param):
            if func_lambda(param):
                print(func(param))
            else:
                raise ValueError(f'wrong val {param}')

        return logger

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


a = calc_cube(5)
a = calc_cube(-5)
