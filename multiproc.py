import time

from multiprocessing import Pool

counter1 = 30000000

def calc1(a):
    while a < counter1:
    	a += 1
    return a

if __name__ == '__main__':
	processpool = Pool(processes=4)

	begin1 = time.time()

	runtime1 = processpool.apply_async(1)
	runtime2 = processpool.apply_async(1)
	runtime3 = processpool.apply_async(1)
	runtime4 = processpool.apply_async(1)

	processpool.close()
	processpool.join()

	end1 = time.time()
	print("it took : ", end1 - begin1 , "seconds to count till", counter1," with multi-threading")