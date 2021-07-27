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

# 字典查
# 1.dictName['key'] 不存在会报错
# 2.dictName.get('key') 不存在不会报错，会返回None
# dictName.get('key','value') 不存在指定key时会返回
# 可以使用in/not in判断是否存在对应key  -- 'key' in dictName

# 字典改
# 1.为已存在的key赋予一个新的value值
# dictName['key'] = value 一次修改一个key对应的value
# 2.调用update，多个value修改
# dictName.update({'k1':'v11', 'k2':'v22'...}) 冒号可换成等号
# dictName.update([('k1','v11'), ('k2','v22')...])

# 字典增
# 1.dictName['k3'] = v3 k3原本不存在，一次加一个
# 2.调用方法update，以下k1,k2不存在于字典中
# dictName.update({'k1':'v11', 'k2':'v22'...}) 冒号可换成等号
# dictName.update([('k1','v11'), ('k2','v22')...])

# 字典删
# 1.调用方法pop
# dictName.pop('key') key如果不存在报错
# dictName.pop('key', value) key如果不存在返回value
# 2.使用del语句
# del dictName['key'] 一次只删除一个
# 3.使用popitem
# dictName.popitem('key') 会返回被删除的KV对
# 4.清空
# dictName.clear() 清空整个字典

# 为字典设置key的默认value值
# dictName.setDefault('k1', 'default') default内容自定义
# 如果k1已存在value，则返回k1原来的value
# 如果k1不存在，则返回default

# 字典视图
# 调用一下的方法返回对象
# 1.keys返回字典所有key的视图 --> dict_keys(['k1','k2'...])
# 2.values返回字典所有value的视图 --> dict_values(['v1','v2'...])
# 3.items返回所有k-v视图 --> dict_items([('k1','v1'),('k2','v2')...])
# 视图会随字典变化而变化

# 使用字典创建格式化字符串
# 1.百分号作为占位符
# print('aaaa %s, bbbb %s' % (dictName['k1'], dictName['k2']))
# 打印时会将k1,k2对应的v1,v2会依次塞到前两个百分号中
# 或者print('aaaa %(k1)s, bbbb %(k2)s' % dictName) 可以自定义传入位置
# 2.使用花括号作为占位符
# print('aaaa {}, bbbb {}' .format(dictName['k1'], dictName['k2']))
# print('aaaa {k1}, bbbb {k2}' .format_map(dictName))
