import re

def type_logger(func):
    def logger(param):
        rez = func(param)
        name_func = (re.findall(r'\s(.+)\s[a]',str(func)))[0]
        return f'{name_func}({param}: {type(param)})\n{param} в степени 3 = {rez}'
    return logger
@type_logger
def calc_cube(x):
   return x ** 3

a = calc_cube(5)
print(a)
