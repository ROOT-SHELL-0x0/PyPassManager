class crypt_system:
	def __init__(self):
		None

	def crypt_data(self,data,key):
		ciphertext = ''.join(chr(ord(p) ^ ord(k)) for p, k in zip(data, key))
		return ciphertext

	def decrypt_data(self,data,key):
		decrypted_text = ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(data, key))
		return decrypted_text