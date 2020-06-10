password = 'a123456'
x = 3 #剩余机会
while x > 0:
	x = x - 1
	q = input('请输入你的密码: ')
	if q == password:
		print('登陆成功!')
		break
	else:
		print('密码错误!')
		if x > 0:
			print('还有', x, '次机会')
		else:
			print('没机会尝试了！要锁账号了!')