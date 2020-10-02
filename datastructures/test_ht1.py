import pytest

from hashtable import Node,HashTable

def test_createtable():
	total_size = 10
	test_table = HashTable(total_size)
	assert len(test_table.buckets) == total_size
def test_hash():
	total_size = 50
	test_table = HashTable(total_size)
	test_hash = 'testhash'
	test_result = 44
	assert test_table.hash(test_hash) == test_result
def test_insert():
	total_size = 50
	test_table = HashTable(total_size)
	key1 = 'test1'
	value1 = 'passed1'
	hashvalue = test_table.hash(key1)
	test_table.insert(key1,value1)
	assert test_table.buckets[hashvalue] != None
def test_find():
	total_size = 50
	test_table = HashTable(total_size)
	key1 = 'test1'
	value1 = 'passed1'
	test_table.insert(key1,value1)
	assert test_table.find(key1) == value1
def test_remove():
	total_size = 50
	test_table = HashTable(total_size)
	key1 = 'test1'
	value1 = 'passed1'
	test_table.insert(key1,value1)
	test_table.remove(key1)
	assert test_table.find(key1) == None
def test_remove_node():
	total_size = 50
	test_table = HashTable(total_size)
	key1 = 'hah'
	value1 = 'passed1'
	key2 = 'lol'
	value2 = 'passed2'
	test_table.insert(key1,value1)
	test_table.insert(key2,value2)
	test_table.remove(key1)
	test_table.remove(key2)
	assert test_table.buckets[40] == None
