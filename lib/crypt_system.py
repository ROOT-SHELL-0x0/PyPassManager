from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from base64 import urlsafe_b64encode
import os

class crypt_system:
	def __init__(self):
		None

	def crypt_data(self,data,key):

		password = key.encode()  
		salt = b"IOIidisiEO-eJKDKJdufiorjf"
		kdf = PBKDF2HMAC(
			algorithm=hashes.SHA256(),
			length=32,
			salt=salt,
			iterations=100000,
			backend=default_backend())
		key = urlsafe_b64encode(kdf.derive(password))

		cipher=Fernet(key)
		return cipher.encrypt(data.encode()).decode()
		





	def decrypt_data(self,data,key):
		password = key.encode()  
		salt = b"IOIidisiEO-eJKDKJdufiorjf"
		kdf = PBKDF2HMAC(
			algorithm=hashes.SHA256(),
			length=32,
			salt=salt,
			iterations=100000,
			backend=default_backend())
		key = urlsafe_b64encode(kdf.derive(password))

		cipher=Fernet(key)
		return cipher.decrypt(data.encode()).decode()
		


