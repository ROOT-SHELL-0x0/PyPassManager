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
	def parse_command(self,command):
		args=command.split()
		match args:
			case "/add_new":
				Name=str(input("$>Name:"))
				URL=str(input("$>URL:"))
				Password=str(input("$>Password:"))







PyPassManager()