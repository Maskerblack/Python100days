import keyword

print(keyword.kwlist)

'''
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue',
'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in',
'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
'''

print('*' * 50)

print(keyword.iskeyword('if'))

print('-' * 50)

# 使用反斜杠`\`来实现多行语句的效果
print('Hello \
    World!'
)
