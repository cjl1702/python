



#随机生成一个数字
import random

secret = random.randint(1,10)


#用户输入数字
print("请输入一个数字是否能猜中电脑里面的，你有三次机会")
temp = input("请输入")

guess = int(temp)

while guess != secret:
	temp = input("哎呀你又猜错了，请重新输入吧:")
	
	guess = int(temp)
	
	if guess > secret:
		print('哥，大了，大了~~')
	else:
		print('姐，小了，小了~~')
		
		
	if guess == secret:
		print("哎呦喂，还让你猜中了")
		print("不过猜中也没奖啊")


print("游戏结束，不玩啦~~")
