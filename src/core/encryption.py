from cryptography.fernet import Fernet
import base64
import os

class EnvVaultEncryption:
    def __init__(self, key=None):
        if key is None:
            self.key = self.generate_key()
        else:
            self.key = key

    def generate_key(self):
        return base64.urlsafe_b64encode(os.urandom(32))

    def encrypt(self, data):
        fernet = Fernet(self.key)
        return fernet.encrypt(data.encode())

    def decrypt(self, encrypted_data):
        fernet = Fernet(self.key)
        return fernet.decrypt(encrypted_data).decode()