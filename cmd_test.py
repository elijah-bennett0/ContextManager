import cmd, sys

class toolCtx:

	def __init__(self, arg):
		self.name = "TOOL NAME"
		self.type = "TOOL"

	def do_run(self, arg):
		print("TOOL RAN")

class ContextManager(cmd.Cmd):

	def __init__(self, stdin, stdout, stderr):
		self.intro = "TEST BANNER"
		self.completekey = 'tab'
		self.stdin, self.stdout, self.stderr = stdin, stdout, stderr
		self.cmdqueue = []
		self.setCtx(None)
		self.prompt = "(%s) > " % self.ctx

	def setCtx(self, ctx):
		if ctx is None:
			self.ctx = "Core"
		else:
			self.ctx = ctx
		self.prompt = "(%s) > " % self.ctx

	def emptyline(self):
		pass

	def do_test(self, arg):
		print("TEST COMMAND WORKED")

	def do_use(self, arg):
		# Arg is the name of a tool or plugin. Here well use a fake name just for testing.
		if arg == "test":
			self.setCtx("Tool")
			self.__class__ = type('Tool',(ContextManager,toolCtx),{})

	def do_back(self, arg):
		self.__class__ = type('Core',(ContextManager,),{})
		self.setCtx(None)

if __name__ == "__main__":
	ContextManager(sys.stdin, sys.stdout, sys.stdout).cmdloop()
