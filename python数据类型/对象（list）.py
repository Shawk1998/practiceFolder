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
print(list2[slice(1, 9, 2)]) # [2, 6, 9, 7]

# list查 用in
# 元素 in list 返回boolean

# list改
# 1.listName[n] = m 将n下标元素改为m
# 2.listName[n:m] = [v1, v2, v3...] 使用切片修改，
# 将下标n到m-1的元素替换为[v1,v2,v3...] 右边多list会扩张，少了会收缩
# 切片修改值必须放在中括号中,

# list增
# 1.listName.append(n) 在末尾加n, 如果n是list则将list作为一个元素
# 2.lsitName.extend([v1, v2, v3...]) 将这个list所有元素追加到listName后
# 3.listName.insert(n, value) 在list的n下标插入value
# 4.切片 listName[n:n] = [v1, v2, v3...] 在n下标位置插入v1, v2, v3...
list2[3:3] = [99,98]
print(list2)

# list删
# 1.listName.remove(value) 删除value元素，若有多个删除第一个，不存在报错
# 2.listName.pop(n) 删除n下标元素, 索引不存在报错
# 3.del listName[n]   删除下标为n的元素
#   del listName[n,m] 删除下标为n到m-1的元素
# 4.赋予空列表 listName[n,m] = [] 删除下标为n到m-1的元素
# 5.listName.clear() 清空list

# 加法乘法操作list
# 加法
# listName3 = listName1 + listName2 listName3为2拼接到1上的
# 乘法
# listName2 = listName1*n 2为n个1拼接而成
# 可用于列表初始化

# list比较
# >= > < <=
# 两个列表从第一个元素开始比较，比较结果为第一个不相等的元素的比较值（boolean）
# == 和 is
# ==比较内容，is比较同一性（地址）

# 元素反转
# 1.listName.reverse() 元素倒序
# 2.迭代器对象reversed(listName) 返回一个迭代器对象，交给list处理
print(list(reversed(list2)))

# 列表排序
# 1.listName.sort() 从小到大排序，内容发生变化
list3 = ['asd', 'asda', 'daa', 'd', 'sad', 'ad', 'ad', 'ads']
list2.sort(reverse = True) # 逆序(默认为False)
print(list2)
list3.sort()
print(list3) # None
# 2.sorted(listName) listName不发生变化
print(sorted(list2))

# 多维列表
# 列表中元素也为列表
# 初始化
print([[0 for i in range(3)] for j in range(3)])


