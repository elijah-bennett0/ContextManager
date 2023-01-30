

class toolCtx:

	def __init__(self):
		pass

	def runTool(self):
		print("Tool Run")

class pluginCtx:

	def __init__(self):
		pass

	def runPlugin(self):
		print("Plugin Run")

class coreCtx:

	def __init__(self):
		pass

	def go(self):
		print("Core Context")

def main():

	core = coreCtx()
	core.go()

	print("TOOL CONTEXT:")
	core.__class__ = type('Tool',(coreCtx, toolCtx),{})
	core.runTool()

	print("PLUGIN CONTEXT:")
	core.__class__ = type('Plugin',(coreCtx, pluginCtx),{})
	core.runPlugin()

	print("BOTH CONTEXTS:")
	core.__class__ = type('All',(coreCtx, toolCtx, pluginCtx),{})
	core.runTool()
	core.runPlugin()

if __name__ == "__main__":
	main()
