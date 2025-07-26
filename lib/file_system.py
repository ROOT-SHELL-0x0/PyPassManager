import sqlite3,os

class file_system():
	def __init__(self):
		self.data="data/"
		self.db=sqlite3.connect(self.data+"data.db")
		self.db_cursor=self.db.cursor()
		self.db_cursor.execute('''CREATE TABLE IF NOT EXISTS Data (Name TEXT NOT NULL,URL_App TEXT NOT NULL,Password TEXT NOT NULL)''')
		self.db.commit()


	def write_data(self,Name,Url_app,password):
		self.db_cursor.execute(f'''INSERT INTO Data (Mame,URL_App,Password) VALUES ({Name},{Url_app},{password})''')



	def check_first_start(self):
		if os.path.isfile(self.data+"data.db"):
			return 0
		else:
			print("Create Table")
			self.db_cursor.execute('''CREATE TABLE IF NOT EXISTS Data (Name TEXT NOT NULL,URL/App TEXT NOT NULL,Password TEXT NOT NULL)''')
			self.db.commit()

