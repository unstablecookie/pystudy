# author github.com/stephengrice
class Node(objects):

	def insert(self,d):
		if self.data == d:
			return False
		elif d < self.data:
			if self.left:
				return self.left.insert(d)
			else:
				self.left = Node(d)
				return True
		else:
			if self.right:
				return self.right.insert(d)
			else:
				self.right = Node(d)
				return True
	def find(self,d):
		if self.data == d:
			return True
		elif d < self.data and self.left:
			return self.left.find(d)
		elif d > self.data and self.right:
			return self.right.find(d)
		return False
	def preorder(self,l):
		#the list of data objects so far in the traversal
		l.append(self.data)
		if self.left:
			self.left.preorder(l)
		if self.right:
			self.right.preorder(l)
		return l
	def inorder(self,l):
		#the list of data objects so far in the traversal
		if self.left:
			self.left.preorder(l)
		l.append(self.data)
		if self.right:
			self.right.preorder(l)
		return l
	def postorder(self,l):
		# the list of data objects so far in the traversal
		if self.left:
			self.left.preorder(l)
		if self.right:
			self.right.preorder(l)
		l.append(self.data)
		return l
class BTS(objects):
	#returns True is succesfully inserted, false if exists
	def insert(self,d):
		if self.root:
			return self.root.insert(d)
		else:
			self.root = Node(d)
			return True
	def find(self,d):
		if self.root:
			return self.root.find(d)
		else:
			return False
	def remove(self,d):
	#returns true if node is successfully removed, false if not removed
	#1 empty tree?
		if self.root == None:
			return False
		# 2 deleting root node
		if self.root.data == d:
			# root has no children
			if self.root.left is None and self.root.right is None:
				self.root = None
				return True
			#root node has left child
			elif self.root.left and self.root.right is None:
				self.root = self.root.left
				return True
			# root node has right child
			elif self.root.left is None and self.root.right:
				self.root = self.root.right
				return True
			# root node has two children
			else:
				moveNode = self.root.right
				moveNodeParent = None

				while moveNode.left:
					moveNodeParent = moveNode
					moveNode = moveNode.left

				self.root.data = moveNode.data
				if moveNode.data < moveNodeParent.data:
					moveNodeParent.left = None
				else:
					moveNodeParent.right = None
				return True
		#find node to remove
		parent = None
		node = self.root
		while node and node.data != d:
			parent = node
			if d < node.data:
				node = node.left
			elif d > node.data:
				node = node.right
		# 3 node not found
		if node == None or node.data != d:
			return False
		# 4 Node has no children
		elif node.left is None and node.right is None:
			if d < parent.data:
				parent.left = None
			else:
				parent.right = None
			return True
			#5 node has left child only
		elif node.left and node.right is None:
			if d < parent.data:
				parent.left = node.left
			else:
				parent.right = node.left
			return True
		# 6 node has right child only
		elif node.left is None and node.right:
			if d < parent.data:
				parent.left = node.right
			else:
				parent.right = node.right
			return True
		# 7 node has left and right child
		else:
			moveNodeParent = node
			moveNode = node.right
			while moveNode.left:
				moveNodeParent = moveNode
				moveNode = moveNode.left
			node.data = moveNode.data
			if moveNode.right:
				if moveNode.data < moveNodeParent.data:
					moveNodeParent.left = moveNode.right
				else:
					moveNodeParent.right = moveNode.right
			else:
				if moveNode.data < moveNodeParent.data:
					moveNodeParent.left = None
				else:
					moveNodeParent.right = None
			return True
	def preorder(self):
		#Returns list of data elements resulting from preorder tree traversal
		if self.root:
			return self.root.preorder([])
		else:
			return []
	def postorder(self):
		#Returns list of post-order elements
		if self.root:
			return self.root.postorder([])
		else:
			return []
	def inorder(self):
		#Returns list of in-order elements
		if self.root:
			return self.root.inorder([])
		else:
			return []