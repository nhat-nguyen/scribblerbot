from Tkinter import *

class calcWindow:
	def __init__(self, master):
		self.clearme = False
		self.points = []
		self.grid = [[] for i in range (8)]
		window = Frame(master)		
		window.pack()
		for x in range(8):
			for y in range(8):
				self.grid[x].append(Button(window, text = '+', command = lambda: self.add((x, y))).grid(row = x, column = y))

	def add(self, point):
		self.points.append(point)

	
root = Tk()

# root.minsize(width = 200, height = 150)
# root.maxsize(width = 200, height = 150)
root.wm_title(u"\u265E" + " knightbot")

Nhat = calcWindow(root)
root.mainloop()