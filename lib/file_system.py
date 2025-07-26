import sqlite3,os

from colorama import Fore,init,Style

class file_system():
	def __init__(self):
		self.data="data/"
		self.db=sqlite3.connect(self.data+"data.db")
		self.db_cursor=self.db.cursor()
		self.db_cursor.execute('''CREATE TABLE IF NOT EXISTS Data (Name TEXT NOT NULL,URL_App TEXT NOT NULL,Password TEXT NOT NULL)''')
		self.db.commit()


	def write_data(self,Name,Url_app,password):

		try:
			sql = "INSERT INTO Data (Name, URL_App, Password) VALUES (?, ?, ?)"
			self.db_cursor.execute(sql, (Name, Url_app, password))
			self.db.commit()
			return 
		except Exception as e:
			return e



	def show_all(self,MASTER_PASSWORD):
		self.db_cursor.execute("SELECT * FROM Data")

		return self.db_cursor.fetchall()
		
		# for data_pack in self.db_cursor.fetchall():
		# 	if Name != "NULL":
		# 		print(Fore.GREEN+crypt_system().decrypt(data_pack[0])+Style.RESET_ALL)
		# 	print(Fore.GREEN+crypt_system().decrypt(data_pack[1])+Style.RESET_ALL)
		# 	print(Fore.GREEN+crypt_system().decrypt(data_pack[2])+Style.RESET_ALL)
		# 	print("\n"+"\n")






	def check_first_start(self):
		if os.path.isfile(self.data+"data.db"):
			return 0
		else:
			print("Create Table")
			self.db_cursor.execute('''CREATE TABLE IF NOT EXISTS Data (Name TEXT NOT NULL,URL/App TEXT NOT NULL,Password TEXT NOT NULL)''')
			self.db.commit()


