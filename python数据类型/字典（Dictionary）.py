# 1.KV 结构
# 2.key是不可变对象
# 3.指定的key对应唯一的value
# 4.通过key计算hash值，找对应value
# 5，可动态分配和收缩空间
# 6.字典会浪费较大内存，利用空间提高查询效率

# 创建字典
# 1.{'k1': 'v1', 'k2': 'v2'... }
# 空字典 {}
# 2.调用dict构造方法
# dict({'k1': 'v1', 'k2': 'v2'...})
# dict(k1='v1', k2='v2'...)
# dict([('k1,v1'), ('k2','v2')...])
# dict(zip(range(n),'abcdef...')) {0:'a', 1:'b'...}
# 3.调用fromKeys方法
# dict.fromkeys(['k1','k2'...]) 默认value为None
# dict.fromkeys(('k1','k2'...))
# dict.fromkeys(['k1','k2'...], 'N/A') 所有值为N/A
