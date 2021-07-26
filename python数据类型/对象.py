# None代表something，可用于清空对象
print(id(None))

# 序列类型range
# 可以调用内置方法创建, 返回值是一个迭代器对象
# 1.range(stop)
# 2.range(start, stop)
# 3.range(start, stop, step)
print(range(5))
print(list(range(5)))
print(list(range(2,5,2)))
# 用not in 或 in 检查是否存在某元素
print(3 in range(2,5,2))

# 列表
# list相当于数组，指定索引找到对应的数据，可重复，可动态伸缩
# 创建
# 1.使用中括号
list1 = [1,3,5,7,9,2,4,6,8,0]
print(list1)
# 获取列表元素下标
print(list1.index(9))
# 获取0下标和5下标之间的1的下标
print(list1.index(1, 0, 5))
# 获取对应下标元素
#print(list1[0])
# 切片一次获得多个元素，允许越界
# 语法[start:stop:step](不包含stop元素),不指定则包含最后一个元素   最终的结果也是list
# step为正数时，不指定start默认为list第一个，不指定stop默认为list最后一个，
# 为负则全部相反
list2 = [1,2,4,6,7,9,0,7,6,5,3]
print(list2[1:9:2]) # [2, 6, 9, 7]
print(list2[::])    # [1, 2, 4, 6, 7, 9, 0, 7, 6, 5, 3]
print(list2[::-1])  # [3, 5, 6, 7, 0, 9, 7, 6, 4, 2, 1]
print(list2[9:6:-1])

# slice
# slice(stop)
# slice(start, stop)
# slice(start, stop, step) 等价于 list[start:stop:step]
