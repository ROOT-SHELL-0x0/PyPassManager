from colorama import Fore,init,Style
from banner import *


class PyPassManager():
	def  __init__(self):
		init()
		print(Fore.GREEN+banner+Style.RESET_ALL)

		#self.crypt_system=crypted_system()
		#self.file_system=file_systen()


PyPassManager()