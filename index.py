print('Python基础')
#Python基础
a = 100;
if a >100:
	print(a)
else:
	print(-a)
	
	
#数据类型和变量	
print('''韩国
美国
中国''')

#常量除法
A = 10
B = 3
print(A/B)
print(A//B);
print(A%B);

#格式化
print('hello,%s' % 'world')
print('票价值 %f' % 1000)
print('%d 块钱都不给我' % 100)
print('%x' % 500)


#循环
names = ['陈俊龙','陈飞','陈海龙']
for value in names:
	print(value)
	
	
sum = 0
for x in [1,2,3,4,5,6,7,8,9]:
	sum = sum+x
print(sum)
	

#list组合
sum = 0
num  = list(range(101))
print(num)
for k in num:
	sum = sum+k
print (sum)


sum = 0
n = 100

#while循环
while n >0:
	sum = sum +n
	if sum >200:
		break
	if n%2 == 0:
		continue
	n = n-1
print(sum)


#dict
data = {'chenjunlong':9999,'cuixigtao':34,'pangxingyu':56}
print(data['chenjunlong'])


#判断某个索引值'cjl'是否存在
print('cjl' in data)

#判断某个索引值是否存在，不存在返回100
#print(data.get('cjl','cjl默认索引值不存在返回该句话'))



#set集合
s =  set([1,2,3,3,5,6])
print(s)
s.add(4)
print(s)
s.remove(4)
print(s)


#定义函数
def my_abs(num):
	my_noabs()
	if not isinstance(num,(int,float)):
		raise TypeError('参数只能为整数或浮点数')
	if num >0:
		return num
	else:
		return -num
		
def my_noabs():
	pass
		
		
print(my_noabs())
print(my_abs(4))


#高级特性
print('获取 1,3,5,7,9,11')
L = []
n = 1
while n <=99:
	L.append(n);
	n = n+2
	
print(L)

#切片 
print('切片取出前2个元素')
M = []
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
for i in range(3):
	M.append(L[i])
	
R = [0,1,2,3,4,5,6,7,8,9,10,11]	
print(M)
print(R[0:3])
print(R[:10:2])#取前十个，但是每两个取一个
print(R[::5])#所有数，每5个取一个


print(L[-3:])#倒数取3个元素
print(L[-3:-1])
print(L[-3:-2])#倒数取3个元素，在从索引等于-2开始倒取
print(L[:])#这样就可以原样复制一个list



#迭代
print('迭代')
from collections import Iterable
print(isinstance('abc',Iterable)) #str 是否可迭代
print(isinstance([1,2,3],Iterable)) #list是否可迭代
print(isinstance(123,Iterable))


#列表生成器
print(list(range(2,10))) #创建2<=&&<10的所有整数
print('1X1,2X2,3X3,……')
#第一种语法
arr = []
for value in range(1,11):
	arr.append(value * value)
	
print(arr)
#第二种语法
a = [x * x for x in range(1,11)] 
print(a)

print('for循环中嵌入if语句筛选仅偶数的平方')
b = [x * x for x in range(1,11) if x%2 == 0]
print(b)

print('使用两层循环，生成全排列')
c = [m + n for m in 'ABC' for n in 'XYZ']
print(c)

print('列表生成式,列出当前目录下的所有文件和目录名')
import os #导入os模块
e = [d for d in os.listdir('.')] #os.listdir可以列出文件和目录
print(e)

print('for 循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value')
d = {'x':'A','y':'B','z':'C'}
f = d.items()
print(f)
for k,v in f:
	print(k,'=',v)

#第二种方式
g = [k + '=' + v for k,v in f]
print(g)


print('把list中所有的字符串变成小写,注；非字符串类型类型没有lower()')
H = ['Hello','World','IBM',55,'APPle']
#i = [s.lower() for s in H] 这样会报错
i = [s.lower() for s in H if isinstance(s,str)]#这样会把55过滤掉
print(i)

#生成器:generator
print('')
print('生成器generator')
J = (x * x  for x in range(10))
print(J)
print('通过next()函数获得generator的下一个返回值')
print(next(J))
print(next(J))
print(next(J))
print('利用for循环')
for s in J:
	print(s)
	
#迭代器：
print('')
print('判断一个对象是否为Iterable对象')
from collections import Iterable
print(isinstance([],Iterable))
print(isinstance({},Iterable))
print(isinstance('abc',Iterable))
print(isinstance((x for x in range(10)),Iterable))
print(isinstance(100,Iterable))

print('可以被next()函数调用并不断返回下一个值的对象称为迭代器:')




















