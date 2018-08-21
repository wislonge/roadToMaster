import threadpool

def fun1(a):
	print(a)

if __name__=='__main__':
	tp=threadpool.ThreadPool(10)
	req=threadpool.makeRequests(fun1,"shit")
	tp.putRequest(req)
	tp.wait()
	print("hello")
