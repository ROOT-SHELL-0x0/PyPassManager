from colorama import Fore,init,Style
from banner import *
from lib.file_system import *
from lib.crypt_system import *
from time import sleep
from argparse import ArgumentParser


class PyPassManager():
	def  __init__(self):



		init()
		print(Fore.GREEN+banner+Style.RESET_ALL)

		self.crypt_system=crypt_system()
		self.file_system=file_system()


		self.parser=ArgumentParser(description="PyPassManager")
		self.parser.add_argument("--act",type=str,choices=["add","get","del","show_all","extract_to_file"],help="Add new password")
		self.parser.add_argument("--Name",type=str,help="Name for actions")
		self.parser.add_argument("--Url",type=str,help="Url for actions")
		self.parser.add_argument("--Pass",type=str,help="Pass for actions")
		self.parser.add_argument("--Path",type=str,help="Path to extract")


		self.MASTER_PASSWORD=""


		self.file_system.db_cursor.execute('''SELECT * FROM Data WHERE Name="TEST_DATA" ''')
		if len(self.file_system.db_cursor.fetchall())==0:
			print("NO MASTER_PASSWORD")
			while True:
				if len(self.MASTER_PASSWORD)==0:
					self.MASTER_PASSWORD=str(input("$>set MASTER_PASSWORD:"))*100
				else:
					break
				if len(self.MASTER_PASSWORD)==0:
					print(Fore.RED+"Wrong input!"+Style.RESET_ALL)

			crypt_TEST_DATA=self.crypt_system.crypt_data("TEST_DATA",self.MASTER_PASSWORD)
			print(crypt_TEST_DATA)
			sleep(10)
			sql = "INSERT INTO Data (Name, URL_App, Password) VALUES (?, ?, ?)"
			self.file_system.db_cursor.execute(sql, ("TEST_DATA","TEST_DATA",crypt_TEST_DATA))

		self.file_system.db.commit()



	def mainloop(self):
		args=self.parser.parse_args()
		if args.act==None:
			while True:
				command=str(input("$>"))
				if len(command)==0:
					None
				else:
					type_=None
					self.parse_command(type_,command)
		else:
			type_="parser"
			self.parse_command(type_,args)





	def parse_command(self,type_,command):
		if type_=="parser":
			act=command.act
		else:
			args=command.split()
			act=args[0]


		match act:
			case "add":
				while True:
					if type_ == "parser":
						Name=command.Name
						if Name is None:
							Name=str(input("$>Name:"))
							
					else:
						Name=str(input("$>Name:"))

					if Name:
						break
					else:
						print(Fore.RED+"Empty input!"+Style.RESET_ALL)


				while True:
					if type_=="parser":
						URL=command.Url
						if URL is None:
							URL=str(input("$>URL or App:"))

					else:
						URL=str(input("$>URL or App:"))

					if URL:
						break
					else:
						print(Fore.RED+"Empty input!"+Style.RESET_ALL)

				while True:
					if type_=="parser":
						Password=command.Pass
						if Password is None:
							Password=str(input("$>Password:"))
					else:
						Password=str(input("$>Password:"))
						if Password:
							break
						else:
							print(Fore.RED+"Empty input!"+Style.RESET_ALL)

				self.get_MASTER_PASSWORD()
				self.add_new(Name,URL,Password)


			case "show_all":
				self.get_MASTER_PASSWORD()

				data=self.file_system.show_all(self.MASTER_PASSWORD)
				if len(data)==1:
					print(Fore.RED+"No saved password!"+Style.RESET_ALL)
					return


				for data_pack in data:
					if data_pack[0] == "TEST_DATA":
						continue
						

					print(Fore.GREEN+"Name:"+self.crypt_system.decrypt_data(data_pack[0],self.MASTER_PASSWORD)+Style.RESET_ALL)
					print(Fore.GREEN+"URL:"+self.crypt_system.decrypt_data(data_pack[1],self.MASTER_PASSWORD)+Style.RESET_ALL)
					print(Fore.GREEN+"Password:"+self.crypt_system.decrypt_data(data_pack[2],self.MASTER_PASSWORD)+Style.RESET_ALL)
					print("\n"+"\n")

			case "get":
			    if type_=="parser":
			    	Name=command.Name
			    	if Name is None:
			    		Name=str(input("$>Name:"))
			    else:
			    	if len(args)!=2:
			    		print(Fore.RED+"Use 'get <Name>'"+Style.RESET_ALL)
			    		return
			    	else:
			    		Name=args[1]
			    self.get_MASTER_PASSWORD()
			    self.get_password(Name)


			case "del":
			    if type_=="parser":
			    	Name=command.Name
			    	if Name is None:
			    		Name=str(input("$>Name:"))
			    else:
			    	if len(args)!=2:
			    		print(Fore.RED+"Use 'del <Name>"+Style.RESET_ALL)
			    		return
			    	Name=args[1]
			    self.get_MASTER_PASSWORD()
			    self.delete_password(Name)



			case "extract":
			    if type_=="parser":
			    	path=command.Path
			    	if path is None:
			    		path=str(input("$>Path:"))
			    else:
			    	if len(args)!=2:
			    		print(Fore.RED+"Use 'extract <path/name>'"+Style.RESET_ALL)
			    		return
			    	path=args[1]



			    data_crypt=self.file_system.show_all(self.MASTER_PASSWORD)
			    if not data_crypt:
			    	print(Fore.RED+"No saved password!"+Style.RESET_ALL)
			    	return

			    data=""
			    self.get_MASTER_PASSWORD()
			    for data_pack in data_crypt:
			    	if data_pack[0] == "TEST_DATA":
			    		continue
			    	data+="Name:"+self.crypt_system.decrypt_data(data_pack[0],self.MASTER_PASSWORD)+"\n"
			    	data+="URL:"+self.crypt_system.decrypt_data(data_pack[1],self.MASTER_PASSWORD)+"\n"
			    	data+="Password:"+self.crypt_system.decrypt_data(data_pack[2],self.MASTER_PASSWORD)+"\n"
			    	data+="\n"+"\n"
			    
			    try:
			    	f=open(path,"a+",encoding="utf-8")
			    	f.write(data)
			    	f.close()
			    except Exception as e:
			    	print(Fore.RED+str(e)+Style.RESET_ALL)
			    	return

			    print(Fore.GREEN+f"Succeessfully extract to {path}"+Style.RESET_ALL)





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
		for data_pack in data:
			print(Fore.GREEN+"Name:"+self.crypt_system.decrypt_data(data_pack[0],self.MASTER_PASSWORD)+Style.RESET_ALL)
			print(Fore.GREEN+"URL:"+self.crypt_system.decrypt_data(data_pack[1],self.MASTER_PASSWORD)+Style.RESET_ALL)
			print(Fore.GREEN+"Password:"+self.crypt_system.decrypt_data(data_pack[2],self.MASTER_PASSWORD)+Style.RESET_ALL)
			print('\n'+'\n')


	def delete_password(self,Name):
		

		crypt_Name=self.crypt_system.crypt_data(Name,self.MASTER_PASSWORD)

		data=self.file_system.db_cursor.execute("SELECT * FROM Data WHERE Name = ?", (crypt_Name,)).fetchall()
		if len(data)==0:
			print(Fore.RED+"Wrong Name!"+Style.RESET_ALL)
			return

		check=str(input(Fore.YELLOW+"Confirm deletion (type 'yes'):"+Style.RESET_ALL))
		if check!="yes":
			print("Stopping...")
			return

		
		self.file_system.db_cursor.execute("DELETE FROM Data Where Name=?",(crypt_Name,))
		self.file_system.db.commit()
		print(Fore.GREEN+"Succeessfully deleted!"+Style.RESET_ALL)





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




PyPassManager().mainloop()