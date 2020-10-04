class descriptor1:
	def __init__(self):
		self._data = 1

	def __set__(self,instance,value):
		if value > 0:
			self._data = value
		if value <= 0:
#			raise ValueError
#		self._data = value
		else:
			print('value should be <= 0')

	def __get__(self,instance,owner):
		return self._data

	def __delete__(self,instance):
		del self._data
		return True

class obj1:
	f = descriptor1()
	def __init__(self):
		self.value1 = 'datavalue'

instance1 = obj1()

print(instance1.value1)
instance1.f = -5
print(instance1.f)
instance1.f = 4
print(instance1.f)
instance1.f = -3
print(instance1.f)
print("instance2 : ")
instance2 = obj1()
print(instance2.f)