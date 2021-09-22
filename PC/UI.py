import tkinter
import tkinter.ttk
import tkinter.messagebox

from DB import DB
from Keyboard import KeyHandler

class UI():

	curdb = 1

	def __init__(self):
		self.window = tkinter.Tk()
		self.window.title("Key-mapper")
		self.db = DB(UI.curdb)

		#Set Frame
		self.container = tkinter.Frame(self.window)
		self.container.pack()

		self.main = tkinter.Frame(self.container)
		self.main.grid(row=0, column=0, sticky='nsew')

		self.binding = tkinter.Frame(self.container)
		self.binding.grid(row=0, column=0, sticky='nsew')

		self.setUI()
		self.setAction()
		self.showMainframe()
		self.combo.current(0)

	def setUI(self):
		self.left = tkinter.Frame(self.main)
		self.left.grid(row=0, column=0)

		self.right = tkinter.Frame(self.main)
		self.right.grid(row=0,column=1)

		self.apply = tkinter.Button(self.left, text = 'Apply', width = 13, height = 2)
		self.apply.grid(row=0, column=0)

		self.new = tkinter.Button(self.left, text = 'New', width = 13, height = 2)
		self.new.grid(row=0, column=1)

		self.delete = tkinter.Button(self.left, text = 'Delete', width = 13, height = 2)
		self.delete.grid(row=0, column=2)

		self.preset = tkinter.Label(self.left, text = 'Preset', width = 13, height = 2)
		self.preset.grid(row=1, column=0)

		self.combo = tkinter.ttk.Combobox(self.left, state='readonly')
		self.combo.grid(row=1, column=1, columnspan=2)

		self.rename = tkinter.Label(self.left, text = 'Rename', width = 13, height = 2)
		self.rename.grid(row=2, column=0)

		self.newname = tkinter.Entry(self.left)
		self.newname.grid(row=2, column=1)

		self.set = tkinter.Button(self.left, text = 'Set', width = 10, height = 2)
		self.set.grid(row=2, column=2)

		self.keylist = tkinter.ttk.Treeview(self.right, columns=['one', 'two'], displaycolumns=['one', 'two'])
		self.keylist.pack()
		self.keylist.column('#0', width=0, stretch='no')

		self.keylist.column('one', anchor='center', width=80)
		self.keylist.heading('one', text='Sensor', anchor='center')

		self.keylist.column('two', anchor='center', width=200)
		self.keylist.heading('two', text='Keybinding', anchor='center')

		self.labelvar = tkinter.StringVar()
		self.pressK = tkinter.Label(self.binding, textvariable=self.labelvar, font=("Courier", 22))
		self.pressK.pack(expand = True)

	def setAction(self):
		self.apply['command'] = self.applyclick
		self.new['command'] = self.newclick
		self.delete['command'] = self.deleteclick
		self.set['command'] = self.setclick
		self.combo.bind("<<ComboboxSelected>>", self.comboclick)

		for i in range(8) :
			self.keylist.tag_bind("tag{}".format(i),sequence="<Double-1>", callback=lambda event, row = i: self.showBindingframe(event, row))

	def applyclick(self):
		self.db.apply()
		UI.curdb = int(self.combo.get()[0])

	def updateTable(self) :
		for i in self.keylist.get_children():
			self.keylist.delete(i)
		data = self.db.getalldata()
		for i in range(len(data)) :
			self.keylist.insert('',index=i, values=data[i], tags='tag'+str(i))

	def updateCombo(self) :
		values = []
		dbnames = self.db.getDBnames()
		for i in range(len(dbnames)):
			values.append("{}. {}".format(i+1, dbnames[i][0]))
		self.combo['values'] = values

	def comboclick(self, event) :
		num = int(self.combo.get()[0])
		self.db.selectDB(num)
		self.updateTable()

	def newclick(self) :
		num = len(self.db.getDBnames())+1
		self.db.createDB(num)
		self.updateCombo()
		self.combo.current(num-1)
		self.updateTable()

	def deleteclick(self) :
		self.db.deleteDB()
		self.updateCombo()
		self.combo.current(0)
		self.updateTable()

	def showMainframe(self) :
		self.main.tkraise()
		self.main.focus_set()
		self.updateTable()
		self.updateCombo()

	def setclick(self) :
		index = int(self.combo.get()[0])
		oldname = self.combo.get()[3:]
		newname = self.newname.get()
		if newname == oldname :
			tkinter.messagebox.showerror("Error", "you can't use the same name")
		elif newname == "":
			tkinter.messagebox.showerror("Error", "type new name")
		else :
			self.db.renameDB(newname)
			self.newname.delete(0, tkinter.END)
			self.updateCombo()
			self.combo.current(index-1)

	def showBindingframe(self, event, row) :
		self.binding.tkraise()
		self.binding.focus_set()
		self.labelvar.set("Press the key")

		keyhandler = KeyHandler()
		keyhandler.startListener()
		self.window.update()

		keyhandler.isWorking = True
		while(keyhandler.isWorking):
			if keyhandler.keyset != "":
				self.labelvar.set(keyhandler.keyset)
				self.window.update()

		keyhandler.endListener()
		if keyhandler.isEnter == True:
			self.db.updatekey(row, keyhandler.keyset)
		self.showMainframe()
