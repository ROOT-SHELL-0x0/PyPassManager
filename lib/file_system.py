

class file_system():
	def __init__(self):
		None

	def read_data_file(self,path_to_file):
		try:
			f=open(path_to_file,"rb",encoding="utf-8")
			data=f.read()
			return data
			
		except Exception as e:
			print(Fore.RED+e+Style.RESET_ALL)
