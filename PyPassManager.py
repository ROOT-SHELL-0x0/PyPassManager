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
				Name=str(input("$>Name (Press Enter to empty):"))
				URL=str(input("$>URL or App:"))
				Password=str(input("$>Password:"))
				if len(self.MASTER_PASSWORD)==0:
					self.MASTER_PASSWORD=str(input("MASTER_PASSWORD:"))*100

				if Name:
					crypt_Name=self.crypt_system.crypt_data(Name,self.MASTER_PASSWORD)
				else:
					Name="NULL"
					crypt_Name=self.crypt_system.crypt_data(Name,self.MASTER_PASSWORD)

				crypt_URL=self.crypt_system.crypt_data(URL,self.MASTER_PASSWORD)
				crypt_Password=self.crypt_system.crypt_data(Password,self.MASTER_PASSWORD)


				output=self.file_system.write_data(crypt_Name,crypt_URL,crypt_Password)
				if output:
					print(Fore.RED+str(output)+Style.RESET_ALL)
				else:
					print(Fore.GREEN+"New password added!"+Style.RESET_ALL)


			case "/show_all":
				if len(self.MASTER_PASSWORD)==0:
					self.MASTER_PASSWORD=str(input("$>MASTER_PASSWORD:"))*100

				data=self.file_system.show_all(self.MASTER_PASSWORD)
				if not data:
					print(Fore.RED+"No saved password!"+Style.RESET_ALL)
					return


				for data_pack in data:
					if data_pack[0] != "NULL":
						print(Fore.GREEN+"Name:"+self.crypt_system.decrypt_data(data_pack[0],self.MASTER_PASSWORD)+Style.RESET_ALL)
					print(Fore.GREEN+"URL:"+self.crypt_system.decrypt_data(data_pack[1],self.MASTER_PASSWORD)+Style.RESET_ALL)
					print(Fore.GREEN+"Password:"+self.crypt_system.decrypt_data(data_pack[2],self.MASTER_PASSWORD)+Style.RESET_ALL)
					print("\n"+"\n")
































	def mainloop(self):
		while True:
			command=str(input("$>"))
			if len(command)==0:
				None
			else:
				self.parse_command(command)










PyPassManager().mainloop()