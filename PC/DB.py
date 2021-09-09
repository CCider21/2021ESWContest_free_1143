import sqlite3 as sq

FILE = "./KeyMap.db"
Sensors = ["검지 짧게","검지 길게","중지 짧게","중지 길게","약지 짧게","약지 길게","소지 짧게","소지 길게"]

class DB():
	def __init__(self, dbnum):
		self.conn = sq.connect(FILE)
		self.cur = self.conn.cursor()
		self.db = self.getDB(dbnum)

	def getDBnames(self):
		self.cur.execute("SELECT * FROM DB")
		return self.cur.fetchall()

	#select table
	def getDB(self, dbnum):
		names = self.getDBnames()
		if len(names) < dbnum:
			return names[0][0]
		else:
			return names[dbnum-1][0]

	#create table
	def createDB(self, dbnum):
		self.cur.execute("INSERT INTO DB VALUES (?)", ("Custom{}".format(dbnum),))
		self.db = self.getDB(dbnum)

		self.cur.execute("CREATE TABLE "+self.db+" (Sensor TEXT, Key TEXT)")
		for i in range(len(Sensors)):
			self.cur.execute("INSERT INTO "+self.db+" VALUES(?,?)", (Sensors[i], ""))

	#rename table
	def renameDB(self, name):
		# if same name is input get error
		self.cur.execute("ALTER TABLE "+self.db+" RENAME TO "+name)
		self.cur.execute("UPDATE DB SET name = ? WHERE name = ?",(name, self.db))
		self.db = name

	#delete table
	def deleteDB(self):
		tablenum = len(self.getDBnames())
		if tablenum > 1:
			self.cur.execute("DELETE FROM DB WHERE name=(?)", (self.db,))
			self.cur.execute("DROP TABLE " + self.db)
			self.db = self.getDB(1)

	def updatekey(self, sensor, key):
		self.cur.execute("UPDATE "+self.db+" SET Key = ? WHERE Sensor = ?",(key, Sensors[sensor]))

	def getalldata(self):
		self.cur.execute("SELECT * FROM "+self.db)
		return self.cur.fetchall()

	def getkey(self, sensor):
		self.cur.execute("SELECT Key FROM "+self.db+" WHERE Sensor = ?", (Sensors[sensor],))
		return (self.cur.fetchone())[0]


	def apply(self):
		self.conn.commit()

	def selectDB(self, dbnum):
		self.db = self.getDB(dbnum)


	def __del__(self):
		self.conn.commit()
		self.conn.close()

