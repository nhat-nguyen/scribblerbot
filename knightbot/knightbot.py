import Tkinter as tk
import ttk
from bfs import *
from knightMoves import *

class knightBot:
	def redrawButtons(self, window):
		for x in range(6):
			for y in range(6):
				self.buttons[x][y].config(text = str(x) + ', ' + str(y))

	def clearButtons(self):
		for i in range(6):
			for j in range(6):
				self.buttons[i][j].config(text = "")

	def insertTextBox(self, something):
		self.textbox.insert(tk.END, something)

	def newButton(self, x, y, window):
		button = ttk.Button(window, text = str(x) + ', ' + str(y), command = lambda: self.add((x, y)))
		button.grid(row = x + 1, column = y)
		return button

	def add(self, point):
		(self.points).append(point)
		self.insertTextBox(str(point) + u" \u2192 ")

	def output(self):
		print self.points

	def clear(self, rmPoint, window):
		self.redrawButtons(window)
		self.textbox.delete(0, tk.END)
		if rmPoint:
			del self.points[:]

	def startMoves(self):
		while len(self.points) > 1:
			steps = bfs(self.points[0], self.points[1])
			start = steps[0]
			for cur in steps[1:]:
				delta = (cur[0]-start[0],cur[1]-start[1])
				knightMoves(delta[0], delta[1])
				start = cur
			del self.points[0]

	def compute(self, list):
		route = []
		results = []
		self.textbox.delete(0, tk.END)
		route.extend(bfs(list[0], list[1]))
		for i in range(1, len(list) - 1):
			results = bfs(list[i], list[i + 1])
			route.extend(results[1:])
		j = 0
		self.clearButtons()
		label = dict((i, '') for i in route)

		for i in route:
			label[i] += str(j) + '   '
			self.buttons[i[0]][i[1]].config(text = str(label[i]))
			j += 1
		self.insertTextBox(str(route))

	def __init__(self, master):
		self.buttons = [[] for i in range(6)]
		self.points = []
		window = tk.Frame(master, bg = "#ececec")		
		window.pack()
		self.input = tk.StringVar()
		self.textbox = tk.Entry(window, width = 770, bg = "white", textvariable = self.input)
		self.textbox.grid(row = 0, columnspan = 1000)

		for x in range(6):
			for y in range(6):
				(self.buttons[x]).append(self.newButton(x, y, window))

		self.start = ttk.Button(window, text = 'Start', command = lambda: self.startMoves(), width = 9).grid(row = 1, column = 9, padx = 20)
		self.steps = ttk.Button(window, text = 'Compute', command = lambda: self.compute(self.points), width = 9).grid(row = 2, column = 9, padx = 20)
		self.clearPoints = ttk.Button(window, text = 'Clear', command = lambda: self.clear(True, window), width = 9).grid(row = 3, column = 9, padx = 20)

root = tk.Tk()

root.minsize(width = 770, height = 230)
root.maxsize(width = 770, height = 230)
root.wm_title(u"\u265E" + " knightBot")

Nhat = knightBot(root)
root.mainloop()