#python实现列表去重的方法
#先通过集合去重，在转列表
lis=[11,12,13,12,15,16,13]
a=set(lis)
print(a)
[x for x in a]