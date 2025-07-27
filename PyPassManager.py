from colorama import Fore,init,Style
from banner import *
from lib.file_system import *
from lib.crypt_system import *
from time import sleep


class PyPassManager():
	def  __init__(self):



		init()
		print(Fore.GREEN+banner+Style.RESET_ALL)

		self.crypt_system=crypt_system()
		self.file_system=file_system()
		self.MASTER_PASSWORD=""


		self.file_system.db_cursor.execute('''SELECT * FROM Data WHERE Name="TEST_DATA" ''')
		print(len(self.file_system.db_cursor.fetchall()))
		if self.file_system.db_cursor.fetchall()==0:
			print("NO MASTER_PASSWORD")
			while True:
				if len(self.MASTER_PASSWORD)==0:
					self.MASTER_PASSWORD=str(input("$>set MASTER_PASSWORD:"))*100
				else:
					break
				if len(self.MASTER_PASSWORD)==0:
					print(Fore.RED+"Wrong input!"+Style.RESET_ALL)

			crypt_TEST_DATA=self.crypt_system.crypt_data("TEST_DATA",self.MASTER_PASSWORD)
			sql = "INSERT INTO Data (Name, URL_App, Password) VALUES (?, ?, ?)"
			self.file_system.db_cursor.execute(sql, ("TEST_DATA","TEST_DATA",crypt_TEST_DATA))

		self.file_system.db.commit()





	def parse_command(self,command):
		args=command.split()
		match args[0]:
			case "/add_new":
				while True:
					Name=str(input("$>Name (Press Enter to empty):"))
					if Name:
						break
					else:
						print(Fore.RED+"Empty input!"+Style.RESET_ALL)


				while True:
					URL=str(input("$>URL or App:"))
					if URL:
						break
					else:
						print(Fore.RED+"Empty input!"+Style.RESET_ALL)
				while True:
					Password=str(input("$>Password:"))
					if Password:
						break
					else:
						print(Fore.RED+"Empty input!"+Style.RESET_ALL)

				self.get_MASTER_PASSWORD()
				self.add_new(Name,URL,Password)


			case "/show_all":
				self.get_MASTER_PASSWORD()

				data=self.file_system.show_all(self.MASTER_PASSWORD)
				if not data:
					print(Fore.RED+"No saved password!"+Style.RESET_ALL)
					return


				for data_pack in data:
					if data_pack[0] == "TEST_DATA":
						continue
						

					print(Fore.GREEN+"Name:"+self.crypt_system.decrypt_data(data_pack[0],self.MASTER_PASSWORD)+Style.RESET_ALL)
					print(Fore.GREEN+"URL:"+self.crypt_system.decrypt_data(data_pack[1],self.MASTER_PASSWORD)+Style.RESET_ALL)
					print(Fore.GREEN+"Password:"+self.crypt_system.decrypt_data(data_pack[2],self.MASTER_PASSWORD)+Style.RESET_ALL)
					print("\n"+"\n")

			case "/get_password":
			    if len(args)!=2:
			    	print(Fore.RED+"Use /get_password <Name>"+Style.RESET_ALL)
			    	return
			    Name=args[1]
			    self.get_MASTER_PASSWORD()
			    self.get_password(Name)




	def add_new(self,Name,URL,Password):
		crypt_Name=self.crypt_system.crypt_data(Name,self.MASTER_PASSWORD)
		crypt_URL=self.crypt_system.crypt_data(URL,self.MASTER_PASSWORD)
		crypt_Password=self.crypt_system.crypt_data(Password,self.MASTER_PASSWORD)
		output=self.file_system.write_data(crypt_Name,crypt_URL,crypt_Password)
		if output:
			print(Fore.RED+str(output)+Style.RESET_ALL)
		else:
			print(Fore.GREEN+"New password added!"+Style.RESET_ALL)




	def get_password(self,Name):
		crypt_Name=self.crypt_system.crypt_data(Name,self.MASTER_PASSWORD)

		data=self.file_system.db_cursor.execute("SELECT * FROM Data WHERE Name = ?", (crypt_Name,)).fetchall()
		if len(data)==0:
			print(Fore.RED+"Wrong Name!"+Style.RESET_ALL)
			return
		print(Fore.GREEN+"Name:"+self.crypt_system.decrypt_data(data[0][0],self.MASTER_PASSWORD)+Style.RESET_ALL)
		print(Fore.GREEN+"URL:"+self.crypt_system.decrypt_data(data[0][1],self.MASTER_PASSWORD)+Style.RESET_ALL)
		print(Fore.GREEN+"Password:"+self.crypt_system.decrypt_data(data[0][2],self.MASTER_PASSWORD)+Style.RESET_ALL)








	def get_MASTER_PASSWORD(self):


		if len(self.MASTER_PASSWORD)==0:
			self.MASTER_PASSWORD=str(input("$>MASTER_PASSWORD:"))*100
			data_for_check=self.file_system.check_MASTER_PASSWORD()

			if self.crypt_system.decrypt_data(data_for_check[0][2],self.MASTER_PASSWORD) !="TEST_DATA":
				print(Fore.RED+"Wrong MASTER_PASSWORD!"+Style.RESET_ALL)
				sleep(3)
				self.MASTER_PASSWORD=""
				self.get_MASTER_PASSWORD()
		else:
			return
		if len(self.MASTER_PASSWORD)==0:
			print(Fore.RED+"Wrong input!"+Style.RESET_ALL)
			self.get_MASTER_PASSWORD()












	def mainloop(self):
		while True:
			command=str(input("$>"))
			if len(command)==0:
				None
			else:
				self.parse_command(command)










PyPassManager().mainloop()