# very basic decorator
def decorator1(infunction1):
	def wrapper():
		infunction1()
		print('internal function')
	return wrapper

@decorator1
def outfunction1():
	print('outer function')
	return 0

outfunction1()

#docorator with variable
def decorator2(infunction2):
	def wrapper(*args,**kwargs):
		wrap1 = infunction2(*args)
		print(wrap1)
		return wrap1 + 10
	return wrapper

@decorator2
def outfunction2(a,b):
	return a * b

print(outfunction2(2,5))

#double decorating

def decorator3(infunction3):
	def wraper():
		infunction3()
		print('inside decorator3')
	return wraper

def decorator4(infunction4):
	def wraper():
		infunction4()
		print('inside decorator4')
	return wraper

@decorator3
@decorator4
def outfunction3():
	print('outer function')

outfunction3()