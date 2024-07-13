dict_example: dict[str, str|int] = {'Name': '小明', 'Age': 20}

#遍历键
for key in dict_example.keys():
    print(key)
    
for k in dict_example:
    print(k)
"""
Name
Age
"""

# 遍历值
for value in dict_example.values():
    print(value)
"""
小明
20
"""

# 遍历键值对
for key, value in dict_example.items():
    print(key, value)
"""
Name 小明
Age 20
"""

