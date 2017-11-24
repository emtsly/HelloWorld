age = 20
name = 'Swaroop'

print('{0} was {1} years old when he wrote this book'.format(name, age))
print('Why is {0} playing with that python?'.format(name))

# 对于浮点数 '0.333' 保留小数点(.)后三位
print('{0:.3f}'.format(1.0/3))
# 使用下划线填充文本，并保持文字处于中间位置
# 适用(^)定义 '___hello___'字符串长度为11
print('{0:_^11}'.format('hello'))
# 基于关键词输出 'Swaroop wrote A Byte of Python'
print('{name} worte {book}'.format(name='Swaroop', book='A Byte of Python'))

# end指定结尾格式
print('a', end='')
print('b', end=' ')
print('c', end=' ')
print('d')