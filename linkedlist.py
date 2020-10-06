class Node:
	def __init__(self,dataval = None):
		self.dataval = dataval
		self.nextval = None

class SLinkedList:
	def __init__(self):
		self.headval = None

	def listprint(self):
		printval = self.headval
		while printval is not None:
			print(printval.dataval)
			printval = printval.nextval
	def atbeg(self,newdat):
		f = self.headval
		self.headval = newdat
		self.headval.nextval = f
	def atend(self,newdat):
		newnode = Node(newdat)
		if self.headval is None:
			self.headval = newnode
			return
		laste = self.headval
		while(laste.nextval):
			laste = laste.nextval
		laste.nextval = newnode
	def inbetw(self,midnode,newdat):
		if midnode is None:
			print("midnode is absent")
			return
		newnode = Node(newdat)
		newnode.nextval = midnode.nextval
		midnode.nextval = newnode
	def delitem(self,remkey):
		head = self.headval
		if (head is not None):
			if head.dataval == remkey:
				self.headval = head
				head = None
				return

		while (head is not None):
			if head.dataval == remkey:
				break
			prev = head
			head = head.nextval
		if (head == None):
			return
		prev.nextval = head.nextval

		head = None