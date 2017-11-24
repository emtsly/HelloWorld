for i in range(1, 5):
    print(i)
else:
    print('The for loop is over')

for i in range(1, 5, 2):
    print(i)
    if i > 2:
        break
else:
    print('The for loop is over')

print(list(range(5)))
# range()每次只会生成一个数字，如果你希望获得完整的数字列表，要在使用range()时候调用list().
print(range(5))