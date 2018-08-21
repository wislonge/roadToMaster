import thread

class hello():
	def __init__(self,word):
		self.word=word;
	def test_hello(self):
		#print("hello word"+self.word);
		thread.start_new_thread(self.test,("hello",))
		while 1:
			pass
	def test(self,arg):
		print(arg)
if __name__=='__main__':	
	h=hello("shit")
	h.test_hello()
	
