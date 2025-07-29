import sqlite3,os

from colorama import Fore,init,Style

class file_system():
	def __init__(self):
		self.data="data/"
		self.db=sqlite3.connect(self.data+"data.db")
		self.db_cursor=self.db.cursor()
		self.db_cursor.execute('''CREATE TABLE IF NOT EXISTS Data (Name TEXT NOT NULL,URL_App TEXT NOT NULL,Password TEXT NOT NULL)''')


	





	def write_data(self,Name,Url_app,password):

		try:
			sql = "INSERT INTO Data (Name, URL_App, Password) VALUES (?, ?, ?)"
			self.db_cursor.execute(sql, (Name, Url_app, password))
			self.db.commit()
			return 
		except Exception as e:
			return e




	def check_MASTER_PASSWORD(self):
		self.db_cursor.execute('''SELECT * FROM Data WHERE Name="TEST_DATA"''')
		data=self.db_cursor.fetchall()
		return data


	def show_all(self,MASTER_PASSWORD):
		self.db_cursor.execute("SELECT * FROM Data")

		return self.db_cursor.fetchall()
	


