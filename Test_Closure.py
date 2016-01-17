def a(x,y):
	def b(x,y):
		print(x,y,sep='   ')
	def c():
		print(x,y,sep = '             ')
		#c()
	b(3,9)
	c()
	
a(5,2)