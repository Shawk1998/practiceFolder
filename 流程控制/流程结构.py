# 顺序结构
# 从上往下
print('开始')
print('程序体')
print('结束')

# 代码块缩进
# 所有代码块的缩进要相同，不相同py会理解为不同的代码块

# if
a = 50
if a < 50:
    print('<');
elif a == 50:
    print('=');
else:
    print('>=');


# 循环结构
# while
i=1
while i<11:
    print(i)
    i+=1

# for 遍历后面的集合内的数据
for j in range(1,11):
    print(j)
    j+=1

for char in '123':
    print(char)

for kk in [1,2,4]:
    print(kk)

# 遍历字典
dict = {'k1':'v1', 'k2':'v2', 'k3':'v3'}
# 遍历所有key
for key in dict:
    print(key)
# 遍历所有value
for value in dict.values():
    print(value)
# 遍历所有k-v
for key,value in dict.items():
    print(key,'-',value)


# 带索引的序列遍历
L = ['a','b','c','d']
index = 0
for item in L:
    print('L[{}] = {}'.format(index, item))
    index+=1

for index in range(len(L)):
    print('L[{}] = {}'.format(index, L[index]))

# while
index = 0
while index < len(L):
    print('L[{}] = {}'.format(index, L[index]))
    index += 1
