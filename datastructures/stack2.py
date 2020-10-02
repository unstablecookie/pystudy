from queue import LifoQueue
stack1 = LifoQueue()

stack1.put('haha')
stack1.put({'jajd':'dwdd'})
stack1.put(('sdasd','123'))
stack1.put('5')

print(stack1.get())