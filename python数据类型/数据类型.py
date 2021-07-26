# 获取变量的数据类型
print(type(18))
print(type(5.6))
print(type('hahhahaha'))


# 整数
# 进制表示方式（1）二（2）八（3）十（4）十六
print(118)
print(0b01110110)
print(0o166)
print(0x76)

# 进制转换
# 十进制转二进制
print(bin(118))
# 十进制转八进制
print(oct(118))
# 十进制转十六进制
print(hex(118))

# 整数创建
# 不传递参数时返回0
print(int())
# 第二个参数指定进制
print(int('1110110', 2))
print(int(118.2))

# 浮点数
print(0.123456789)
# 浮点数创建
print(float(213131))
print(float('23342'))

# 科学计数法
# men表示m*10^n
print(6.023e-19)

# 浮点数存储不精确性,采用二进制存储，可能存在误差
print(1.1+2.2-3.3)
print(1.1+2.2)
# 需要引入decimal模块进行计算浮点数，可用fractions进行处理分数
from decimal import Decimal
print(Decimal('1.1')+Decimal("2.2"))

from fractions import Fraction
print(Fraction(11,10) + Fraction(2,3))

# 布尔类型 True 和 False / 0和1
print(5>3) # True 为1
print(3>5) # False 为0
print(True == 1)
print(False == 1)


