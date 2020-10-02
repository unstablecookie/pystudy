#author github.com/stephengrice

class Node:
	def __init__(self,key,value):
		self.key = key
		self.value = value
		self.next = None

class HashTable:
	def __init__(self,capacity):
		self.capacity = capacity
		self.size = 0
		self.buckets = [None] * self.capacity
	def hash(self,key):
		hashsum = 0
		#for each char in the key
		for idx, c in enumerate(key):
			#add (index + length of key) ^ (current char code)
			hashsum += (idx + len(key)) ** ord(c)
			#perfoms modulus to keep hashsum in range [0,self.capacity - 1]
			hashsum = hashsum % self.capacity
		return hashsum

	def insert(self,key,value):
		# increment size of a table
		self.size += 1
		#compute index of the key
		index = self.hash(key)
		#go to the node, corresponding for the hash
		node = self.buckets[index]
		#if the bucket is empty:
		if node is None:
			#Create node,add it. return
			self.buckets[index] = Node(key,value)
			return
		#collision! iterate to the end of the linked list at provided index
		prev = node
		while node is not None:
			prev = node
			node = node.next
		#add a new node at the end of the list with provided key/value
		prev.next = Node(key,value)

	def find(self,key):
		#compute hash
		index = self.hash(key)
		#go to the first node in list at bucket
		node = self.buckets[index]
		#traverse the linked list at this node
		while node is not None and node.key != key:
			node = node.next
		#now node is the requested key/value or None
		if node is None:
			# not found
			return None
		else:
			#found - return data
			return node.value
	def remove(self, key):
		# compute hash
		index = self.hash(key)
		node = self.buckets[index]
		prev = None
		# iterate to the requested node
		while node is not None and node.key != key:
			prev = node
			node = node.next
		# now, node is either requested node or none
		if node is None:
			return None
		else:
			#the key was found
			self.size -= 1
			result = node.value
			#delete this element in linked list
			if prev is None:
				node = None
				self.buckets[index] = None
			else:
				prev.next = prev.next.next
				node = None
			return result