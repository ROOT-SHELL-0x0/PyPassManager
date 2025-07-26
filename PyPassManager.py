from colorama import Fore,init,Style
from banner import *
from lib.file_system import *
from lib.crypt_system import *


class PyPassManager():
	def  __init__(self):



		init()
		print(Fore.GREEN+banner+Style.RESET_ALL)

		self.crypt_system=crypt_system()
		self.file_system=file_system()
		self.MASTER_PASSWORD=""

	def parse_command(self,command):
		args=command.split()
		match args[0]:
			case "/add_new":
				Name=str(input("$>Name (Press Enter to empty:"))
				URL=str(input("$>URL or App:"))
				Password=str(input("$>Password:"))
				if len(self.MASTER_PASSWORD)==0:
					self.MASTER_PASSWORD=str(input("MASTER_PASSWORD:"))

				if Name:
					crypt_Name=self.crypt_system.crypt_data(Name,self.MASTER_PASSWORD)
				crypt_URL=self.crypt_system.crypt_data(URL,self.MASTER_PASSWORD)
				crypt_Password=self.crypt_system.crypt_data(Password,self.MASTER_PASSWORD)


				print(crypt_URL)
				print(crypt_Password)


				print("Dectypt URL:"+self.crypt_system.decrypt_data(crypt_URL,self.MASTER_PASSWORD))
				print("Dectypt Pass:"+self.crypt_system.decrypt_data(crypt_Password,self.MASTER_PASSWORD))


	def mainloop(self):
		while True:
			command=str(input("$>"))
			if len(command)==0:
				None
			else:
				self.parse_command(command)










PyPassManager().mainloop()