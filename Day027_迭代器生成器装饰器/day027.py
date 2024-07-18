def w1(fn):
    """装饰器函数"""
    print("正在装饰w1")
    def inner():
        print("---1---")
        return "<b>" + fn() + "</b>"
    return inner

def w2(fn):
    """装饰器函数"""
    print("正在装饰w2")
    def inner():
        print("---2---")
        return "<i>" + fn() + "</i>"
    return inner

@w1
@w2
def f1():
    """业务函数"""
    print("---3---")
    return "hello python"

ret = f1()
print(ret)


"""
执行结果：
正在装饰w2
正在装饰w1
---1---
---2---
---3---
<i><b>hello python</b></i>

代码执行到`@w1` 就开始装饰了，我们并没有调用`f1()`都输出了`---正在装饰---`，我们调用的是装饰完后的结果。
`@w1`在最上面，下面需要是一个函数，可下面是`@w2`，必须先等`@w2`装饰完再装饰，所以先输出`正在装饰w2`
"""