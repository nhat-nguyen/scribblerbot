import Tkinter as tk
import ttk

class knightBot:
	def newButton(self, x, y, window):
		button = ttk.Button(window, text = str(x) + ', ' + str(y), command = lambda: self.add((x, y))).grid(row = x + 1, column = y)

	def add(self, point):
		(self.points).append(point)
		self.textbox.insert(tk.END, str(point) + u" \u2192 ")

	def output(self):
		print self.points

	def clear(self):
		del self.points[:]

	def halt(self):
		stop()
		
	def __init__(self, master):
		self.buttons = [[] for i in range(8)]
		self.points = []
		window = tk.Frame(master, bg = "#ececec")		
		window.pack()
		self.input = tk.StringVar()
		self.textbox = tk.Entry(window, width = 700, bg = "white",textvariable = self.input)
		self.textbox.grid(row = 0, columnspan = 1000)

		for x in range(0, 8):
			for y in range(8):
				self.buttons[x].append(self.newButton(x, y, window))

		self.start = ttk.Button(window, text = 'Start', command = lambda: self.add('.'), width = 9).grid(row = 1, column = 9, padx = 20)
		self.halt = ttk.Button(window, text = 'Stop', command = lambda: halt(), width = 9).grid(row = 2, column = 9, padx = 20)
		self.steps = ttk.Button(window, text = 'Compute', command = lambda: self.output(), width = 9).grid(row = 3, column = 9, padx = 20)
		self.showResults = ttk.Button(window, text = 'Results', command = lambda: self.output(), width = 9).grid(row = 4, column = 9, padx = 20)
		self.clearPoints = ttk.Button(window, text = 'Clear', command = lambda: self.clear(), width = 9).grid(row = 5, column = 9, padx = 20)

root = tk.Tk()

root.minsize(width = 770, height = 230)
root.maxsize(width = 770, height = 230)
root.wm_title(u"\u265E" + " knightBot")

Nhat = knightBot(root)
root.mainloop()