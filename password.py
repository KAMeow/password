password = 'a123456'
x = 3
while True:
	q = input('请输入你的密码: ')
	if q == password:
		print('登陆成功!')
		break
	else:
		x = x - 1
		print('密码错误! 还有', x, '次机会')
		if x == 0:
			break