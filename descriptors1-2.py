class testclass:
	def __init__(self):
		self.value = 'testvalue'
		self._data = 1

	@property
	def propertydata1(self):
		return self._data
	@propertydata1.setter
	def propertydata1(self,newdata):
		if newdata > 0:
			self._data = newdata
		else:
			raise ValueError
	@propertydata1.deleter
	def propertydata1(self):
		del self._data