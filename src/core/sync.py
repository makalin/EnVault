import requests
from .encryption import EnvVaultEncryption

class EnvVaultSync:
    def __init__(self, server_url, key):
        self.server_url = server_url
        self.key = key

    def push(self, env_vars):
        encryptor = EnvVaultEncryption(self.key)
        encrypted_vars = {k: encryptor.encrypt(v).decode() for k, v in env_vars.items()}
        response = requests.post(f"{self.server_url}/push", json=encrypted_vars)
        return response.json()

    def pull(self):
        response = requests.get(f"{self.server_url}/pull")
        encrypted_vars = response.json()
        decryptor = EnvVaultEncryption(self.key)
        return {k: decryptor.decrypt(v.encode()) for k, v in encrypted_vars.items()}