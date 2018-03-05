# coding=utf-8
"""
Python练习实例1

题目: 有四个数字：1、2、3、4，能组成多少个互不相同且无重复的三位数？各是多少。
分析：可填在百位、十位、个位的数字都是1、2、3、4，组成所有的排列之后，再去掉不满足条件的排列。

"""

from itertools import permutations

# 方法一
print("方法一")
# 保存符合条件的个数
cnt = 0

# 通过循环嵌套组成三位数
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            # 确保三位数字互不重复
            if (i != j) and (i != k) and (j != k):
                cnt += 1
                print("第", '%2s' % cnt, "组三位数：", i * 100 + j * 10 + k)

print("互不相同且无重复的三位数共有", cnt, "个")

# 方法二
print("")
print("方法二")
# 使用列表保存符合条件的数
dict1 = []

for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            # 确保三位数字互不重复
            if (i != j) and (i != k) and (j != k):
                dict1.append(i * 100 + j * 10 + k)

print(dict1)
print("互不相同且无重复的三位数共有", len(dict1), "个")

# 方法三
print("")
print("方法三")
# 使用极值进行判断，降低时间复杂度
dict2 = []

# 该最大值最小值已认为缩小一部分，默认应从 (111,445)
for i in range(123, 433):
    a = i % 10  # 获取个位数
    b = (i % 100) // 10  # 获取十位数
    c = (i % 1000) // 100  # 获取百位数

    if a != b and a != c and b != c and 0 < a < 5 and 0 < b < 5 and 0 < c < 5:
        print(i)
        dict2.append(i)

print(dict2)
print("互不相同且无重复的三位数共有", len(dict2), "个")

# 方法四
print("")
print("方法四")
# 使用Python自带函数permutations
dict3 = []

for i in permutations([1, 2, 3, 4], 3):
    dict3.append(i)

print(dict3)
print("互不相同且无重复的三位数共有", len(dict3), "个")




