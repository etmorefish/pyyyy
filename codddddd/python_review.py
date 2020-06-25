# 必须有一个内嵌函数
# 内嵌函数必须引用外部函数中的变量
# 外部函数的返回值必须是内嵌函数
# 闭包函数，指的是定义在一个函数内部的函数，被外层函数包裹着，其特点是可以访问到外层函数的名字
# def outer(): 
#     num = 1 
#     def inner(): 
#         print(num) 
#     return inner  # 基于对象的概念我们可以将内层函数返回到外界使用，从而打破函数调用的层级限制，但无论在何处调用，作用区域都在外层函数内
                                                                    
# f = outer()   # f == inner f指向的是inner的内存地址，但是f本身确实是一个全局变量，可以在任何位置调用f
# num = 100                                                         
# f()  # 1

# 普通的装饰器
# 
# import functools
# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print('call %s():' % func.__name__)
#         print('args = {}'.format(*args))
#         return func(*args, **kwargs)

#     return wrapper

# @log
# def test(p):
#     print(test.__name__ + " param: " + p)
    
# test("I'm a param")



# 请实现一个装饰器，限制改函数被调用的频率，如4秒一次
# import time
# def time_pay(func):
#     def inner(*args, **kwargs):
#         for i in range(10):
#             print(i + 1)
#             time.sleep(2)
        
#         res = func(*args, **kwargs)
#         return res
#     return inner

# @time_pay
# def func1():
#     print('from func1...'+ func1.__name__)

# func1()

# 装饰器这一语法体现了Python中函数是第一公民，函数是对象、是变量，可以作为参数、可以是返回值，非常的灵活与强大。


# 邮箱正则
import re
email = '849078367@qq.56.com'
if re.match(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$', email):
    print('OK !')
else:
    print('error')