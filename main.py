#class Object(object): pass

class added1:

	def __init__(self):
		pass

	def test(self):
		print("ADDED 1")

class added2:

	def __init__(self):
		pass

	def test(self):
		print("ADDED 2")


class main:

	def __init__(self):
		pass

	def go(self):
		print("GO")


m = main()
m.__class__ = type('Test',(main,added1),{})
m.test()
m.go()
m.__class__ = type('Test2',(main,added2),{})
m.test()
