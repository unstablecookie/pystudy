# unfinished
class Node:
	def __init__(self,data):
		self.data = data
		self.previous = None
		self.next = None

class Queue:
	def __init__(self):
		self.size = 0
		self.root = None
		self.end = None

	def addNode(self,data):
		self.size += 1
		if self.root == None:
			self.root = Node(data)
			node = self.root
		elif self.root != None:
			node = self.root
			newnode = Node(data)
			newnode.next = node
			node.previous = newnode
	def searchNode(self,data):
		if self.root == None:
			return False
		elif self.root != None:
			node = self.root
			prevnode = None
			result = None
			if node.data == data:
				return node
			while node.data != data:
				prevnode = node
				node = prevnode.next
			result = node
			return result
	def getNode(self):
		self.size -= 1
		if self.root == None:
			return False
		else:
			node = self.root
			while node.next:
				prevnode = node
				node = node.next
			prevnode.next = None
			return node.data