import pytest

from btreetest.binarytree import Node,BST

def test_createTree():
	test_tree = BST()
	assert test_tree.root == None
def test_insert():
	args = [44,66,28]
	test_tree = BST()
	for arg in args:
		test_tree.insert(arg)
	assert test_tree.root.data == args[0]
	assert test_tree.root.right.data == args[1]
	assert test_tree.root.left.data == args[2]
def test_find():
	args = [44,66,28]
	not_exist = 11
	test_tree = BST()
	for arg in args:
		test_tree.insert(arg)
	assert test_tree.find(args[1]) == True
	assert test_tree.find(not_exist) == False
def test_preorder():
	args = [44,50,20,15,28,76]
	test_tree = BST()
	result = [44, 20, 15, 28, 50, 76]
	for arg in args:
		test_tree.insert(arg)
	assert test_tree.preorder() == result
def test_inorder():
	args = [44,50,20,15,28,76]
	test_tree = BST()
	result = [20, 15, 28, 44, 50, 76]
	for arg in args:
		test_tree.insert(arg)
	assert test_tree.inorder() == result
def test_postorder():
	args = [44,50,20,15,28,76]
	test_tree = BST()
	result = [20, 15, 28, 50, 76, 44]
	for arg in args:
		test_tree.insert(arg)
	assert test_tree.postorder() == result
def test_remove_leaf():
	args = [44,50,20,15,28,76]
	test_tree = BST()
	for arg in args:
		test_tree.insert(arg)
	todel = 15
	result = [44, 20, 28, 50, 76]
	test_tree.remove(todel)
	assert test_tree.preorder() == result
def test_remove_root():
	args = [44,50,20,15,28,76]
	root = 44
	test_tree = BST()
	for arg in args:
		test_tree.insert(arg)
	test_tree.remove(root)
	assert test_tree.root.data == 50