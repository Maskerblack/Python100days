# 100天精通Python（基础篇）——第22天：eval 函数基础以及危险警告



## **1. eval()函数的概念**

哇哦，eval()函数听起来就像是一个小魔术师，它可以把字符串转换成可执行的表达式，然后把结果呈现给你。只需把想要执行的表达式放进去，它就会像变魔术一样，把结果变出来。不过，它还有两个可选的小助手，globals和locals，它们分别是全局和局部的命名空间。如果你提供了globals参数，它必须是一个字典类型；而locals参数可以是任意的映射对象。简而言之，eval()函数就像一个变魔术的小助手，可以在字符串和其他数据类型之间进行转换。

## **2. eval()函数语法**

**语法格式**：

```python
eval(expression[, globals[, locals]])
```

**参数说明**：

- expression：表达式，就是你想让eval函数执行的那一串东西。
- globals：全局命名空间，如果提供了，就必须是一个字典对象。我再说一次，必须是字典！必须是字典！必须是字典！
- locals：局部命名空间，如果提供了，可以是任何映射对象。

**返回值**：执行表达式后的结果。

eval函数里有两个可选的小助手globals和locals，它们就是命名空间的名字。那么命名空间是什么呢？

## **3. 命名空间**

命名空间就像是对象的名字地图。大多数情况下，命名空间都是用Python字典来实现的，不过也有例外，比如优化性能的时候。命名空间的例子有abs()函数、内置异常等等，甚至还有模块里的全局名称和函数里的局部名称。在不同的命名空间里，名字是互不干扰的。举个例子，两个不同的模块可以都定义一个maximize函数，但不会造成混淆，因为用户使用函数时必须要指定模块名。

点号后面的名字就是属性。比如说，z.real里面，real就是对象z的属性。严格来说，对模块中名称的引用就是属性引用。比如modname.funcname，modname是模块对象，funcname是模块的属性。模块的属性和模块中定义的全局名称之间有直接的映射关系，它们共享相同的命名空间。

属性有时是只读的，有时是可写的。如果属性是可写的，那就可以给它赋值。如果模块的属性是可写的，就可以用modname.the_answer=42这种方式来赋值。用del语句可以删除可写属性，比如delmodname.the_answer会把modname对象中的the_answer属性删除掉。

命名空间是在不同时刻创建的，而且它们有着不同的生命周期。内置名称的命名空间是在Python解释器启动时创建的，永远不会被删除。模块的全局命名空间是在读取模块定义时创建的，通常会持续到解释器退出。从脚本文件或者交互式界面读取的代码是作为__main__模块调用的一部分，也有自己的全局命名空间。内置名称实际上也是在模块里的，也就是builtins。

函数的局部命名空间是在调用函数时创建的，在函数返回或者抛出不在函数内部处理的错误时被删除。每次递归调用都会有自己的本地命名空间。

Python用命名空间来记录变量的轨迹，命名空间就是一个字典，键是变量名，值是变量值。

**当一行代码要使用变量 x 的值时，Python 会到所有可用的名字空间去查找变量，按照如下顺序:**

- 局部命名空间 - 就是当前函数或者类的方法。如果函数定义了一个局部变量 x，或者一个参数 x，Python 会使用它，然后停止搜索。
- 全局命名空间 - 就是当前的模块。如果模块定义了一个名为 x 的变量，函数或者类，Python 会使用它然后停止搜索。
- 内置命名空间 - 对每个模块都是全局的。作为最后的尝试，Python 会假设 x 是内置函数或者变量。

**Python的全局命名空间储存在一个叫做globals()的字典对象里；局部命名空间则储存在一个叫做locals()的字典对象里。你可以用print (locals())来查看函数体内的所有变量名和变量值。**

## **4. 在示例中融入一些幽默**

### **1. 数学运算：**

这里是我们的数学课，做些简单的数学运算来活跃一下气氛吧！让我们看看 Python 是如何处理加减乘除的：

```python
>>> # 加法
>>> result = eval("1 + 1")
>>> print(result)
2
>>> # 减法
>>> result = eval("2 - 1")
>>> print(result)
1
>>> # 乘法
>>> result = eval("2 * 1")
>>> print(result)
2
>>> # 除法
>>> result = eval("10 / 1")
>>> print(result)
10.0
```

### **2. 字符串重复：**

想象一下，你是一位复读机，重复你看到的内容，就像这样：

```python
>>> result = eval("'-' * 5")
>>> print(result)
-----
```

### **3. 字符串转列表：**

我们的字符串现在想变身成列表了，让我们来实现这个小小的魔术吧！

```python
>>> str1 = "[0, 1, 2, 3, 4]"
>>> result = eval(str1)
>>> print(result)
[0, 1, 2, 3, 4]
>>> print(type(result))
<class 'list'>
```

### **4. 字符串转字典：**

看，这个字符串想要成为一个字典！让我们满足它的愿望吧！

```python
>>> str1 = "{'name': '小明', 'age': 10}"
>>> result = eval(str1)
>>> print(result)
{'name': '小明', 'age': 10}
>>> print(type(result))
<class 'dict'>
```

### **5. 字符串转元组：**

字符串现在想变成元组了，咱们就给它这个机会吧！

```python
>>> str1 = "(1,2,3,4)"
>>> result = eval(str1)
>>> print(result)
(1, 2, 3, 4)
>>> print(type(result))
<class 'tuple'>
```

### **6. 与其他函数结合使用：**

这里是一个有趣的实例，我们让用户输入一个数字，然后给它加上 555，看看会发生什么神奇的事情吧！

```python
x = eval(input('请输入一个数字：'))
y = x + 555
print(y)
```

运行结果：

![18416cc14d0e96b190a11a92ff19680a](https://flower-1324274955.cos.ap-shanghai.myqcloud.com/18416cc14d0e96b190a11a92ff19680a.png)

### **7. globals参数案例**

```python
>>> b = {'a': 4}
>>> temp = eval("a+1", b)
>>> print(temp)
5
>>> print(type(temp))
<class 'int'>
```

**8. locals参数案例**

```python
>>> A = 'a+b+c'
>>> B = {'a': 10, 'b': 20}
>>> C = {'b': 30, 'c': 40}
>>> temp = eval(A, B, C)
>>> print(temp)
80
>>> print(type(temp))
<class 'int'>
```

## **5. eval函数的危险之处（重中之中）**

> 哎呀呀，小心啊，这个`eval()`函数有点像一个神奇的魔法盒子，你给它一个字符串，它就能把里面的表达式计算出来，太神奇了！但是，别被它的魔法迷惑了，它也有点像魔幻的黑洞，一不小心就会把你卷进去，不得了啊！
>
> python中eval函数的用法十分的灵活，但也十分危险，安全性是其最大的缺点。在开发时千万不要使用eval直接转换input的结果，因为如果用户直接通过os这个模块来调用system方法可以执行任何的终端命令，这样细想很恐怖，家底都给暴露出来了。所以不要滥用eval函数！！！

```python
eval("__import__('os').system('dir')")
```

**等价代码**：

```python
import os
os.system("终端命令")
```

- 如果执行成功，就像变魔术一样，它会返回 0
- 如果失败了，就会冒出一串错误信息，就像魔法变戏法失败了一样。

**运行结果**：

![图片](https://flower-1324274955.cos.ap-shanghai.myqcloud.com/640)

##  

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)