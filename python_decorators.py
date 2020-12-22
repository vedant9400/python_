# decorator example of adding numbers

def my_dec(func):
    def inner1(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return inner1


@my_dec
def my_func(*args, **kwargs):
    try:
        x = 0
        for i in args:
            x += int(i)
        return x
    except Exception as e:    
        return e.args[0]

x = my_func('23','23', '23s') 
print(x)
